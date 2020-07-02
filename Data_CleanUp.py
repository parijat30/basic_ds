#!/usr/bin/env python
# coding: utf-8

# In[20]:


#Script dipicts ways to deal with data clean up process
import pandas as pd
data_df=pd.read_csv('F:\Data\House_Price.csv')
data_df.head()


# In[19]:


#To remove the null or NAN values from data 
df1=data_df
print(df1.shape)
df1=df1.dropna())#By default will drop all the rows having NAN or null values
print(df1.shape)


# In[22]:


#To replace all the null values with 0 
data_df.isnull()
df2=data_df
df2=df2.fillna(0)
print(df2)


# In[ ]:




