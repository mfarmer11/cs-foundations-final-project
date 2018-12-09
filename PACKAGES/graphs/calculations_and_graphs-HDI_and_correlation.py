{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#GNI per capita growth graph\n",
    "ax = gni_pc_g.plot(figsize=(20,10), fontsize=13)\n",
    "plt.legend(loc='best', fontsize=13)\n",
    "plt.title('GNI per Capita Growth(%): 2004-2013', fontsize=20)\n",
    "ax.set_xlabel('Year', fontsize=13)\n",
    "ax.set_ylabel('(%) Growth', fontsize=13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#GNI/capita graph\n",
    "ax = gni_pc_value.plot(figsize=(20,10), fontsize=13)\n",
    "plt.legend(loc='best', fontsize=13)\n",
    "plt.title('GNI per Capita: 2004-2013', fontsize=20)\n",
    "ax.set_xlabel('Year', fontsize=13)\n",
    "ax.set_ylabel('(constant 2010 US$)', fontsize=13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#GNI graph\n",
    "ax = gni.plot(figsize=(20,10), fontsize=13)\n",
    "plt.legend(loc='best', fontsize=13)\n",
    "plt.title('GNI: 2004-2013', fontsize=20)\n",
    "ax.set_xlabel('Year', fontsize=13)\n",
    "ax.set_ylabel('Current  US$ (10 trillion)', fontsize=13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Health Expenditure/capita graph\n",
    "ax = chc.plot(figsize=(20,10), fontsize=13)\n",
    "plt.legend(loc='best', fontsize=13)\n",
    "plt.title('Health Expendetiture per Captia: 2004-2013', fontsize=20)\n",
    "ax.set_xlabel('Year', fontsize=13)\n",
    "ax.set_ylabel('Current US$', fontsize=13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Poverty head couunt ratio graph\n",
    "ax = pv.plot(figsize=(20,10), fontsize=13)\n",
    "plt.legend(loc='best', fontsize=13)\n",
    "plt.title('Population in Poverty at $5.5 a Day: 2004-2013', fontsize=20)\n",
    "ax.set_xlabel('Year', fontsize=13)\n",
    "ax.set_ylabel('% of Population', fontsize=13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Number of internet users graph\n",
    "ax = pi.plot(figsize=(20,10), fontsize=13)\n",
    "plt.legend(loc='best', fontsize=13)\n",
    "plt.title('Number of Internet Users: 2004-2013', fontsize=20)\n",
    "ax.set_xlabel('Year', fontsize=13)\n",
    "ax.set_ylabel('% of Population', fontsize=13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Total Unemployment graph\n",
    "ax = urt.plot(figsize=(20,10), fontsize=13)\n",
    "plt.legend(loc='best', fontsize=13)\n",
    "plt.title('Unemployment Rate: 2004-2013', fontsize=20)\n",
    "ax.set_xlabel('Year', fontsize=13)\n",
    "ax.set_ylabel('% of Total Labor Force', fontsize=13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Household Consumption graph\n",
    "ax = hsc.plot(figsize=(20,10), fontsize=13)\n",
    "plt.legend(loc='best', fontsize=13)\n",
    "plt.title('Household Consumption Expenditure: 2004-2013', fontsize=20)\n",
    "ax.set_xlabel('Year', fontsize=13)\n",
    "ax.set_ylabel('Annual % Growth', fontsize=13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Age Dependency Ratio graph\n",
    "ax = adr.plot(figsize=(20,10), fontsize=13)\n",
    "plt.legend(loc='best', fontsize=13)\n",
    "plt.title('Age Dependency Ratio: 2004-2013', fontsize=20)\n",
    "ax.set_xlabel('Year', fontsize=13)\n",
    "ax.set_ylabel('% of Working-Age Population', fontsize=13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create a change column in HDI\n",
    "hdi[\"Change\"] = ((hdi[\"2013\"] - hdi[\"2004\"]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Bar graph comparing HDI across the 11 countries for 2004\n",
    "hdi.set_index('Country', inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "hdi = hdi.sort_values(by='2004', ascending=False)\n",
    "pd.Series(hdi['2004']).plot(kind='barh',\n",
    "                                                    title= \"Human Development Index:2004\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Bar graph comparing the change in HDI across the 11 countries\n",
    "hdi = hdi.sort_values(by='Change', ascending=False)\n",
    "pd.Series(hdi['Change']).plot(kind='barh',\n",
    "                                                    title= \"Human Development Index Change:2004-2013\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "del hdi[\"Change\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "hdi = hdi.T\n",
    "hdi.index = pd.to_datetime(hdi.index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Time series visualizing the change in HDI\n",
    "\n",
    "ax = hdi.plot(figsize=(20,10), fontsize=13)\n",
    "plt.legend(loc='best', fontsize=13)\n",
    "plt.title('Human Development Index: 2004-2013', fontsize=20)\n",
    "ax.set_xlabel('Year', fontsize=13)\n",
    "ax.set_ylabel('HDI', fontsize=13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#make a graph showing the change across tiem frame\n",
    "usa_change = usa_change.sort_values(by='Change', ascending=False)\n",
    "pd.Series(usa_change['Change']).plot(kind='barh', \n",
    "                                                    title= \"Metric Changes for the United States: 1991-2013\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#perform a simple correlation analysis between the GINI index of the US and another metric\n",
    "\n",
    "gini_txr = uf['GINI index (World Bank estimate)'].corr(uf['Tax revenue (% of GDP)'])\n",
    "gini_txi = uf['GINI index (World Bank estimate)'].corr(uf['Taxes on income, profits and capital gains (% of total taxes)'])\n",
    "gini_i = uf['GINI index (World Bank estimate)'].corr(uf['Individuals using the Internet (% of population)'])\n",
    "gini_hc = uf['GINI index (World Bank estimate)'].corr(uf['Households and NPISHs Final consumption expenditure (annual % growth)'])\n",
    "gini_gdp_rt = uf['GINI index (World Bank estimate)'].corr(uf['GDP growth (annual %)'])\n",
    "gini_gdp_pc_rt = uf['GINI index (World Bank estimate)'].corr(uf['GDP per capita growth (annual %)'])\n",
    "gini_gni_pc = uf['GINI index (World Bank estimate)'].corr(uf['GNI per capita (constant 2010 US$)'])\n",
    "gini_gni_pc_rt = uf['GINI index (World Bank estimate)'].corr(uf['GNI per capita growth (annual %)'])\n",
    "gini_pr = uf['GINI index (World Bank estimate)'].corr(uf['Poverty headcount ratio at $5.50 a day (2011 PPP) (% of population)'])\n",
    "gini_ei = uf['GINI index (World Bank estimate)'].corr(uf['Employment in industry (% of total employment) (modeled ILO estimate)'])\n",
    "gini_yth_urt = uf['GINI index (World Bank estimate)'].corr(uf['Unemployment, youth total (% of total labor force ages 15-24) (modeled ILO estimate)'])\n",
    "gini_urt = uf['GINI index (World Bank estimate)'].corr(uf['Unemployment, total (% of total labor force) (modeled ILO estimate)'])\n",
    "gini_adr = uf['GINI index (World Bank estimate)'].corr(uf['Age dependency ratio (% of working-age population)'])\n",
    "gini_hdi = uf['GINI index (World Bank estimate)'].corr(uf['Human Development Index'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Store correlation values in a diction for easy access\n",
    "\n",
    "us_correlation_dict = [{\"Tax rev as GDP\":gini_txr, \"Tax rev on income\":gini_txi, \"Internet users\":gini_i,\n",
    "                        \"Household Consumption\":gini_hc, \"GDP growth\": gini_gdp_rt, \"GDP per capita grwoth\": gini_gdp_pc_rt,\n",
    "                       \"GNI per capita\": gini_gni_pc, \"GNI per capita growth\": gini_gni_pc_rt,\n",
    "                        \"Poverty at $5.5 a day\": gini_pr, \"Employment in industry sector\": gini_ei,\n",
    "                        \"Youth unemployment rate\": gini_yth_urt, \"Unemployment rate\": gini_urt,\n",
    "                        \"Age dependency ration\": gini_adr, \"Hunman Development Index\": gini_hdi}]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Convert dictionary to a dataframe\n",
    "us_corr = pd.DataFrame(us_correlation_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#transpose data frame\n",
    "us_corr = us_corr.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#rename column with r values to \"Correlation\"\n",
    "us_corr.columns = [\"Correlation\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Graph correlation as bar\n",
    "us_corr = us_corr.sort_values(by='Correlation', ascending=False)\n",
    "pd.Series(us_corr['Correlation']).plot(kind='barh', \n",
    "                                                    title= \"Correlation: U.S GINI vs U.S Economic & Social Metrics\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}