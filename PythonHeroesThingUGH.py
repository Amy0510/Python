#!/usr/bin/env python
# coding: utf-8

# ## Pandas Walkthrough

# In[1]:


import pandas as pd


# Steve : 738
# Bruce : 283
# Tony : 193
# Wayde : 322

# In[3]:


#Pandas Series
sales = pd.Series([738, 283, 193, 322], index = ["Steve", "Bruce", "Tony", "Wayde"])
print(sales)


# In[4]:


print(sales["Steve"])


# In[5]:


print(sales["Wayde"])


# In[6]:


sales["Thor"] = 777
print(sales)


# ## Data Frame
# 
# 

# In[7]:


heroes = pd.DataFrame("_", index = ["Steve", "Bruce", "Wayde"], columns =["Last Name", "Age", "Alias"])
print(heroes)


# In[8]:


heroes.at["Steve", "Last Name"] = "Rogers"
print(heroes)


# In[9]:


heroes.at["Bruce", "Last Name"] = "Banner"
heroes.at["Wayde", "Last Name"] = "Wilson"


# In[10]:


print(heroes)


# In[20]:


print(heroes)


# In[40]:


heroes = heroes.drop(index = "Alias")
print(heroes)


# In[38]:


#heroes = heroes.drop(heroes.index[3])
print(heroes)


# In[47]:


listofthings = list(heroes.index)
print(listofthings)


# In[ ]:




