import pandas as pd
zy = pd.read_csv("zzrainfall.csv")  

import matplotlib.pyplot as plt

import numpy as np
from sklearn.linear_model import LinearRegression

xuanr = input("Select month (-mm-): ")    # ridate
xuanz = input("Select state (full): ")   # zhoustate 

jin = zy.loc[[xuanr in c for c in list(zy['date'])] & (zy["state"] == xuanz)]   # ru
jin.to_csv("ztemp.csv")

tp = pd.read_csv("ztemp.csv")
yue = tp["date"][0]   # [] 0 no ?
#print(yue)
yue = int(yue[5:7]) * 100

for i in range(len(tp["date"])):                           # Pre-processing: filter out the "-"s and convert to int
    if "-" in tp["date"][i]:
        tp["date"][i] = int(tp["date"][i].replace("-", ""))
        #print("eee")

print(tp["date"])

x = np.array(tp["date"]).reshape((-1, 1))
y = np.array(tp["rainfall"])

modo = LinearRegression().fit(x, y)

wei = [20230001 + yue, 20250001 + yue, 20280001 + yue]    #wlai future predic
wei = np.array(wei).reshape(-1, 1)

y_pred = modo.predict(wei)
print(y_pred)