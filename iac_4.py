#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("iacdata.csv")
data.drop_duplicates(subset="Email ID",keep=False,inplace=True)
data=pd.DataFrame(data)
data=data[["First Name","Experience with python (Months)"]]
data=data.groupby("Experience with python (Months)")
data=pd.DataFrame(data,columns=["Experience with python (Months)","students"])
l=[]
for i in data["students"]:
    l.append(len(i))
data["Number of Students"]=l
data=pd.DataFrame({"Experience with python (Months)":["3","4","5","6","7","8"],"Number of Students":l})
data.plot.barh(x="Experience with python (Months)",ylabel="Number of Students",title="Experience with python programming",color="yellow")


# In[ ]:




