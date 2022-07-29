import pandas as pd
zy = pd.read_csv("zzrainfall.csv")  # yu yv

import matplotlib.pyplot as plt
#zy.info()
#print(zy.head())
#print(zy.tail())
#print(zy.hour.unique())
print(zy.state.unique())