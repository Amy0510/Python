#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

#classifiers
from sklearn.cluster import KMeans
from sklearn import metrics

#feature selection
from sklearn.feature_selection import SelectKBest, chi2

#encoders and model eval
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
import matplotlib.pyplot as plt


# In[2]:


crimes = pd.read_csv("ChicagoCrimes4500Bal.csv")


# In[3]:


print(crimes.head())
print(len(crimes))


# In[4]:


#data cleaning
crimes = crimes.dropna() #drops empty values
len(crimes)


# In[5]:


#determine class balance
crimes['Domestic'].value_counts()


# In[8]:


#find out which feature has few rows and remove them
print(crimes['Location Description'].value_counts())
print(crimes['Primary Type'].value_counts())
print(crimes['FBI Code'].value_counts())


# In[9]:


#get rid of the ones below 5

ld_vcts = crimes['Location Description'].value_counts()
to_remove = ld_vcts[ld_vcts<5].index
crimes = crimes[~crimes['Location Description'].isin(to_remove)]
print(len(crimes)) #got rid of 80 rows


# In[10]:


#get rid of the ones below 5

pt_vcts = crimes['Primary Type'].value_counts()
to_remove = pt_vcts[pt_vcts<5].index
crimes = crimes[~crimes['Primary Type'].isin(to_remove)]
print(len(crimes)) #got rid of 9 rows


# In[13]:


#get rid of the ones below 5

fc_vcts = crimes['FBI Code'].value_counts()
to_remove = fc_vcts[fc_vcts<5].index
crimes = crimes[~crimes['FBI Code'].isin(to_remove)]
print(len(crimes)) #got rid of 1 row


# In[14]:


#split the data because we will use hte faux mallow metric
X = crimes
Y = crimes.Domestic 
print(X.head())


# In[18]:


#encode the data
oe = OrdinalEncoder()  
oe.fit(X)
X_enc = oe.transform(X) 

le = LabelEncoder()
le.fit(Y)
Y_enc = le.transform(Y)


# In[43]:


#Feature Selection

selector = SelectKBest(chi2, k=2)
newX = selector.fit_transform(X_enc, Y_enc)


# In[44]:


cols = selector.get_support(indices = True) 
print(cols)
print(X.iloc[:, cols])


# ## Determine the Number of CLusters unsing hte elbow method

# In[45]:


error = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i).fit(newX)
    error.append(kmeans.inertia_)
    
plt.plot(range(1,11), error)
plt.title('Elbow Method')
plt.xlabel('Number of CLuster')
plt.ylabel('Variance')
plt.show() #elbow is at the number 2, so we need 2 clusters


# In[48]:


#put everything into 2 clusters
kmeans2 = KMeans(n_clusters = 2)
y_kmeans2 = kmeans2.fit_predict(newX)
print(y_kmeans2)


# In[49]:


kmeans2.cluster_centers_


# ## Model Evaluation - Fowlkes Mallows Score then Silhouette Score
# 

# In[50]:


print(metrics.fowlkes_mallows_score(Y_enc, y_kmeans2)) #acuracy is not good


# In[52]:


labels = kmeans2.labels_
print(labels)
print(metrics.silhouette_score(newX, labels, metric = 'euclidean')) ##quality of clusters is good


# In[54]:


plt.scatter(newX[:,0], newX[:,1], c=y_kmeans2, cmap='rainbow') #you can see that they are not that close together


# In[ ]:




