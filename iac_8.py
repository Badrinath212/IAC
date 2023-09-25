#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data=pd.read_csv("iacdata.csv")
data.drop_duplicates(subset="Email ID",keep=False,inplace=True)
data_new=pd.DataFrame(data)
data_new=data.groupby("City")
avg_city_cgpa=data_new["CGPA"].mean().sort_values(ascending=False)
print(avg_city_cgpa.round(2))

