import pandas as pd
usc = pd.read_csv("GlobalLandTemperaturesByCity.csv")  # usc : us city

import matplotlib.pyplot as plt

usc.info()
#print(usc.head())
#print(usc.tail())
#print(usc.Country.unique())

uofsac = usc.loc[usc["Country"] == "United States"]
print(len(uofsac.City.unique()))
print(uofsac.City.unique())
print(uofsac.head())


uofsac.to_csv("AMercaCity.csv")