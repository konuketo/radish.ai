import pandas as pd
mc = pd.read_csv("MiguC.csv")  # mc : major cities

a = "aaa"
for i in range(len(mc["City"])):
    if mc["City"][i] != a:
        #print(mc["City"][i], mc["Latitude"][i], mc["Longitude"][i])
        #print(mc["City"][i])
        #print(mc["Latitude"][i])
        print(mc["Longitude"][i])
        a = mc["City"][i]


# ayo len investigate shouldn't it be vertically to work hmm