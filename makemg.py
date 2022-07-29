import pandas as pd
st = pd.read_csv("GlobalLandTemperaturesByState.csv")  # st : state

import matplotlib.pyplot as plt

st.info()
print(st.head())
#print(st.tail())
print(st.Country.unique())

uofsa = st.loc[st["Country"] == "United States"]
print(len(uofsa.State.unique()))

uofsa.to_csv("AMercaStates.csv")