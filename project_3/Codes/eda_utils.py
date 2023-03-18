def show_missing(df):

    # Import libraries
    import pandas as pd
    import numpy as np
    """
    Return a Pandas dataframe describing the contents of a source dataframe including missing values.

    Parameters:
    --------
    df: pandas Dataframe
        dataset to be checked

    Returns:
    --------
    pandas Dataframe with 7 columns
    variables - name of columns in df
    dtypes - the data type of variable
    count - the nunber of non-missing observations of variables
    nunique - the unique nunber of non-missing observations of variables
    missing - the number of missing observations of variables
    pc_missing - the percentage of missing observations of variables
    """
    
    variables = []
    dtypes = []
    count = []
    nunique = []
    missing = []
    pc_missing = []
    
    for item in df.columns:
        variables.append(item),
        dtypes.append(df[item].dtype)
        count.append(len(df[item]))
        nunique.append(df[item].nunique())
        missing.append(df[item].isna().sum())
        pc_missing.append(round((df[item].isna().sum() / len(df[item])) * 100, 2))

    output = pd.DataFrame({
        'variable': variables,
        'dtype': dtypes,
        'count': count,
        'nunique': nunique,
        'missing': missing, 
        'pc_missing': pc_missing
    })
    
    return output



def clean_string(text, stem="none"):
    
    # Import libraries
    import spacy
    sp = spacy.load('en_core_web_sm')
    import re
    import string
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
    from nltk.stem.snowball import SnowballStemmer
    
    """
    Return a string that has been cleaned for text analysis. 
    Lemmatization has higher accuracy than stemming. 
    Lemmatization is preferred for context analysis, but requires more processing power
    Stemming is recommended when the context is not important, it also requires less processing power

    Parameters:
    --------
    text: string
    stem: default="None", choice of NLTK stemming (stem) or lematizing (lem), or spaCy lematizing (spacy)

    Returns:
    --------
    string
    """
    
    final_string = ""

    # Make lower
    text = text.lower()

    # Remove line breaks
    text = re.sub(r'\n', '', text)

    # Remove numbers
    text= re.sub(r'\w*\d\w*', '', text)
    
    # Remove puncuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Tokenize words. Since we have removed punctuations, there's no value add for nltk.tokenzier which required more processing power 
    text = text.split()
        
    # Remove stop words
    if stem in ['stem','lem','none']:
        stopwords = nltk.corpus.stopwords.words("english")
    else:
        stopwords = list(sp.Defaults.stop_words) #sp stopwords is a dictionary
    # manual tweaks to add more stopwords
    stopwords = stopwords + ['hi', 'im']
    text_filtered = [word for word in text if not word in stopwords]

    # Stem or Lemmatize
    # Stemming refers to reducing a word to its root form. Compute, computer, computing, computed => comput. Root form need not be a dictionary word
    if stem == 'stem':
        stemmer = SnowballStemmer(language='english')
        text_stemmed = [stemmer.stem(y) for y in text_filtered]
    #Lemmatization converts words in the second or third forms to their first form variants. Compute, computer, computing, computed => compute, a dictionary word.
    elif stem == 'lem':
        lem = WordNetLemmatizer()
        text_stemmed = [lem.lemmatize(y) for y in text_filtered]
    # spaCy lemmatization. spaCy determines the part-of-speech tag by default and assigns the corresponding lemma
    elif stem == 'spacy':
        text_filtered = sp(' '.join(text_filtered))
        text_stemmed = [y.lemma_ for y in text_filtered]
    else:
        text_stemmed = text_filtered

    final_string = ' '.join(text_stemmed)

    return final_string


def get_top_post(input, ngram_range=(1,1), n=10):

   # Import libraries
    from sklearn.feature_extraction.text import TfidfVectorizer
    import pandas as pd
    
    """
    Using tf-idf, return top 10 n-gram of dataframe. 

    Parameters:
    --------
    df: string
    ngram_range: default=(1,1)

    Returns:
    --------
    [10,1] dataframe
    """
    vectorizer = TfidfVectorizer(ngram_range=ngram_range)
    tfidf = vectorizer.fit_transform(input)
    feature_names = vectorizer.get_feature_names_out()
    tfidf_sorted=tfidf.toarray().sum(axis=0).argsort()[::-1][:n]
    top_ngrams = [(feature_names[i], tfidf.toarray().sum(axis=0)[i]) for i in tfidf_sorted]

    top_ngrams_df = pd.DataFrame(top_ngrams, columns=['feature_names', 'tfidf_scores'])

    return top_ngrams_df