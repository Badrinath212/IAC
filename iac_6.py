#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("iacdata.csv")
data.drop_duplicates(subset="Email ID",keep=False,inplace=True)
data=data[["College Name","CGPA"]]
data=data.groupby("College Name")
avg=data["CGPA"].mean()
re=avg.sort_values(ascending=False).round(2)
re.head()


# In[ ]:




