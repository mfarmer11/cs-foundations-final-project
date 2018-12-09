gini.drop(gini.iloc[:,3:23], inplace=True, axis=1)
gini1 = gini[['Country Name', '1979', '1986', '1991', '1994', '1997', '2000', '2004', '2007', '2010', '2013', '2016']]
gini1 = gini1[['Country Name', '2004', '2007', '2010', '2013']]
gini1 = gini1.dropna()
gini1
gini1.index = range(1, 50+1)
gini1 = gini1.sort_values('2004')
gini1.index = range(1, 50+1)
gini2 = gini1.loc[[2,6,9,21,24,32,38,39,41,44,50]]
