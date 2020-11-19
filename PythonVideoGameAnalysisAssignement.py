#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd


# In[29]:


#Create a list of the names of your closest friends
friends = ["Anusha", "Aubrey", "Sreshta", "Nitya", "Vaishnavi"]


# In[16]:


#Create a dictionary of the names of your family members as keys and their ages as the values. 
family = {"Avni": 42, "Rajesh": 44, "Rudransh": 6, "Amy": 14}


# In[4]:


#Loop through your friends list using a For loop and print each name.
for item in friends:
    print(item)


# In[18]:


#Loop through your family dictionary using a For loop and print the name of the person if they are under 18 years old.
for key, value in family.items():
    if value < 18:
        print(key)


# In[2]:


# Read in the vgsales.csv file and save it into a DataFrame named vgsales
vgsales = pd.read_csv("vgsales.csv")


# In[4]:


#Print the head and the tail of vgsales DataFrame.
print(vgsales.head())
print(vgsales.tail())


# In[10]:


#What is the total sales in NA for all video games?
naTotal = vgsales["NA_Sales"].sum()
print(naTotal)


# In[12]:


#What is the total for all sales in each region?
allTotal = vgsales["NA_Sales"].sum() + vgsales["EU_Sales"].sum() + vgsales["JP_Sales"].sum() + vgsales["Other_Sales"].sum()
print(allTotal)


# In[20]:


#What is the total sales for Mario Kart Wii?
salescols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]
vgindex = vgsales.Name[vgsales.Name == "Mario Kart Wii"].index[0]
vgtotal = vgsales[salescols].iloc[vgindex].sum(axis = 0)
print(f"The total sales for Mario Kart Wii is {vgtotal}")


# In[28]:


#What is the total of all sales for all games (all regions)? 
vgsales["Total"] = vgsales["NA_Sales"] + vgsales["EU_Sales"] + vgsales["JP_Sales"] + vgsales["Other_Sales"]
print(vgsales.head())


# In[31]:


#What is the mean, median and standard deviation for all sales across all regions? 
vgsales["Mean"] = vgsales[salescols].mean(axis = 1)
vgsales["Median"] = vgsales[salescols].median(axis=1)
vgsales["StDev"] = vgsales[salescols].std(axis=1)
print(vgsales.head())


# In[32]:


#What publisher had the most video games on the list?
print(vgsales["Publisher"].value_counts())


# In[33]:


#Which publisher had the most sales? 
bypub = vgsales.groupby("Publisher").Total.sum()
bypub.sort_values(ascending = False, inplace = True)
print(bypub)


# In[ ]:




