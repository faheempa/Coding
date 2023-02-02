import pandas as pd
import numpy as np

# 1 - dataframe
data1 = dict(cars=[15, 13, 20,50], bikes=[20, 24, 17,10])
dataf1=pd.DataFrame(data1)
print(dataf1)
print(dataf1.loc[0])
print(dataf1.loc[[0,1]])
print(dataf1.loc[0:2])
dataf2=pd.DataFrame(data1, index=["monday", "tuesday", "wednesday", "thursday"])
print(dataf2)
print(dataf2.loc["monday"])
print(dataf2.loc["tuesday"])
print(dataf2.loc[["monday", "tuesday"]])
print("-"*50)

# 2 - series
a=[20,15,10,5]
s1 = pd.Series(a)
print(s1[0])
print(s1[[0,1]])
print(s1[0:2])
s2 = pd.Series(a, index=["mon", "tue", "wed", "thu"])
print(s2)
print(s2.loc["mon"])
print(s2.loc[["mon", "wed"]])
print("-"*50)

# 3 - csv file
b=pd.read_csv("data.csv")
print(b)
print(b.loc[0])
print(b.loc[[0,4,7]])
print(b.loc[0:5])
print(b.head()) # return first 5 rows
print(b.head(3)) # return first 3 rows
print(b.tail()) # return last 5 rows
print(b.tail(3)) # return last 3 rows
print(b.info())
print("-"*50)

# 4 - dealing with null values
# droping null value rows
c=b.dropna()
print(c)
# filling a perticular column with a value
b["cars"].fillna(200, inplace=True)
print(b)
# filling the null values with 100
b.fillna(100, inplace=True)
print(b)
# simplily replacing a perticular cell
b.loc[1,"cars"]=900 #[index,column_name]
print(b)
print("-"*50)

# 5 - mean, mode, median
print(b["cars"].mean())
print(b["cars"].mode()) # most frequent value
print(b["cars"].median())

# 6 - ploting data as a graph
import matplotlib.pyplot as plt
b.plot()
plt.show()
print("-"*50)

# 7
d1 = dict(cars=[15, 13, 20, 50], bikes=[20, 24, 17, 10], plane=[1,2,3,4])
df1 = pd.DataFrame(d1)
# converting to numpy array
npa1 = df1.to_numpy()
print(npa1)
# displaying a detailed describtion
print(df1.describe())
# sorting values with car column
print(df1.sort_values("cars"))
# accessing a perticular cell
print(df1.at[0,"cars"])
print(df1.loc[0,"cars"])
#slicing
print(df1.loc[0:2,"cars"])
print(df1.loc[0:2,"cars":"bikes"])
# conditional selection
print(df1["cars"])
print(df1[df1["cars"]==20])
print(df1[df1["cars"]!=20])
print(df1[df1["cars"]>=20])
print(df1[df1["cars"]>20])
print(df1[df1["cars"]<20])