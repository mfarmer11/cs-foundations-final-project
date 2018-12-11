
# coding: utf-8

# In[ ]:


#Add a new collumn to see the amount in Gini Coefficent from 2004-2013
gini1["Change"] = ((gini1["2013"] - gini1["2004"]))


# In[ ]:


#Change index to country name in order to easily graph
gini2.set_index('Country Name', inplace=True)


# In[ ]:


gini2 = gini2.sort_values(by='2004', ascending=False)
pd.Series(gini2['2004']).plot(kind='barh',
                                                    title= "GINI Index :2004")


# In[ ]:


#Bar graph comparing the change in GINI Coefficent across the 11 countries
gini2 = gini2.sort_values(by='Change', ascending=False)
pd.Series(gini2['Change']).plot(kind='barh',
                                                    title= "GINI Index Change:2004-2013")


# In[ ]:


#Remove change column to prepare for a time series graph
del gini2["Change"]


# In[ ]:


#Transpose df to move years to x axis
gini2 = gini2.T


# In[ ]:


#create new collunn for years
gini2["Year"] = [2004,2007,2010,2013]


# In[ ]:


#set year column as index
gini2.set_index('Year', inplace=True)


# In[ ]:


gini2


# In[ ]:


#Create a time series graph showing the chabge in GINI index for all the countries across the time frame

ax = gini2.plot(figsize=(20,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20)
plt.ylabel("GINI Index(x100)", fontsize=20)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
          ncol=3, fancybox=True, shadow=True)

