import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("IMVA.xlsx")
print(df)

df1 = df[["Periods", " United Kingdom ", " Germany ", " France ", " Italy ", " Netherlands ", " Greece ", " Belgium & Luxembourg "," Switzerland ",	" Austria ", " Scandinavia "]]

Countries = df1['Periods'].str.split(' ', n = 2, expand = True)
print(Countries)

df1 = df1.assign(year=Countries[1])
df1 = df1.assign(month=Countries[2])
df1["year"] = pd.to_numeric(df1["year"])
print(df1)

df3 = df1[(df1["year"] >= 1988) & (df1["year"] <= 1997)]
print(df3)

df4 = df3[[" Germany ", " France ", " Italy ", " Netherlands ", " Greece ", " Belgium & Luxembourg "," Switzerland ",	" Austria ", " Scandinavia "]]
print(df4)
ps = df4.sum().sort_values(ascending=False)
top3countries = ps.head(3)
top3countries.index

import numpy as np
index = np.arange(len(top3countries.index))
plt.figure(figsize=(10, 10))
plt.xlabel('Countries (Others)', fontsize=10)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, top3countries.index, fontsize=7, rotation=60)
plt.title('Top 3 Europe Countries from 1988-1997')
plt.bar(top3countries.index, top3countries.values/1000)
plt.show();

index = np.arange(len(ps.index))
plt.xlabel('Countries (Others)', fontsize=10)
plt.ylabel('No. of Travellers (in thousands)', fontsize=8)
plt.xticks(index, ps.index, fontsize=7, rotation=60)
plt.title('Total Europe Countries from 1988-1997')
plt.bar(ps.index, ps.values/1000)
plt.show();






