#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("iacdata.csv")
data.drop_duplicates(subset="Email ID",keep=False,inplace=True)
data=pd.DataFrame(data["Family Income"],columns=["Family Income"])
l=[]
for i in data["Family Income"]:
    if "+" in i:
        l.append(int(i[0]))
    elif "-" in i:
        l.append(int(i[2]))
    else:
        l.append(int(i[0]))
data["Family Income"]=l
out=data["Family Income"].mean().round(2)
print(f"Average family income of the student is {out} Lakhs")     


# In[ ]:




