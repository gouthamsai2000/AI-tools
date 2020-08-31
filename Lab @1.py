#!/usr/bin/env python
# coding: utf-8

# Matplotlib

# pip install matplotlib

# In[20]:


from matplotlib import pyplot as plt


# In[21]:


import numpy as np


# Types of graphs 

# Linear Graph

# In[4]:


x=np.array([1,2,3])
y=np.array([4,5,6])
plt.plot(x,y,label="line one",color='m')
plt.xlabel("xaxis")
plt.ylabel("yaxis")
plt.legend()
plt.show()


# Histograph
# 

# In[8]:


x=[10,15,20,25,30,35,40,45,50,55,60]
y=[0,10,20,30,40,50,60,70,80,90,100]#increasing order
plt.hist(x,y,histtype="bar",label="hist",rwidth=0.5) #syntax

plt.xlabel("x hist")
plt.ylabel("y hist")

plt.title("histogram")
plt.legend()
plt.show()


# Scatter plot

# In[10]:


x1=np.array([5,8,9])
y1=np.array([12,6,7])
plt.scatter(x1,y1,label="scat",color='r')
plt.xlabel("x scat")
plt.ylabel("y scat")
plt.title("scatter plot")
plt.legend()
plt.show


# Stack plot

# In[11]:


a=np.array([1,2,3,4,5])
b=np.array([2,3,4,3,2])
c=np.array([7,6,5,8,9])
d=np.array([8,7,5,4,10])
plt.plot(a,color='g',label='gren',linewidth=3)
plt.plot(b,color='m',label='pink',linewidth=3)
plt.plot(c,color='b',label='blue',linewidth=3)
plt.plot(d,color='r',label='red',linewidth=3)
plt.stackplot(a,b,c,d,colors=['g','m','b','r'])#syntax
plt.xlabel("x stack")
plt.ylabel("y stack")
plt.title("stack plot")
plt.legend()
plt.show


# Pie chart

# In[23]:


a=([10,3,4,12])
b=(['green','blue','black','red'])
colors=(['g','b','k','r'])
plt.pie(a,labels=b,colors=colors,startangle=90)
plt.title(["pie chart"])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




