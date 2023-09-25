#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
S=pd.read_csv("iacdata.csv")
S.drop_duplicates(subset="Email ID",keep=False,inplace=True)
R=S[["CGPA","Leadership- skills"]]
B=R.tail()
B.plot.bar(x='Leadership- skills', ylabel='CGPA', rot=0)
A=S[["Leadership- skills","Expected salary (Lac)"]]
D=A.tail()
D.plot.bar(x='Leadership- skills',ylabel='Expected salary (Lac)', rot=0)


# In[ ]:




