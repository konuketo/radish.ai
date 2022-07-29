import pandas as pd
uscp = pd.read_csv("AMercaCity.csv")  # usc : us city

import matplotlib.pyplot as plt

for i in range(len(uscp["Latitude"])):                           # Pre-processing: filter out the "N"/"S"
    if "S" in uscp["Latitude"][i]:
        uscp["Latitude"][i] = uscp["Latitude"][i].replace("S", "")
        #print("eee")
    elif "N" in uscp['Latitude'][i]:
        uscp["Latitude"][i] = uscp["Latitude"][i].replace("N", "")
        #print("yuh")

for i in range(len(uscp["Latitude"])):                           # Pre-processing: convert string numbers into float
    uscp["Latitude"][i] = float(uscp["Latitude"][i])


############################################################
############################################################


for i in range(len(uscp["Longitude"])):                           # Pre-processing: filter out the "E"/"W"
    if "E" in uscp["Longitude"][i]:
        uscp["Longitude"][i] = uscp["Longitude"][i].replace("E", "")
        #print("eee")
    elif "W" in uscp["Longitude"][i]:
        uscp["Longitude"][i] = uscp["Longitude"][i].replace("W", "")
        #print("yuh")

for i in range(len(uscp["Longitude"])):                           # Pre-processing: convert string numbers into float
    uscp["Longitude"][i] = float(uscp["Longitude"][i])

print(uscp.head())
print(uscp.tail())

uscp.to_csv("MiguC.csv")