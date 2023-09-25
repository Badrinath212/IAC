#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
data=pd.read_csv("iacdata.csv")
data.drop_duplicates(subset="Email ID",keep=False,inplace=True)
data=pd.DataFrame(data)
avg_cgpa=data["CGPA"].mean().round(2)
print(f"Average GPA of the students is {avg_cgpa} ")


# In[ ]:




