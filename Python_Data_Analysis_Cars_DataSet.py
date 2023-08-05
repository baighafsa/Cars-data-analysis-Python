#!/usr/bin/env python
# coding: utf-8

# # Cars Dataset
# 
# The data of different cars is given with their specifications.

# In[3]:


import pandas as pd
cars=pd.read_csv(r'C:\Users\SPECTRE\Desktop\DataAnalysis_DataSets\Cars.csv.csv')


# In[4]:


cars.head()


# In[5]:


cars.shape


# ### Data Cleaning

# In[6]:


# Find null values if any fill them with mean of that column.


# In[7]:


cars.isnull()


# In[8]:


cars.isnull().sum()


# In[11]:


cars.fillna(cars.mean())


# In[12]:


cars.isnull().sum()


# In[13]:


cars.fillna(cars.mean().iloc[0], inplace=True)


# In[14]:


cars.isnull().sum()


# In[15]:


# Check what are the different types of 'Make' are there in the dataset, and what is the count(occurence of each Make in the data


# In[16]:


data.head(2)


# In[18]:


cars['Make'].value_counts()


# In[19]:


# filtering
#show all the records where Origin is Asia or Europe


# In[21]:


cars[cars['Origin'].isin(['Asia','Europe'])]


# In[22]:


# Removing unwanted columns
# Remove all the records (rows) where Weight is above 4000


# In[24]:


cars.head(2)


# In[26]:


cars[cars['Weight'] > 4000]


# In[27]:


cars[~(cars['Weight'] > 4000)] # (~) to remove


# In[28]:


# Applying function on a column
# increase all the values of 'MPG_City' column by 3


# In[31]:


cars['MPG_City'] = cars['MPG_City'].apply(lambda x:x+3)


# In[30]:


cars


# In[ ]:




