### Problem Statement
<b>To recommend to kite enthusiasts, a suitable location and ideal months for kite flying based on historical weather data</b><br>

Station Code  | Station Name         | Missing files                                   |
------------- | ---------------------| ------------------------------------------------|
S50           | Clementi             | -                                               |
S60           | Sentosa Island       | 2016-12                                         |    
S106          | Pulau Ubin           | 2013-11 2013-12 2014-01 2014-02                 |
S108          | Marina Barrage       | -                                               |
S111          | Newton               | 2016-09 2016-10 2016-11                         |                        
S115          | Tuas South           | -                                               |
<br>

There are 16 active [weather stations](./data/Station_Records.pdf) collecting both rain and wind data in Singapore. The other weather stations are either not active or do not collect full data. Out of the 16, 4 locations - Clementi (S50), Newton (S111), Sentosa Island (S60), and Tuas South (S115) have no restrictions for kite flying (permitable fly zones are outside the red boundaries in map below) are are accessible to the public. A further 2 - Marina Barage (S108) and Pulau Ubin (S106), have restrictions of flying not higher than 200 feet above mean sea level (as indicated by shaded blue boundaries in map below).<br>

This analysis will analysis historical weather data at these 6 locations and recommend the most suitable locations for kite flying.

<img src="./picture/area-limits-map-version-24bfa8924455e4ad8b6e06eae70f46f52.jpeg" style="float: center; margin: 20px; height: 200px, width: 200px"><br>
[source: CAAS](https://www.caas.gov.sg/public-passengers/aerial-activities/flying-kites)<br>

---

### Datasets

#### Provided Data

There are 2 datasets included in the [`data`](./data/) folder for this project. These correponds to rainfall information. 

* [`rainfall-monthly-number-of-rain-days.csv`](./data/rainfall-monthly-number-of-rain-days.csv): Monthly number of rain days from 1982 to 2022. A day is considered to have “rained” if the total rainfall for that day is 0.2mm or more.
* [`rainfall-monthly-total.csv`](./data/rainfall-monthly-total.csv): Monthly total rain recorded in mm(millimeters) from 1982 to 2022

#### Additional Data
We have added 778 monthly data files from 2012-2022 from the 6 weather stations in the [`data`](./data/) folder for this project. These correponds to rainfall, temperature and wind speed information at each weather station. These have been downloaded from [weather.gov.sg](http://www.weather.gov.sg), via an [automated script](#automated-script)

---

### Deliverables

#### <u>By Stations</u>

<img src="./picture/Mthly_rainfall.jpg" style="float: center; margin: 20px; height: 200px, width: 200px">

Monthly rainfall across the 6 weather stations are approximately similarly normally distributed 

<img src="./picture/Mthly_temp.jpg" style="float: center; margin: 20px; height: 200px, width: 200px">

Monthly mean temperature across the 6 weather stations are approximately similarly normally distributed, but with different mean temperture. 

Pulau Ubin have the lowest mean temperature at 27.4 °c, Clementi and Newton the next, at a mean temperature of 27.6 °c, and Marina Barrage is the hottest at 28.5 °c.

<img src="./picture/Mthly_wind_sp.jpg" style="float: center; margin: 20px; height: 200px, width: 200px">

Distribution of monthly mean wind speed across the 6 weather stations are more varied compared to the other weather features. Marina Barrage having the widest range of recorded wind speed and would thus provide inconsistent wind environment for kite flying, and Sentosa Island have the narrowest range. 

While Marina Barrage and Newton both have the same mean wind speed at 7.3 km/hr, Newton has the higher median wind speed at 6.9km/hr vs 6.1km/hr at Marina Barrage.

#### <u>By Months</u>
<img src="./picture/Rainfall_bymth.jpg" style="float: center; margin: 20px; height: 200px, width: 200px">

Rainfall is low in Jan and lowest in Feb. It rises til May, dips til Aug and then rises again with the highest in Dec.

<img src="./picture/Temp_bymth.jpg" style="float: center; margin: 20px; height: 200px, width: 200px">

Average temperature is the lowest in Jan and Feb. It then hovers above 28 °c from Mar to Oct, before cooling again in Nov and Dec

<img src="./picture/Windsp_bymth.jpg" style="float: center; margin: 20px; height: 200px, width: 200px">

Wind speed is varied within each month with more outliers than other weather features. Wind speed is generally highest in Jan and Feb. It then dips til Apr, rises til Aug, and dips again til Nov.


---

### Conclusion
Marina Barage has always been a top choice for kite enthusiasts to fly kites. Surprisingly, it is not the windiest location and experiences varied wind conditions as compared to other locations. It is also hotter as compared to the other locations and is limited by fly height restrictions. 

As there are no significant differences in rainfall between locations, we focus on wind speed and temperature to identify a more suitable location. Newton is as windy as Marina Barrage but with more consistent wind condition. It is also one of the more cooler location. The nearest park with wide open space to Newton weather station is at the Botanic Gardens. 

Rain, wind and temperature weather conditions are most favourable at the being of the year at Jan/Feb. 

----


### automated script
````
#import modules
import webbrowser

#download files
stations=['50','60','106','108','111','115']
for station in stations:
    for year in range(2012,2022+1):
        for month in range(1,12+1):
            ym_str=str(year)+str(month).rjust(2, "0")
            url="http://www.weather.gov.sg/files/dailydata/DAILYDATA_S"+station+"_"+ym_str+".csv"
            try:
                webbrowser.open(url)
            except:
                pass
````