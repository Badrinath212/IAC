#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("iacdata.csv")
data.drop_duplicates(subset="Email ID",keep=False,inplace=True)
plt.boxplot(data["Quantity"])
fig = plt.figure(figsize =(10, 7))
plt.show()


# In[ ]:




