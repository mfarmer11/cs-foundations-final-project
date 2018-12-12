def load_worldbank():

	import pandas as pd
	import numpy as np

	states = pd.read_csv('data/journal_wb.csv', header=4)

	usal = states
	states = states[['Country Name', 'Indicator Name', 'Indicator Code', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013]]

	states = states[states['Indicator Code'].isin(['NY.GNP.PCAP.KD.ZG', 'NY.GNP.PCAP.KD', 'NY.GNP.MKTP.CD', 'SH.XPD.CHEX.PC.CD', 'SI.POV.UMIC', 'IT.NET.USER.ZS', 'SL.UEM.TOTL.ZS', 'NE.CON.PRVT,KD.ZG', 'SP.POP.DPND'])]
	states = states.sort_values('Indicator Code')
	gni_pc_g = states.loc[states['Indicator Code'] == 'NY.GNP.PCAP.KD.ZG']
	gni_pd_g = gni_pc_g.drop(gni_pc_g.ix[:, 'Indicator Name': 'Indicator Code'].head(0).columns, axis=1)
	gni_pc_g.set_index('Country Name', inplace = True)
	gni_pc_g = gni_pc_g.T
	gni_pc_g.index = pd.to_datetime(gni_pc_g.index)
	
	return gni_pc_g
