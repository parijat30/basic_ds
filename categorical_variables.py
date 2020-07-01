#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Script has different ways of dealing with categorical variables 
import pandas as pd


# In[18]:


data_df=pd.read_excel('F:\Data\BreastTissue.xls',"Data")


# In[19]:


data_df.head()


# In[20]:


s=(data_df.dtypes=='object')
#object dtype shows column has text


# In[21]:


print (s)


# In[22]:


print(s[s].index)
print(list(s[s].index))


# In[23]:


#Approach 1: Drop the categorical variable 
drop_data_categorical=data_df
drop_data_categorical=drop_data_categorical.drop('Class',axis=1)
#axis 1 is used for columns and axis 0 is used for rows 


# In[24]:


drop_data_categorical.head()


# In[25]:


#Approach 2: Label Encoding (0 1 2 3 4 5 ...) 
from sklearn.preprocessing import LabelEncoder


# In[35]:


# Apply label encoder to each column with categorical data
label_encoder = LabelEncoder()
label_data_set=data_df['Class']
print(label_data_set.head())
label_data_set_encoded = label_encoder.fit_transform(label_data_set)
print(label_data_set_encoded)


# In[37]:


#Approach 3: One Hot Encoding 
from sklearn.preprocessing import OneHotEncoder
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
#handle_unknown='ignore' to avoid errors when the validation data contains classes that aren't
#represented in the training data, and
#sparse=False ensures that the encoded columns are returned as a numpy array
#instead of a sparse matrix
OneHotEncoder_Data_Set=data_df
OneHotEncoded_Data_Set=OH_encoder.fit_transform(OneHotEncoder_Data_Set)
print(OneHotEncoded_Data_Set)


# In[ ]:




