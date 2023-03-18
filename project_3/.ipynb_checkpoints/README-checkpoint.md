<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# <u><b>Project 3:</b></u> Subeddit suitability moderation between r/Discworld r/Cosmere subreddits using NLP classification modelling

<img src="https://www.redditinc.com/assets/images/site/reddit-logo.png" style="float: left; margin: 20px; height: 55px"><br>
### <u><b>About Reddit:</b></u> 
<br>
Reddit is a social aggregation and discussion website. Posts are submitted by registered users (commonly referred to as "Redditors") to the website, which are then voted on and discussed by other Redditors. Posts' content can either be links, text posts, images, or videos. With over 50 million daily active users worldwide, it is understandable that interest will be diverse and not all posts would be of interest to everyone. Therefore to encourage robust discussion, Redditors are required to choose topic-specific user-created communities or "subreddits" (commonly referred to as "subs") most suitable for their post.  
<br>  

Reddit administrators (Reddit employees) moderate the website, whereas subreddit moderators (commonly referred to as "Mods") are done by volunteers who are not paid. Reddit rely on the Mods to maintain the standard of content within each sub, Mods may also settle disputes, levy rules on what is and isn't appropriate and delete or edit content deemed unsuitable for the site. 
<br>  

Since Mods only perform their roles during their free time, it makes sense to leverage on Data Science to perform some routine moderation task such as assessing if the post is on topic. Posting on the wrong sub is such a prevalent problem that there's even a sub to discuss them: r/lostredditors 
<br>  

### <u><b>Problem statement:</b></u> 
<b>This project aims to help r/Discworld and r/Cosmere (two subs that this author is a stan of) mods to perform the routine task of identifying posts that are more suitable for the other sub than their own, so that they can focus their time on more value added services, and the post's Origninal Poster (commonly refered to as "OP") can reach their intended audience. </b>

--------------
### <u><b>Exploratory Data Analysis - non-text features</b></u> 
<br>   
Comparing 'Hot' or popular posts from r/discworld and r/cosmere:  
<br>   

| submission reception| r/discworld                    | r/cosmere                     |
| :------------------ | :----------------------------: | :---------------------------: |
| word_count          | 53                             | <font color='green'>137</font>|
| is_text             | 44%                            | <font color='green'>88%</font>|
| is_media            | <font color='green'>39%</font> | 8%                            |
| is_spoiler          | 5%                             | <font color='green'>78%</font>|
| score               | <font color='green'>163</font> | 72                            |
| upvote_ratio        | <font color='green'>92%</font> | 83%                           |
| total_comments      | 19                             | <font color='green'>27</font> |
| total_awards        | <font color='green'>0.05</font>| 0.00                          |
<br>   
r/cosmere appears to have more content and interactions: with a larger post average word count of 137 vs 53 and more average comments of 27 vs 19. However, it's worth noting that r/cosmere has 110K members while r/discworld only has 80K members, which may explain the greater interaction. r/cosmere posts also have a greater probability to have 'spoiler' tags at 78% vs 5%, or to be a text only post at 88% vs 44%. This is likely due to the cosmere series still being ongoing.
<br>  
r/discword appears to be more rewarding with higher average net score of 163 vs 72, more upvote ration of 92% vs 83%, as well as more awards given. This seems to indicate a more friendly community. r/discworld posts also have a greater probability of being a media only post at 39% vs 8%.
<br>  
### <u><b>Exploratory Data Analysis - text features</b></u> 
<br>   
<img src="./Pictures/wordcloud.png" style="margin: 20px; height: 500px"><br>
<br>   
<img src="./Pictures/venn-words.png" style="fmargin: 20px; height: 500px"><br>
<br>   
<img src="./Pictures/bigrams.png" style="margin: 20px; height: 500px"><br> 
<br>   
--------- 
<br>
<br>
Ignoring words or n-grams unique to the series (e.g `blood stupid johnson`, `auditor trap`, `discworld` for r/discworld and e.g. `tress emerald sea`, `mistborn era`, `mistborn` in r/Cosmere), there are more discussion on spoilers, as well as the most recent book (`tress`, `tress emerald`, `tress emeral sea`) in r/Cosmere. r/discworld have more discussion about the author Sir Terry Pratchett. 
<br>
<br>
Common words appearing in both subs are related to reading (e.g. `book`, `read`) and Redditor's reaction (e.g. `know`, `think`, `like`), which is expected since they are both subs to discuss their respective name-sake fantasy book series universe. 

`do not know` seem to be a common and frequent topic between both subs. Looking at the posts with such phrases, it appears that these Redditors are caveating that they are not aware if the topic in their post have already been discussed on, least it gets downvoted by others.

<i><u>Author's note:</u> While the text preprocessing ultimately choose was spaCy lemmentization, i had explored using NLTK's stemming and lemmentization as well. spaCy's lemmazitation produces better results. spaCy lemmatization is better than NLTK lemmatization as it takes into account part-of-speech tag by default. Lemmatization is better than stemming as context of text is important for this analysis.</i>
<br>   
<img src="./Pictures/sentiment.png" style="margin: 20px; height: 500px"><br>
<br>
r/cosmere sentiment score skews left, with and average of 0.27 sentiment score and 60% of posts having positive sentiments. Whereas, 50% of r/discworld have positive sentiments with a lower average sentiment score of 0.22.

--------------
### <u><b>Model tuning</b></u> 

Accuracy score
| Model               | default| optimized|
| :------------------ | :----: | :------: |
| Dummy Regressor.    | 49.9%  | -        |
| Naive Bayes         | 87.6%  | 94.6%    |
| Random Forest       | 93.8%  | 94.6%.   |
| SVM                 | 89.6%  | 95.2%    |

The baseline model uses a dummy regressor predicting is_discword=1 all the time, and thus as an accuracy score the same as the proportion of discworld posts in the y_test sample.

Implementing ML models such as Random Forest Classifier, Naive Bayes Classifier and Support Vector Classifier, immediately improves the accuracy score predicting discworld posting correctly at least 87% of the time. This indicates that there is value-add in improving prediction leveraging on ML models.

Between the 3 models, Random Forest Classifier appear to have the greatest accuracy at 93%. Post optimisation however, SVM classifier had the greatest accurage at 95.2%

SVC is a type of machine learning algorithm that finds the best decision boundary to separate different classes in a dataset. In NLP, SVC is often used for classification tasks such as sentiment analysis or text classification.

When using SVC for NLP, the feature importance of an SVC NLP model refers to how much each word in the text contributes to the classification decision, based on the coefficients of the model. Words with higher coefficients are more important for the classification decision.

However this is only possible in linear kernal. The optimized kernel option was "rbf' therefore was transform by kernel method to another space, which is not related to input space.

--------------
### <u><b>Model Evaluation</b></u> 
<br>  
<br>  
As this project aims to help r/Discworld and r/Cosmere mods to perform the routine task of identifying posts that are more suitable for the other sub than their own, and make that suggestion to the OP for a more suitable platform, accuracy is most important. As a social media platform there are no significant detrimental effect in a false prediction. All 3 optimised models have similar accuracy with SVC performing marginally better, being able to which subreddit should the post below to 95.1% of the time, based on our text and categorical features. 

|               | PREDICTED: NO | PREDICTED: YES|
|---------------|:-------------:|:-------------:|
| ACTUAL: NO    | 285           | 15            |
| ACTUAL: YES   | 14            | 285           |

Sensitivity :TP / (TP + FN) = 285 / (14 + 285) = 95.3 % <br>
False Negative Rate: FN / (TP + FN) = 14 / (14 + 285) = 4.7% <br>
Specificity: TN / (TN + FP) = 285 / (285 + 15) = 95% <br>
False Positive Rate: FP / (TN + FP) = 15 / (285 + 15) = 5% <br>

Since this project aims to help suggest soon after the post is submitted, ex-ante features like `total_score` and `total_award` were not used in the model training as such information only comes after some time has passed. 

The Receiver Operator Characteristic (ROC) curve is an evaluation metric for binary classification problems. It is a probability curve that plots the Specificity against the False Positive Rate at various threshold values and essentially separates the signal from the noise. In other words, it shows the performance of a classification model at all classification thresholds. The Area Under the Curve (AUC) is the measure of the ability of a binary classifier to distinguish between classes and is used as a summary of the ROC curve. 

The model also has high AUC-ROC score of 0.99. which is the probability that the model will assign a larger probability to a random positive example than a random negative. We can interpret this metric as proof that that this model good as distinguishing between classes. The model does well in terms of recall too, with only 14 false negatives (predicted r/cosmere but actually r/discworld posts).

--------------
### <u><b>Further Improvements</b></u> 
<br>  
<br>  
`is_spoiler`: As we have seen earlier in the EDA, 78% of r/Cosmere posts have been tagged as spoilers, where as only 5% of r/discworld posts are tagged as spoilers. It is observed that none of the wrong predictions for r/Cosmere posts are tagged as spoilers whereas most of the wrong predictions for r/disworld were tagged as spoilers. However, we do not recommend to remove `is_spoiler` feature from the model as it had correctly predicted 237 r/discworld posts with spoiler tags vs 11 it had missed out. And it had also correctly predicted 48 r/Cosmere posts without spoiler tags vs 15 it had missed out. Therefore `is_spoiler` features adds more to the model than removes.<br/>  
<br>  
<img src="./Pictures/Wrong_Classification2.png" style="margin: 20px; height: 500px"><br>
<br>    
We have also seen doing EDA, that only 12% of r/Cosmere posts are not Text-only posts, whereas 56% of r/discworld posts are not Text-only posts. The Title of the post: 
> "Handmade Birthday Gift for my Brother".   
 
is generic enough that it could fit into any subs. Though it is obvious from the picture that this is a r/Cosmere post as it dicpict a miniature bookcase with books from Brandon Sanderson. Image detection could be a enhancement for future improvements in the model.
<br>   
<img src="./Pictures/Wrong_Classification.png" style="margin: 20px; height: 300px"><br>
<br>  
<br>This post is posted in r/discworld but wrongly predicted as a r/Cosmere post. A possible reason why it was wrongly classified was that there are more r/Cosmere-related phrases such as : `Sanderson` (repeated 3 times), `Mistborn Trilogy` than r/discworld, and many common words such as: `books`, `read`. 

Reading the posts, it seems to still be appropriate to be posted on r/discworld as OP would like the opinion of those who have read both Discworld and Cosmere series on their views of how the 2 compare and if the Discowrld series are more light-hearted. Though a better forum may be r/fantasy where Redditors can seek the the community's reccommendation of books that fit a certain theme. 

Such examples showcases the predicting limitation of machine learning models, and it may not be possible to get 100% accuracy.