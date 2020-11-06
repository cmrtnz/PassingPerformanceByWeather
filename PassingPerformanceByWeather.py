#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
from sklearn import preprocessing
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[39]:


#Use Pandas to read data into passing df
passing = pd.read_csv('passing.csv')
passing.info()


# In[40]:


#Ability to change the stat analyzed, by default set to yards
stat = 'Yds'
passing = passing[[stat,'Team', 'Wk']]
passing = passing[passing[stat] > 50]
passing.info()
#Standardize the stat as to try to eliminate outside factors such as quarterback quality
passing['Standardized_Stat'] = preprocessing.scale(passing[stat])


# In[41]:


#Get aggregate stats for each week of the season
means = (passing.groupby('Wk').mean())
print(means)


# In[42]:


#Split the data into 4 quadrants of the season
first_quarter = passing[passing['Wk'] < 105]
second_quarter = passing[(passing['Wk'] > 105) & (passing['Wk'] < 109)]
third_quarter = passing[(passing['Wk'] > 109) & (passing['Wk'] < 113)]
fourth_quarter = passing[(passing['Wk'] > 113) & (passing['Wk'] < 117)]


# In[43]:


print(first_quarter[stat].mean())
print(second_quarter[stat].mean())
print(third_quarter[stat].mean())
print(fourth_quarter[stat].mean())
#The start of the 4th quarter of the season typically marks the beginning of December, which is where heavy dropoff is expected


# In[45]:


#Initialize a subset of the df of the 8 teams that play indoors (presumably unaffected by weather)
indoor_stadiums = passing[(passing['Team'] == 'HOU') | (passing['Team'] == 'DAL') |
                                 (passing['Team'] == 'IND') | (passing['Team'] == 'ARZ') |
                                 (passing['Team'] == 'DET') | (passing['Team'] == 'ATL') |
                                 (passing['Team'] == 'NO') | (passing['Team'] == 'MIN')]


# In[46]:


indoor_stadiums[stat][indoor_stadiums['Wk'] > 113].mean()


# In[47]:


#Initialize a subet of the df of 8 teams that play outside and experience the worst/near the worst weather (should be heavily affected)
worst_weather = passing[(passing['Team'] == 'BUF') | (passing['Team'] == 'GB') |
                                 (passing['Team'] == 'CLE') | (passing['Team'] == 'PIT') |
                                 (passing['Team'] == 'CHI') | (passing['Team'] == 'NE') |
                                 (passing['Team'] == 'KC') | (passing['Team'] == 'SEA')]


# In[48]:


worst_weather[stat][worst_weather['Wk'] > 113].mean()


# In[49]:


indoor_stadiums.groupby(['Wk']).mean()['Standardized_Stat'].plot()
worst_weather.groupby(['Wk']).mean()['Standardized_Stat'].plot()


# In[ ]:





# In[ ]:




