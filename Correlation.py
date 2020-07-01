#!/usr/bin/env python
# coding: utf-8

# In[30]:


#Script dipicts way to check out correlation between variables
import pandas as pd


# In[31]:


data_df=pd.read_csv('F:\Data\House_Price.csv')
data_df.head()


# In[32]:


data_df.shape 


# In[33]:


import matplotlib.pyplot as plt 
import seaborn as sns 
corrmat = data_df.corr() 

f, ax = plt.subplots(figsize =(9, 8)) 
sns.heatmap(corrmat, ax = ax, cmap ="YlGnBu", linewidths = 0.1) 


# In[34]:


# saleprice correlation matrix 
# k : number of variables for heatmap 
import numpy as np 

k = 15
corrmat = data_df.corr() 

cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index 
print(cols)
cm = np.corrcoef(data_df[cols].values.T) 
f, ax = plt.subplots(figsize =(12, 10)) 

sns.heatmap(cm, ax = ax, cmap ="YlGnBu", 
			linewidths = 0.1, yticklabels = cols.values, 
							xticklabels = cols.values) 


# In[ ]:




