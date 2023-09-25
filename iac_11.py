#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from colorama import Fore, Back, Style
data=pd.read_csv("iacdata.csv")
data.drop_duplicates(subset="Email ID",keep=False,inplace=True)
data=pd.DataFrame(data)
data=data[["First Name","Events"]]
data=data.groupby("Events")
data=pd.DataFrame(data,columns=["Event Name","Students"])
count=[]
for i in data["Students"]:
    count.append(len(i))
data["Number of Students attened for the event"]=count
data=pd.DataFrame(data.sort_values(by=["Number of Students attened for the event"],ascending=False))
out = data['Event Name'].values[0]
print(f"The event tend to attract more students from specific field of study is ||{out}||.")

