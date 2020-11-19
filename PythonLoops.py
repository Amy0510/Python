#!/usr/bin/env python
# coding: utf-8

# In[1]:


for num in range(10,50):
    print(num, end=' ')


# In[4]:


num = 10
while num<51:
    print(num, end=' ')
    num +=1


# In[7]:


prog = "python"
for thing in prog:
    print(thing)


# In[8]:


for letter in range(len(prog)):
    print(prog[letter])


# In[9]:


for num in range(11):
    if num<=5 and num>=0:
        print(f"{num} is in the lower half")
    elif num<=9 and num>5:
        print(f"{num} is in the upper half")
    else:
        print("number is 10" )


# In[ ]:




