#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("iacdata.csv")
data.drop_duplicates(subset="Email ID",keep=False,inplace=True)
print(f"{len(data)} unique students are included in the dataset.")


# In[ ]:




