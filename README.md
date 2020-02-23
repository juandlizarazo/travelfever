# Travel Fever
Analysis of trends in travel to the US and disease outbreaks in the world

We used data  from four sources:
* Using `Beautiful Soup` we scraped data from the WHO website that include news about disease outbreaks. (/data/whodf-dos.pkl)
* From the Bureu of Transportation Statistics we got data for flight information for incoming and outgoing air-travel from the US [OST_R | BTS | Transtats](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=).

. description of your methods (feel free to describe anything you tried but abandoned)
. output, conclusion, result in whatever form
. explanation of model limitations, assumptions

[![Visualization of incoming air-travel into the USA](https://img.youtube.com/vi/6OUvG_YInZs/0.jpg)](https://www.youtube.com/watch?v=6OUvG_YInZs&feature=youtu.be)


https://github.com/juandlizarazo/travelfever/blob/master/figs/Travel%20to%20the%20US%20-%20Total.png

![Travel to the US based on data from the National Travel and Tourism Office](https://github.com/juandlizarazo/travelfever/blob/master/figs/Travel%20to%20the%20US%20-%20Total.png)
![Correlation between air-travel passengers and disease outbreak reports submitted to WHO]

(https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20histogram%20of%20r%20with%20no%20zeros.png)
![Total Incoming Air-Travel Passengers into the US](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20Total%20travel%20into%20the%20US.png)
![Correlation plot for air-travel from China](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20Correlation%20China%20into%20the%20US.png?raw=true)
![Total Incoming Air-Travel Passengers into the US per country](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20Travel%20into%20the%20US%20per%20country%20of%20origin.png)

## Introduction to `src/main.py`
1) Parsing two excel files `COR Quick Release.xlsx`, `Final COR Port of Entry.xlsx` provided by Fidelity (from NTTO).

2) Predicting correlation between death toll in the country/area the had severe (more than 100 death tolls a year) epidemic outbreaks and the number of international entries to US.
*Data file*: `sick_people_number.xlsx`, `monthly_arrivals.xlsx`;

*Machine learning algorithm*: Gaussian Process Regression;

*Data resources*: https://www.worldometers.info/world-population/ and NTTO.

![Death toll in epidemic outbreak country/area versus Number of international entries to US](https://github.com/juandlizarazo/travelfever/blob/master/figs/death_entry_prediction.png)


