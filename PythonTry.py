#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


print("hello")
#this is a comment 
'''
fg
ggg
gggggg
print("hi)")

'''


# ## Python Data Types

# integers: numbers without decimals  
# floats: numbers with decimals  
# Strings: any word . . . denoted with quotes  

# In[5]:


year = 2020
print(year)


# In[6]:


print(year)


# In[7]:


print(f"hello {year}")


# In[8]:


print("hello {year}")


# In[9]:


greeting = "hello world"
print(f"{greeting}, it is {year}")


# In[11]:


month, year = "july", 2020
print(f"{month} in  {year}")


# In[12]:


num1 = 12
num2 = 10

#add
answer = num1+num2
print(answer)
answer = num1-num2
print(answer)

print(num1*num2)


# In[13]:


print(type(answer))


# In[14]:


total = 12*3/72
print(total)


# In[15]:


print(type(total))


# In[16]:


inttotal = int(total)
print(inttotal)


# In[19]:


age =9
if age >= 18:
    print("legal age")
elif age>=13:
    print("teenager")
else:
    print("child")


# In[20]:


for x in range(0,10):
    print(x)


# In[22]:


x = 12
while x>0:
    print(x)
    x = x-1


# In[ ]:




