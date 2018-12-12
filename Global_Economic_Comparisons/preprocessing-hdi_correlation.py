
# coding: utf-8

# In[ ]:


#Since we know the time frame are for particular years we can go ahead and select those columns
states = states[["Country Name", "Indicator Name", "Indicator Code", "2004", "2005","2006","2007",
        "2008","2009","2010","2011","2012","2013"]]


# In[ ]:


#Select specific economic, social, and health data

states = states[states['Indicator Code'].isin(["NY.GNP.PCAP.KD.ZG", "NY.GNP.PCAP.KD","NY.GNP.MKTP.CD","SH.XPD.CHEX.PC.CD",
                                               'SI.POV.UMIC','IT.NET.USER.ZS','SL.UEM.TOTL.ZS','NE.CON.PRVT.KD.ZG','SP.POP.DPND'])]


# In[ ]:


#Sort data frame by metric so all countries for each metric are next to each other
states = states.sort_values("Indicator Code")


# In[ ]:


states


# In[ ]:


#To better work and vizualze data, will partiion this main DF into smaller ones by metric


# In[ ]:


#GNI per capita growth (annual %)	NY.GNP.PCAP.KD.ZG

gni_pc_g= states.loc[states['Indicator Code'] == 'NY.GNP.PCAP.KD.ZG']


# In[ ]:


gni_pc_g = gni_pc_g.drop(gni_pc_g.ix[:,'Indicator Name':'Indicator Code'].head(0).columns, axis=1)
gni_pc_g.set_index('Country Name', inplace=True)
gni_pc_g = gni_pc_g.T
gni_pc_g.index = pd.to_datetime(gni_pc_g.index)


# In[ ]:


#GNI per capita (constant 2010 US$)
gni_pc_value = states.loc[states['Indicator Code'] == 'NY.GNP.PCAP.KD']


# In[ ]:


gni_pc_value= gni_pc_value.drop(gni_pc_value.ix[:,'Indicator Name':'Indicator Code'].head(0).columns, axis=1)
gni_pc_value.set_index('Country Name', inplace=True)
gni_pc_value = gni_pc_value.T
gni_pc_value.index = pd.to_datetime(gni_pc_value.index)


# In[ ]:


#GNI (current US$)
gni = states.loc[states['Indicator Code'] == 'NY.GNP.MKTP.CD']


# In[ ]:


gni = gni.drop(gni.ix[:,'Indicator Name':'Indicator Code'].head(0).columns, axis=1)
gni.set_index('Country Name', inplace=True)
gni = gni.T
gni.index = pd.to_datetime(gni.index)


# In[ ]:


#Current health expenditure per capita (current US$)

chc = states.loc[states["Indicator Code"] == "SH.XPD.CHEX.PC.CD"]
chc = chc.drop(chc.ix[:,'Indicator Name':'Indicator Code'].head(0).columns, axis=1)
chc.set_index('Country Name', inplace=True)
chc = chc.T
chc.index = pd.to_datetime(chc.index)


# In[ ]:


#Poverty headcount ratio at $5.50 a day (2011 PPP) (% of population)

pv = states.loc[states["Indicator Code"] == "SI.POV.UMIC"]
pv = pv.drop(pv.ix[:,'Indicator Name':'Indicator Code'].head(0).columns, axis=1)
pv.set_index('Country Name', inplace=True)
pv = pv.T
pv.index = pd.to_datetime(pv.index)


# In[ ]:


#Individuals using the Internet (% of population)	IT.NET.USER.ZS

pi = states.loc[states["Indicator Code"] == "IT.NET.USER.ZS"]
pi = pi.drop(pi.ix[:,'Indicator Name':'Indicator Code'].head(0).columns, axis=1)
pi.set_index('Country Name', inplace=True)
pi = pi.T
pi.index = pd.to_datetime(pi.index)


# In[ ]:


#Unemployment, total (% of total labor force) (modeled ILO estimate)

urt = states.loc[states["Indicator Code"] == "SL.UEM.TOTL.ZS"]
urt = urt.drop(urt.ix[:,'Indicator Name':'Indicator Code'].head(0).columns, axis=1)
urt.set_index('Country Name', inplace=True)
urt = urt.T
urt.index = pd.to_datetime(urt.index)


# In[ ]:


#Households and NPISHs Final consumption expenditure (annual % growth)

hsc = states.loc[states["Indicator Code"] == "NE.CON.PRVT.KD.ZG"]
hsc = hsc.drop(hsc.ix[:,'Indicator Name':'Indicator Code'].head(0).columns, axis=1)
hsc.set_index('Country Name', inplace=True)
hsc = hsc.T
hsc.index = pd.to_datetime(hsc.index)


# In[ ]:


#Age dependency ratio (% of working-age population)

adr = states.loc[states["Indicator Code"] == "SP.POP.DPND"]
adr = adr.drop(adr.ix[:,'Indicator Name':'Indicator Code'].head(0).columns, axis=1)
adr.set_index('Country Name', inplace=True)
adr = adr.T
adr.index = pd.to_datetime(adr.index)


# In[ ]:


#create a differnt df for US values only for later analysis
hdi_us = hdi[["Country", '1991','1994','1997','2000','2004','2007','2010','2013']]


# In[ ]:


#Select time frame years
hdi = hdi[["Country",'2004','2007','2010','2013']]


# In[ ]:


#Select countries
hdi = hdi.loc[[6,44,179,178,176,166,138,65,126,46,72]]  


# In[ ]:


#As per earlier analysis, focus only on US years that have GINI index data
#Focusing on only one country there are more metrics that can be added

usa = usa1[["Country Name", "Indicator Name", "Indicator Code",
            '1979','1986','1991','1994','1997','2000','2004','2007','2010','2013','2016']]


# In[ ]:


#Focusing on only one country there are more metrics that can be added
usa = usa[usa['Indicator Code'].isin(["NY.GNP.PCAP.KD.ZG", "NY.GNP.PCAP.KD","NY.GNP.MKTP.CD","SH.XPD.CHEX.PC.CD",
                                     'SI.POV.UMIC','IT.NET.USER.ZS','SL.UEM.TOTL.ZS','NE.CON.PRVT.KD.ZG','SP.POP.DPND',
                                     "NY.GDP.MKTP.KD.ZG","GC.TAX.TOTL.GD.ZS","SI.POV.GINI","SL.IND.EMPL.ZS","GC.TAX.YPKG.ZS",
                                     "SL.UEM.1524.ZS","SI.POV.UMIC","NY.GDP.PCAP.KD.ZG"])]


# In[ ]:


# Only select the United States

us = usa.loc[usa["Country Name"] == "United States"]


# In[ ]:


us = us.sort_values('Indicator Code')


# In[ ]:


us


# In[ ]:


us = us.reset_index(drop=True)


# In[ ]:


us


# In[ ]:


del us["1979"]
del us["1986"]
del us["2016"]
us = us.drop(us.index[9])


# In[ ]:


#unfortunatley there was no individual health or educational data for years with GINI Index data
#Hence, will use the Human Development Index in their place from the United Nations Development Program
#Read in UN data for the United States
us_hdi = hdi_us.iloc[179]
us_hdi


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


us_hdi = pd.DataFrame(list(nhdi.items()), columns=["Column", "values"])


# In[ ]:


us_hdi = us_hdi.T
us_hdi.columns = us_hdi.iloc[0]


# In[ ]:


us_hdi = us_hdi.reset_index(drop=True)
us_hdi.drop([0])


# In[ ]:


frames = [us, us_hdi]


# In[ ]:


usa_final = pd.concat(frames, keys=["Country Name", "Indicator Name", "Indicator Code", "1991","1994","1997","2000","2004","2007","2010","2013"])


# In[ ]:


usa_final = usa_final.reset_index(drop=True)


# In[ ]:


#drop GNI because it is too big to compare with due to scale and get rid of a string row
usa_final = usa_final.drop(usa_final.index[[15,6]])


# In[ ]:


#cant use GNI/capita because of scale 
#nor change in internent users because it is too big  of a differnce compared to other metrics

usa_change = pd.concat([usa_final.loc[:1], usa_final.loc[3:5], usa_final.loc[8:]])


# In[ ]:


usa_change


# In[ ]:


#create a change column to see changes from 1991 to 2013
usa_change["Change"]= ((usa_change["2013"] - usa_change["1991"]))


# In[ ]:


# delete string columns
usa_change
del usa_change["Country Name"]
del usa_change["Indicator Code"]


# In[ ]:


#make metrics the index for graphing
usa_change.set_index('Indicator Name', inplace=True)


# In[ ]:


#prepare data for correlation analysis
del usa_final["Country Name"]
del usa_final["Indicator Code"]
usa_final.set_index('Indicator Name', inplace=True)
usa_final = usa_final.apply(pd.to_numeric)


# In[ ]:


uf = usa_final.T

