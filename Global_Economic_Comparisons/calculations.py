
# coding: utf-8
def calculations():
	#Add a new collumn to see the amount in Gini Coefficent from 2004-2013
	gini1["Change"] = ((gini1["2013"] - gini1["2004"]))

	#Create a change column in HDI
	hdi["Change"] = ((hdi["2013"] - hdi["2004"]))

	#perform a simple correlation analysis between the GINI index of the US and another metric

	gini_txr = uf['GINI index (World Bank estimate)'].corr(uf['Tax revenue (% of GDP)'])
	gini_txi = uf['GINI index (World Bank estimate)'].corr(uf['Taxes on income, profits and capital gains (% of total taxes)'])
	gini_i = uf['GINI index (World Bank estimate)'].corr(uf['Individuals using the Internet (% of population)'])
	gini_hc = uf['GINI index (World Bank estimate)'].corr(uf['Households and NPISHs Final consumption expenditure (annual % growth)'])\n",gini_gdp_rt = uf['GINI index (World Bank estimate)'].corr(uf['GDP growth (annual %)'])
	gini_gdp_pc_rt = uf['GINI index (World Bank estimate)'].corr(uf['GDP per capita growth (annual %)'])
	gini_gni_pc = uf['GINI index (World Bank estimate)'].corr(uf['GNI per capita (constant 2010 US$)'])
	gini_gni_pc_rt = uf['GINI index (World Bank estimate)'].corr(uf['GNI per capita growth (annual %)'])
	gini_pr = uf['GINI index (World Bank estimate)'].corr(uf['Poverty headcount ratio at $5.50 a day (2011 PPP) (% of population)'])
	gini_ei = uf['GINI index (World Bank estimate)'].corr(uf['Employment in industry (% of total employment) (modeled ILO estimate)'])
	gini_yth_urt = uf['GINI index (World Bank estimate)'].corr(uf['Unemployment, youth total (% of total labor force ages 15-24) (modeled ILO estimate)'])
	gini_urt = uf['GINI index (World Bank estimate)'].corr(uf['Unemployment, total (% of total labor force) (modeled ILO estimate)'])
	gini_adr = uf['GINI index (World Bank estimate)'].corr(uf['Age dependency ratio (% of working-age population)'])
	gini_hdi = uf['GINI index (World Bank estimate)'].corr(uf['Human Development Index'])


	#Store correlation values in a diction for easy access


	us_correlation_dict = [{"Tax rev as GDP":gini_txr, "Tax rev on income":gini_txi, "Internet users":gini_i,
                      "Household Consumption":gini_hc, "GDP growth": gini_gdp_rt, "GDP per capita grwoth": gini_gdp_pc_rt,
                   "GNI per capita": gini_gni_pc, "GNI per capita growth": gini_gni_pc_rt,
                       "Poverty at $5.5 a day": gini_pr, "Employment in industry sector": gini_ei,
                        "Youth unemployment rate": gini_yth_urt, "Unemployment rate": gini_urt,
                        "Age dependency ration": gini_adr, "Human Development Index": gini_hdi}]


	#Convert dictionary to a dataframe
	us_corr = pd.DataFrame(us_correlation_dict)


	#transpose data frame
	us_corr = us_corr.T

	#rename column with r values to correlation
	us_corr.columns = ["Correlation"]
	return;
