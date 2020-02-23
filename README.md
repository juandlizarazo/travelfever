# Travel Fever: An Analysis of Trends in Travel to the US and Disease Outbreaks in the World

We used data  from four sources:
* Using `Beautiful Soup` we scraped data from the WHO website that include news about disease outbreaks. (/data/whodf-dos.pkl)
* From the Bureau of Transportation Statistics we got data for flight information for incoming and outgoing air-travel from the US [OST_R | BTS | Transtats](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=).
* https://www.worldometers.info/world-population/
* The National Travel and Tourism Office. 

# Methods

* To quantify the current status of disease outbreaks in countries we used the aggregated amount of reports filed by countries to WHO. We then correlated this signal against the aggregated amount of air-travel passengers coming in the same month to the US. Interestingly a small negative correlation was found for most countries, as can be seen in the three figures below. Note that in the barchart the datapoints with zero reports were removed, if they're maintained a similar trend is found by for smaller correlation coefficients.

![Correlation plot for air-travel from China](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20Correlation%20China%20into%20the%20US.png?raw=true)

![Correlation coefficients](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20Pearson-r-with-zeros.png)

![Correlation between air-travel passengers and disease outbreak reports submitted to WHO](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20histogram%20of%20r%20with%20no%20zeros.png)

* We also performed a basic descriptive analysis of the data provided by the Tourism office. Bellow is the total amount of incoming travellers as reported by them.

![Travel to the US based on data from the National Travel and Tourism Office](https://github.com/juandlizarazo/travelfever/blob/master/figs/Travel%20to%20the%20US%20-%20Total.png)

. description of your methods (feel free to describe anything you tried but abandoned)
. output, conclusion, result in whatever form
. explanation of model limitations, assumptions

* To visualize the rich data that we found for air-travel we made a video to show the changing pattern of travel into the us. And with a greater resolution than was possible with the data from the Tourism Office we again explored the influx from several countries.

[![Visualization of incoming air-travel into the USA](https://img.youtube.com/vi/6OUvG_YInZs/0.jpg)](https://www.youtube.com/watch?v=6OUvG_YInZs&feature=youtu.be)

* The traces of amount of passengers flowing from China clearly show seasonal variations and also the effect of the SARS epidemic,

![Influx of air-travel from China](https://github.com/juandlizarazo/travelfever/blob/master/figs/travel-from-china.png)

and also a few notable features for total influx into the US:

![Total Incoming Air-Travel Passengers into the US](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20Total%20travel%20into%20the%20US.png)



## Introduction to `src/main.py`
1) Parsing two excel files `COR Quick Release.xlsx`, `Final COR Port of Entry.xlsx` provided by Fidelity (from NTTO).

2) Predicting correlation between death toll in the country/area the had severe (more than 100 death tolls a year) epidemic outbreaks and the number of international entries to US.

*Data file*: `sick_people_number.xlsx`, `monthly_arrivals.xlsx`;

*Machine learning algorithm*: Gaussian Process Regression;

*Data resources*: https://www.worldometers.info/world-population/ and NTTO.

![Death toll in epidemic outbreak country/area versus Number of international entries to US](https://github.com/juandlizarazo/travelfever/blob/master/figs/death_entry_prediction.png)


