
# coding: utf-8

# In[ ]:


# variable names for packages used
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
fileDir = os.path.dirname(os.path.realpath('__file__'))



# In[ ]:


#variable names for inital datasets/read in


# In[ ]:


#Import Gini Index data from the World Bank
gini = pd.read_csv(os.path.join(fileDir, '../data/gini.csv'), header=4)


# In[ ]:


#Read in world bank data for all the selected states
states = pd.read_csv(os.path.join(fileDir,'../data/journal_wb.csv'), header=4)


# In[ ]:


#Create a copy of orignal data to later use to workwith for US analysis
usa1 = states


# In[ ]:


#unfortunatley there was no individual health or educational data for years with GINI Index data
#Hence, will use the Human Development Index in their place from the United Nations Development Program
hdi = pd.read_csv(os.path.join(fileDir,'../data/h_d_i.csv'), encoding='ISO-8859-1', header=1)


# In[ ]:


#variable names used for preprocessing 


# In[ ]:


# Gini data prerocessing
#Select only years for which there is US data availble
gini1 = gini[['Country Name','1979','1986','1991','1994','1997','2000','2004','2007','2010','2013','2016']]


# In[ ]:


#Select 11 countries for analysis, based upon differnt geographic location and GINI Coefficent
gini2 = gini1.loc[[2,6,9,21,24,32,38,39,41,44,50]]   


# In[ ]:


#Variable names used in HDI and correlation preprocessing


# In[ ]:


#GNI per capita growth (annual %)	NY.GNP.PCAP.KD.ZG
gni_pc_g= states.loc[states['Indicator Code'] == 'NY.GNP.PCAP.KD.ZG']


# In[ ]:


#GNI per capita (constant 2010 US$)
gni_pc_value = states.loc[states['Indicator Code'] == 'NY.GNP.PCAP.KD']


# In[ ]:


#Current health expenditure per capita (current US$)
chc = states.loc[states["Indicator Code"] == "SH.XPD.CHEX.PC.CD"]


# In[ ]:


#Poverty headcount ratio at $5.50 a day (2011 PPP) (% of population)
pv = states.loc[states["Indicator Code"] == "SI.POV.UMIC"]


# In[ ]:


#Individuals using the Internet (% of population)	IT.NET.USER.ZS
pi = states.loc[states["Indicator Code"] == "IT.NET.USER.ZS"]


# In[ ]:


#Unemployment, total (% of total labor force) (modeled ILO estimate)
urt = states.loc[states["Indicator Code"] == "SL.UEM.TOTL.ZS"]


# In[ ]:


#Households and NPISHs Final consumption expenditure (annual % growth)
hsc = states.loc[states["Indicator Code"] == "NE.CON.PRVT.KD.ZG"]


# In[ ]:


#create a differnt df for US values only for later analysis
hdi_us = hdi[["Country", '1991','1994','1997','2000','2004','2007','2010','2013']]


# In[ ]:


# Only select the United States
us = states.loc[states["Country Name"] == "United States"]


# In[ ]:


#unfortunatley there was no individual health or educational data for years with GINI Index data
#Hence, will use the Human Development Index in their place from the United Nations Development Program
#Read in UN data for the United States
us_hdi = hdi_us.iloc[179]


# In[ ]:


#reformat hdi data to fit the world bank data set and change HDI values from decimal to percent(x100)
nhdi  = {'Country Name': "United States",
        'Indicator Name': "Human Development Index",
        'Indicator Code': "HDI",
        '1991': 86.1,
        '1994': 87.4,
        '1997': 88.1,
        '2000': 88.4,
        '2004': 89.5,
        '2007': 90.5,
        '2010': 91.0,
        '2013': 91.6}


# In[ ]:


frames = [us, us_hdi]


# In[ ]:


usa_final = pd.concat(frames, keys=["Country Name", "Indicator Name", "Indicator Code", "1991","1994","1997","2000","2004","2007","2010","2013"])


# In[ ]:


usa_change = pd.concat([usa_final.loc[:1], usa_final.loc[3:5], usa_final.loc[8:]])


# In[ ]:


uf = usa_final.T


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

