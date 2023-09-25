#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("iacdata.csv")
data.drop_duplicates(subset="Email ID",keep=False,inplace=True)
data=pd.DataFrame(data)
data=data[["First Name","Year of Graduation"]]
data=data.groupby("Year of Graduation")
data=pd.DataFrame(data,columns=["Year of Graduation","students"])
count=[]
for i in data["students"]:
    count.append(len(i))
data["Number of Students"]=count
out=data["Number of Students"].values[0]+data["Number of Students"].values[1]
print(f"{out} students are graduating by the end of 2024.")


# In[ ]:




