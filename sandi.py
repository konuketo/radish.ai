import pandas as pd
mc = pd.read_csv("MiguC.csv")  # mc : major cities

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

xuanr = input("Select date (yyyy-mm-01): ")    #ridate

ri = mc.loc[mc["dt"] == xuanr]

fig = plt.figure()
ax = plt.axes(projection = "3d")

ax.scatter3D(ri["Latitude"], ri["Longitude"], ri["AverageTemperature"], c = ri["AverageTemperature"], cmap = "Greens")
plt.title("3D Visual of Average Temp over Coordinates on " + xuanr)

plt.show()
"""
for i in mc:
    if 
        plt.plot(mc['Latitude'], mc['AverageTemperature'], "o")
plt.xticks(rotation=90)
plt.show()
"""