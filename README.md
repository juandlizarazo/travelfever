# Travel Fever
Analysis of trends in travel to the US and disease outbreaks in the world

. summary of what data you used,
. description of your methods (feel free to describe anything you tried but abandoned)
. output, conclusion, result in whatever form
. explanation of model limitations, assumptions

![The Ebola Outbreak from 2013](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20Ebola%20Outbreak%20of%202013.png)
![Correlation between air-travel passengers and disease outbreak reports submitted to WHO](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20histogram%20of%20r%20with%20no%20zeros.png)
![Total Incoming Air-Travel Passengers into the US](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20Total%20travel%20into%20the%20US.png)
![Correlation plot for air-travel from China](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20Correlation%20China%20into%20the%20US.png?raw=true)
![Total Incoming Air-Travel Passengers into the US per country](https://github.com/juandlizarazo/travelfever/blob/master/figs/Final%20-%20Travel%20into%20the%20US%20per%20country%20of%20origin.png)

## Introduction to `src/main.py`
1) Parsing two excel files provided by Fidelity (from NTTO).

2) Predicting correlation between death toll in the country/area the had severe (more than 100 death tolls a year) epidemic outbreaks and the number of international entries to US, using Gaussian Process Regression.
![Death toll in epidemic outbreak country/area versus Number of international entries to US](https://github.com/juandlizarazo/travelfever/blob/master/figs/death_entry_prediction.png)


