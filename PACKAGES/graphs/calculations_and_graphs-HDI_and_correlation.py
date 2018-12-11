
# coding: utf-8

# In[ ]:


#GNI per capita growth graph
ax = gni_pc_g.plot(figsize=(20,10), fontsize=13)
plt.legend(loc='best', fontsize=13)
plt.title('GNI per Capita Growth(%): 2004-2013', fontsize=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('(%) Growth', fontsize=13)


# In[ ]:


#GNI/capita graph
ax = gni_pc_value.plot(figsize=(20,10), fontsize=13)
plt.legend(loc='best', fontsize=13)
plt.title('GNI per Capita: 2004-2013', fontsize=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('(constant 2010 US$)', fontsize=13)


# In[ ]:


#GNI graph
ax = gni.plot(figsize=(20,10), fontsize=13)
plt.legend(loc='best', fontsize=13)
plt.title('GNI: 2004-2013', fontsize=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Current  US$ (10 trillion)', fontsize=13)


# In[ ]:


#Health Expenditure/capita graph
ax = chc.plot(figsize=(20,10), fontsize=13)
plt.legend(loc='best', fontsize=13)
plt.title('Health Expendetiture per Captia: 2004-2013', fontsize=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Current US$', fontsize=13)


# In[ ]:


#Poverty head couunt ratio graph
ax = pv.plot(figsize=(20,10), fontsize=13)
plt.legend(loc='best', fontsize=13)
plt.title('Population in Poverty at $5.5 a Day: 2004-2013', fontsize=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('% of Population', fontsize=13)


# In[ ]:


#Number of internet users graph
ax = pi.plot(figsize=(20,10), fontsize=13)
plt.legend(loc='best', fontsize=13)
plt.title('Number of Internet Users: 2004-2013', fontsize=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('% of Population', fontsize=13)


# In[ ]:


#Total Unemployment graph
ax = urt.plot(figsize=(20,10), fontsize=13)
plt.legend(loc='best', fontsize=13)
plt.title('Unemployment Rate: 2004-2013', fontsize=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('% of Total Labor Force', fontsize=13)


# In[ ]:


#Household Consumption graph
ax = hsc.plot(figsize=(20,10), fontsize=13)
plt.legend(loc='best', fontsize=13)
plt.title('Household Consumption Expenditure: 2004-2013', fontsize=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Annual % Growth', fontsize=13)


# In[ ]:


#Age Dependency Ratio graph
ax = adr.plot(figsize=(20,10), fontsize=13)
plt.legend(loc='best', fontsize=13)
plt.title('Age Dependency Ratio: 2004-2013', fontsize=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('% of Working-Age Population', fontsize=13)


# In[ ]:


#Create a change column in HDI
hdi["Change"] = ((hdi["2013"] - hdi["2004"]))


# In[ ]:


#Bar graph comparing HDI across the 11 countries for 2004
hdi.set_index('Country', inplace=True)


# In[ ]:


hdi = hdi.sort_values(by='2004', ascending=False)
pd.Series(hdi['2004']).plot(kind='barh',
                                                    title= "Human Development Index:2004")


# In[ ]:


#Bar graph comparing the change in HDI across the 11 countries
hdi = hdi.sort_values(by='Change', ascending=False)
pd.Series(hdi['Change']).plot(kind='barh',
                                                    title= "Human Development Index Change:2004-2013")


# In[ ]:


del hdi["Change"]


# In[ ]:


hdi = hdi.T
hdi.index = pd.to_datetime(hdi.index)


# In[ ]:


#Time series visualizing the change in HDI

ax = hdi.plot(figsize=(20,10), fontsize=13)
plt.legend(loc='best', fontsize=13)
plt.title('Human Development Index: 2004-2013', fontsize=20)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('HDI', fontsize=13)


# In[ ]:


#make a graph showing the change across tiem frame
usa_change = usa_change.sort_values(by='Change', ascending=False)
pd.Series(usa_change['Change']).plot(kind='barh', 
                                                    title= "Metric Changes for the United States: 1991-2013")


# In[ ]:


#perform a simple correlation analysis between the GINI index of the US and another metric

gini_txr = uf['GINI index (World Bank estimate)'].corr(uf['Tax revenue (% of GDP)'])
gini_txi = uf['GINI index (World Bank estimate)'].corr(uf['Taxes on income, profits and capital gains (% of total taxes)'])
gini_i = uf['GINI index (World Bank estimate)'].corr(uf['Individuals using the Internet (% of population)'])
gini_hc = uf['GINI index (World Bank estimate)'].corr(uf['Households and NPISHs Final consumption expenditure (annual % growth)'])
gini_gdp_rt = uf['GINI index (World Bank estimate)'].corr(uf['GDP growth (annual %)'])
gini_gdp_pc_rt = uf['GINI index (World Bank estimate)'].corr(uf['GDP per capita growth (annual %)'])
gini_gni_pc = uf['GINI index (World Bank estimate)'].corr(uf['GNI per capita (constant 2010 US$)'])
gini_gni_pc_rt = uf['GINI index (World Bank estimate)'].corr(uf['GNI per capita growth (annual %)'])
gini_pr = uf['GINI index (World Bank estimate)'].corr(uf['Poverty headcount ratio at $5.50 a day (2011 PPP) (% of population)'])
gini_ei = uf['GINI index (World Bank estimate)'].corr(uf['Employment in industry (% of total employment) (modeled ILO estimate)'])
gini_yth_urt = uf['GINI index (World Bank estimate)'].corr(uf['Unemployment, youth total (% of total labor force ages 15-24) (modeled ILO estimate)'])
gini_urt = uf['GINI index (World Bank estimate)'].corr(uf['Unemployment, total (% of total labor force) (modeled ILO estimate)'])
gini_adr = uf['GINI index (World Bank estimate)'].corr(uf['Age dependency ratio (% of working-age population)'])
gini_hdi = uf['GINI index (World Bank estimate)'].corr(uf['Human Development Index'])


# In[ ]:


#Store correlation values in a diction for easy access

us_correlation_dict = [{"Tax rev as GDP":gini_txr, "Tax rev on income":gini_txi, "Internet users":gini_i,
                        "Household Consumption":gini_hc, "GDP growth": gini_gdp_rt, "GDP per capita grwoth": gini_gdp_pc_rt,
                       "GNI per capita": gini_gni_pc, "GNI per capita growth": gini_gni_pc_rt,
                        "Poverty at $5.5 a day": gini_pr, "Employment in industry sector": gini_ei,
                        "Youth unemployment rate": gini_yth_urt, "Unemployment rate": gini_urt,
                        "Age dependency ration": gini_adr, "Hunman Development Index": gini_hdi}]


# In[ ]:


#Convert dictionary to a dataframe
us_corr = pd.DataFrame(us_correlation_dict)


# In[ ]:


#transpose data frame
us_corr = us_corr.T


# In[ ]:


#rename column with r values to "Correlation"
us_corr.columns = ["Correlation"]


# In[ ]:


#Graph correlation as bar
us_corr = us_corr.sort_values(by='Correlation', ascending=False)
pd.Series(us_corr['Correlation']).plot(kind='barh', 
                                                    title= "Correlation: U.S GINI vs U.S Economic & Social Metrics")

