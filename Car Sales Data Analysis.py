#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


df['Cars Sold'].mean()


# In[6]:


df['Cars Sold'].max()


# In[7]:


df['Cars Sold'].min()


# In[8]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[9]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[10]:


df['Years Experience'].mean()


# In[12]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[13]:


pd.pivot_table(df, values=['Cars Sold'], index=["SalesTraining"])


# In[16]:


df['Hours Worked'].mean()


# In[24]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)

plt.scatter(df['Hours Worked'], df['Cars Sold'])


# In[32]:


df.boxplot(by = 'Hours Worked', column = 'Cars Sold')


# In[33]:


df.boxplot(by = 'Cars Sold', column = 'Hours Worked')


# In[34]:


df.boxplot(by = 'Gender', column = 'Cars Sold')


# In[ ]:





# In[ ]:





# In[ ]:




