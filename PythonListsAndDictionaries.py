#!/usr/bin/env python
# coding: utf-8

# ## Lists

# In[1]:


emptyLIst = []
numList = [1,2,3]
strList = ["alabama", "alaska", "arizona"]
print(len(strList))
print(strList)


# In[2]:


mixList = ["robot", 12, "android", 20.2]
print(mixList)


# In[3]:


print(mixList[0:3])


# In[4]:


print(mixList[-1]) #prints last thing in list


# In[8]:


ans = mixList[1]*mixList[-1]
print(ans)


# In[11]:


for item in mixList:
    print(item, end =', ')


# In[13]:


for item in mixList:
    if type(item) == str:
        print(item)
        


# In[15]:


cities = ["Seattle", "Tacoma", "Spokane"]
print(cities)
cities.append("Olympia")
print(cities)


# In[16]:


#test to see if a value is in the list

if "Olympia" in cities:
      print("it is there")
else:
    print("Olympia not found")


# ## Dictionaires
# gives labels to data  
# color: red  
# brand: Honda  
# Year: 2012  
# 

# In[22]:


car = {"Color": "Red", "Brand": "Honda", "Year": 2012 }
print(car)


# In[23]:


print(car["Color"])


# In[25]:


print(car.keys())
print(car.values())


# In[29]:


# add new element
car["Model"] = "Civic"
print(car)


# In[30]:


for key, value in car.items():
    print(f"{key} : {value}")


# In[ ]:




