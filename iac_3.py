#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
data=pd.read_csv("iacdata.csv")
data.drop_duplicates(subset="Email ID",keep=False,inplace=True)
data_new=pd.DataFrame(data)
data_new=data[["First Name","Year of Graduation"]]
data_by_year=data_new.groupby("Year of Graduation")
data=pd.DataFrame(data_by_year,columns=["year","students"])
l=[]
for i in data["students"]:
    l.append(len(i))
data["number_of_students"]=l
data_new=pd.DataFrame({"year":["2023","2024","2025","2026"],"number_of_students":l})
data_new.plot.bar(x="year",ylabel="number_of_students",title="students across different graduation years",color="green")


# In[ ]:




