#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
S=pd.read_csv("iacdata.csv")
S.drop_duplicates(subset="Email ID",keep=False,inplace=True)
R=S[["First Name","How did you come to know about this event?"]]
B=R.groupby("How did you come to know about this event?").size().sort_values()
B.tail(1)


# In[ ]:




