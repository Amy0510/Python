#!/usr/bin/env python
# coding: utf-8

# ## reading CSV with pandas
# 

# In[1]:


import pandas as pd


# In[2]:


stperf = pd.read_csv("StudentsPerformance.csv")


# In[3]:


print(stperf)


# In[7]:


print(stperf.head(3))


# In[8]:


print(stperf.tail(7))


# In[12]:


#Which section had the highest scores

scorecols = ["math score", "reading score", "writing score"]
allTotals = stperf[scorecols].sum()
print(allTotals)


# In[14]:


#what is the total score for james smith

stindex = stperf.name[stperf.name == "James Smith"].index[0]
sttotal = stperf[scorecols].iloc[stindex].sum(axis = 0)
print(f"Total for james smith is {sttotal}")


# In[34]:


#what is the total scores for each collection of section scores

stperf["ScoresTotal"] = stperf["math score"] + stperf["reading score"]+ stperf["writing score"]
print(stperf.head())


# In[20]:


#what are the mean, medians, and standerd deviation of al the student's scores

stperf["Mean"] = stperf[scorecols].mean(axis = 1)
stperf["Median"] = stperf[scorecols].median(axis = 1)
stperf["Standerd Deviation"] = stperf[scorecols].std(axis = 1)
print(stperf)


# In[22]:


# what is the mean, median and standerd deviation of the sections
mean = stperf[scorecols].mean()
median = stperf[scorecols].median()
std = stperf[scorecols].std()
print(mean)
print(median)
print(std)


# In[29]:


#Lets turn these into dataframe along wth the sum

scoreStats = pd.concat([mean, median, std, allTotals], axis = 1 )
scoreStats.columns = ["Mean", "Median", "Standerd Deviation", "Sum"]
print(scoreStats)


# In[30]:


#What were the counts of the different parental education levels
print(stperf["parent education"].value_counts())


# In[42]:


#Who performed best based of their parent's background
byPed = stperf.groupby("parent education").ScoresTotal.mean()
byPed.sort_values(ascending = False, inplace = True)
print(byPed)


# In[ ]:




