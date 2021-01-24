#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        l.append(i)
print(l)


# In[2]:


def fact(x):
    if x==0 or x==1:
        return 1
    return x*fact(x-1)


# In[6]:


n = int(input("give a number : "))
dic = {}
for i in range(n+1):
    dic[i]=i*i
print(dic)


# In[16]:


ch = input("Give a string : ")
index = -1
while(index>=len(ch) or index<0):
    index = int(input("Give an index to remove character"))
ch = ch[:index]+ch[index+1:]
print(ch)


# In[12]:


import numpy as np
l = np.array([[1, 2], [3, 4], [5, 6]])
l=l.tolist()
print(l)


# In[14]:


import numpy as np
l = np.array([0, 1, 2])
l1 = np.array([2, 1, 0])
print(np.cov([l, l1]))


# In[25]:


import math
c, h, l = 50, 30, []
n = int(input("how much values to compute? "))
for i in range(n):
    l.append(float(input("Give a number : ")))
l1 = list(map(lambda x : round(math.sqrt((2*c*x)/h)), l))
print(l1)


# In[ ]:




