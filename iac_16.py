#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("iacdata.csv")
data.drop_duplicates(subset="Email ID",keep=False,inplace=True)
data=data[["First Name","Events"]]
data=data.groupby("Events")
data=pd.DataFrame(data,columns=["Event Name","Students"])
count=[]
for i in data["Students"]:
    count.append(len(i))
data["Number of students"]=count

l=[]
for i in range(11):
    a={data["Event Name"].values[i]:data["Number of students"].values[i]}
    l.append(a)
l_ds_courses=['Artificial Intelligence','Data Visualization using Power BI','Hello ML and DL','IS DATA SCIENCE FOR YOU?','RPA: A Boon or A Bane']
std_count=0
for i in l:
    for j in i.items():
        if j[0] in l_ds_courses:
            std_count+=j[1]
        else:
            pass
print(f"The total Number of Students who attended Data Science is {std_count}.")


# In[ ]:




