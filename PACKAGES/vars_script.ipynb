{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# variable names for packages used\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#variable names for inital datasets/read in"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import Gini Index data from the World Bank\n",
    "gini = pd.read_csv('gini.csv', sep=',', header=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Read in world bank data for all the selected states\n",
    "states = pd.read_csv('journal_wb.csv', header=4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create a copy of orignal data to later use to workwith for US analysis\n",
    "usa1 = states"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#unfortunatley there was no individual health or educational data for years with GINI Index data\n",
    "#Hence, will use the Human Development Index in their place from the United Nations Development Program\n",
    "hdi = pd.read_csv('h_d_i.csv', encoding='ISO-8859-1', header=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#variable names used for preprocessing "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Gini data prerocessing\n",
    "#Select only years for which there is US data availble\n",
    "gini1 = gini[['Country Name','1979','1986','1991','1994','1997','2000','2004','2007','2010','2013','2016']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Select 11 countries for analysis, based upon differnt geographic location and GINI Coefficent\n",
    "gini2 = gini1.loc[[2,6,9,21,24,32,38,39,41,44,50]]   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Variable names used in HDI and correlation preprocessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#GNI per capita growth (annual %)\tNY.GNP.PCAP.KD.ZG\n",
    "gni_pc_g= states.loc[states['Indicator Code'] == 'NY.GNP.PCAP.KD.ZG']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#GNI per capita (constant 2010 US$)\n",
    "gni_pc_value = states.loc[states['Indicator Code'] == 'NY.GNP.PCAP.KD']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Current health expenditure per capita (current US$)\n",
    "chc = states.loc[states[\"Indicator Code\"] == \"SH.XPD.CHEX.PC.CD\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Poverty headcount ratio at $5.50 a day (2011 PPP) (% of population)\n",
    "pv = states.loc[states[\"Indicator Code\"] == \"SI.POV.UMIC\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Individuals using the Internet (% of population)\tIT.NET.USER.ZS\n",
    "pi = states.loc[states[\"Indicator Code\"] == \"IT.NET.USER.ZS\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Unemployment, total (% of total labor force) (modeled ILO estimate)\n",
    "urt = states.loc[states[\"Indicator Code\"] == \"SL.UEM.TOTL.ZS\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Households and NPISHs Final consumption expenditure (annual % growth)\n",
    "hsc = states.loc[states[\"Indicator Code\"] == \"NE.CON.PRVT.KD.ZG\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create a differnt df for US values only for later analysis\n",
    "hdi_us = hdi[[\"Country\", '1991','1994','1997','2000','2004','2007','2010','2013']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Only select the United States\n",
    "us = usa.loc[usa[\"Country Name\"] == \"United States\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#unfortunatley there was no individual health or educational data for years with GINI Index data\n",
    "#Hence, will use the Human Development Index in their place from the United Nations Development Program\n",
    "#Read in UN data for the United States\n",
    "us_hdi = hdi_us.iloc[179]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#reformat hdi data to fit the world bank data set and change HDI values from decimal to percent(x100)\n",
    "nhdi  = {'Country Name': \"United States\",\n",
    "        'Indicator Name': \"Human Development Index\",\n",
    "        'Indicator Code': \"HDI\",\n",
    "        '1991': 86.1,\n",
    "        '1994': 87.4,\n",
    "        '1997': 88.1,\n",
    "        '2000': 88.4,\n",
    "        '2004': 89.5,\n",
    "        '2007': 90.5,\n",
    "        '2010': 91.0,\n",
    "        '2013': 91.6}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "frames = [us, us_hdi]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "usa_final = pd.concat(frames, keys=[\"Country Name\", \"Indicator Name\", \"Indicator Code\", \"1991\",\"1994\",\"1997\",\"2000\",\"2004\",\"2007\",\"2010\",\"2013\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "usa_change = pd.concat([usa_final.loc[:1], usa_final.loc[3:5], usa_final.loc[8:]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "uf = usa_final.T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#perform a simple correlation analysis between the GINI index of the US and another metric\n",
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
