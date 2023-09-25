#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
S=pd.read_csv("iacdata.csv")
S.drop_duplicates(subset="Email ID",keep=False,inplace=True)
R=S[["CGPA","Expected salary (Lac)"]].mean().round(1)
B=S[["Experience with python (Months)","Expected salary (Lac)"]].mean().round(1)
print(R)
print(B)


# In[ ]:




