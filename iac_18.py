#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
S=pd.read_csv("iacdata.csv")
S.drop_duplicates(subset="Email ID",keep=False,inplace=True) 
re=S[S['Specify in "Others" (how did you come to know about this event)']=='College']
out=re.groupby(["College Name"]).size().sort_values(ascending=False)
out.head()


# In[ ]:




