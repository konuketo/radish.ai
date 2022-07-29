import pandas as pd
mc = pd.read_csv("MiguC.csv")  # mc : major cities

import numpy as np
from sklearn.linear_model import LinearRegression

xuanr = input("Select date (-mm-01): ")    # ridate
xuanz = input("Select city: ")   # zhoustate cty

jin = mc.loc[[xuanr in c for c in list(mc['dt'])] & (mc["City"] == xuanz)]   # ru
jin.to_csv("temp.csv")

tp = pd.read_csv("temp.csv")
yue = tp["dt"][0]   # [] 0 no ?
#print(yue)
yue = int(yue[5:7]) * 100

for i in range(len(tp["dt"])):                           # Pre-processing: filter out the "-"s and convert to int
    if "-" in tp["dt"][i]:
        tp["dt"][i] = int(tp["dt"][i].replace("-", ""))
        #print("eee")

print(tp["dt"])

x = np.array(tp["dt"]).reshape((-1, 1))
y = np.array(tp["AverageTemperature"])

modo = LinearRegression().fit(x, y)

wei = [20230001 + yue, 20250001 + yue, 20280001 + yue]    #wlai future predic
wei = np.array(wei).reshape(-1, 1)

y_pred = modo.predict(wei)
print(y_pred)