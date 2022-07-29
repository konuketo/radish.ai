import pandas as pd
mg = pd.read_csv("MiguC.csv")  # mg : america

import matplotlib.pyplot as plt

mg.info()
print(mg.head())
#print(st.tail())
#print(mg.Country.unique())

xuanz = input("Select city: ")   #zhoustate cty

zhou = mg.loc[mg["City"] == xuanz]           #city

print(zhou.tail())
plt.plot(zhou['dt'], zhou['AverageTemperature'], "o")
plt.xticks(rotation=45)
plt.show()