
def load_gini():
	import pandas as pd
	import numpy as np
	gini = pd.read_csv('data/gini.csv', header=4)
	gini.drop(gini.iloc[:,3:23], inplace=True, axis=1)
	gini1 = gini[['Country Name', '1979', '1986', '1991', '1994', '1997', '2000', '2004', '2007', '2010', '2013', '2016']]
	gini1 = gini1[['Country Name', '2004', '2007', '2010', '2013']]
	gini1 = gini1.dropna()
	gini1.index = range(1, 50+1)
	gini1 = gini1.sort_values('2004')
	gini1.index = range(1, 50+1)
	gini1['Change'] = ((gini1["2013"] - gini1["2004"]))
	gini1.index = range(1, 50+1)
	gini2 = gini1.loc[[2,6,9,21,24,32,38,39,41,44,50]]
	gini2.set_index('Country Name', inplace=True)
	gini2 = gini2.sort_values(by='2004', ascending=False)

	return gini2
