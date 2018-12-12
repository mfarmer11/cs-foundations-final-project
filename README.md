# GLOBAL ECONOMIC COMPARISONS

### Abstract

The United States has been cited as one of the most unequal countries in the developed world in terms of income. Many U.S. politicians have argued that income inequality will be one of the United States’ most pressing issues to combat in the 21st century as the rich get richer and the poor get poorer. However, economists are divided over whether the presence of inequality causes negative consequences on the economy or if it negatively impacts the standard of living of Americans in the middle-class and below.  The purpose of this paper is to analyze and illustrate the associations of income inequality with the standard of living in the United States. Through country-comparative analysis, and correlation analysis between Gini Index and various socio-economic indictors such as unemployment, Gross National Income (GNI), Human Development Index (HDI), etc., no strong association was derived that linked the decline in standard of living in the United States with rising income inequality.

### INTRODUCTION

In the past couple of years, world leaders and American politicians have criticized and expressed concern over the increasing income inequality in the United States. Pope Francis declared in his Apostolic Exhortation that “inequality is the root of social ill,” and “as long as the problems of the poor are not radically resolved by rejecting the absolute autonomy of markets and financial speculation and by attacking the structural causes of inequality”, social ill will continue to exist.  (Pope Francis, 2014).  Likewise, in President Barrack Obama emphasized the income gap in the United Sates as the “defining challenge of our time” (Davis and Brook, 2015). President Obama’s rhetoric echoed March 2018 when Senator Bernie Sanders hosted a live streamed town hall, “Inequality in America: Rise of Oligarchy’s and Collapse of the Middle-Class”, with fellow Senator, Elizabeth Warren. During the town hall, they interviewed local and state government officials and non-profit workers about the issues they have faced because of income inequality (Marans, 2018). Catherine Coleman Flowers, a founder of the anti-poverty Alabama Center for Rural Enterprise Community Development Corp. invited U.N. Special Rapporteur on extreme poverty and human rights, Philip Alston, to speak first hand to the issues in Alabama. His verdict on the issue was “it's very uncommon in the first world. This is not a sight that one normally sees” (Silver and Whitehead, 2017). Most of the grievances that these leaders and politicians seem to have are with poverty not income inequality. There is without a doubt that poverty is both an important issue and a challenge that the United States must face. However, are these national and prominent leaders correctly associating poverty as damages caused by income inequality? Is the presence of income inequality in the United States inherently bad or detrimental to the standard of living of the American people? The purpose of this paper is to explore this phenomenon and determine if there are correlations between the rising income inequality in the United States and other metrics that capture standards of living such as income, education, health, unemployment, social engagement, and number of people of under poverty worsen.

### LITERATURE REVIEW

Studies centered between unemployment and income inequality such as Mehic (2018), demonstrate that industrial employment is negatively associated with income inequality. This comes from various possible causes such as trade liberalization, high supply of labor overseas, and skill-biased technological change. There have been multiple studies on the effects and associations of income inequality on American society. Aguiar and Bils (2015) aimed at finding if the rise in income inequality mirrored or was equally reflected in consumption inequality. They performed data analysis on Consumer Expenditure Survey (CE) data from 1980-2010 to demonstrate that consumption inequality had, in fact, kept up with income inequality as result of high-income households shifting more of their consumption from needs to luxury goods relative to lower-income houses. Regarding education, Jerrim and Macmillan (2015) performed a cross-national study of the relationship between rising income inequality across members of the Organization for Economic Co-operation and Development (OECD). Their research showed that the higher financial and non-financial resources are the key to linking income inequality with social mobility as it gives families the capacity to invest in their children’s education. Additionally, Coady and Dizioli (2018) concluded a positive correlation between education and income inequality using the Gini Index across several world regions. They believe that reduction in education inequality can reduce income inequality. Oren Levin-Waldman performed a short time series study between the changes in income inequality and the amount of civic engagement among different income households during the recession years of 2007-2010. His study found that civic engagement increased at both ends of the income gap amongst the low-income and the high-income households, but it decreased among the middle-class (Levin -Waldman, 2014).  Although popular to use, the Gini Index as a measurement for income inequality does have drawback. In a review of the Gini Index, Osberg (2017) argues that the Gini index is not sensitive enough to changes in income inequality. He found that two income distributions can exist with same Gini coefficient. In one scenario the difference between top earners and bottom 40 percent is $60,000, and in another scenario the difference between the top 1 percent and everyone else is $1.4 million. Yet, everyone in the latter distribution is richer than the bottom 40 percent in the former distribution. 

### RESEARCH METHODS

This study aims to capture the scope and nuance of income inequality of the United States in three parts. Part One will compare the income inequality of the United States with that of ten other countries using the Gini index from 2004 to 2013.Ten other countries are chosen to cover a full range in Gini index value with low to high values. Furthermore, these countries will vary geographically as well to avoid regional biases. Additionally, these countries vary regarding types of government and amount wealth. The purpose of this first part is give insight to how the United States ranks amongst other countries and to offer a snapshot in the trend of global inequality.
Part Two aims at exploring deeper into the comparative study between the United States and the other ten countries by comparing them across economic and social metrics across the same time frame of 2004 to 2013. These metrics are intended to capture the standard of living of the general population. The goal is to see if countries with low inequality fall short of countries with higher inequality or by comparing Gini and HDI values, see if countries with high inequality are rising in their standard of living as well. 
Part Three aims to perform a correlation analysis between Gini index and a large set of economic and social metrics across a wider time frame, 1991 to 2013 for the United States. The added metrics and wider time frame are used to give a more robust correlation analysis. The goal is to determine if the standard of living of the general U.S. population is improving or degrading in the presence of growing inequality.  

### DATA

The data used for this study comes from two main international organizations, the World Bank Group and the United Nations. Two of the three datasets come from the World Indicator database from the World Bank open data. Both data sets cover the range of 1960 to 2016. The first dataset contains the Gini index of 264 countries as well as geographic and political regions. Many countries did not have available data, and those that did have data available did so at irregular yearly intervals. Since countries were limited, the scope in time was sacrificed instead for a coherent set of countries. The second dataset contained over fifteen-thousand socio-economic variables for each selected country. Ten metrics were chosen, four economic, four social, and one health from 2004 to 2013. The third dataset from the United Nations Development Programme contains the Human Development Index (HDI) data for 154 countries every year from 1990 to 2015.  The HDI aims to measure the standard of living in a country based upon educational attainment, health attributes, and income inequality from 1990 to 2015. 

### DATA ANALYSIS

#### Pre-Processing

All data pre-processing, mining, and visualization took place using Python and Python packages such as Pandas and Matplotlib. Datasets were imported using Pandas as data frames. Countries, years, and metrics that did not have data for each respective data set were eliminated. This produced the small window of 2004-2013 for the comparative analysis. Of the 246 countries and regions, the ten countries selected were: Denmark, Czech Republic, Ukraine, Pakistan, Greece, United Kingdom, Russian Federation, Thailand, Argentina, and Honduras. These countries met the criteria set out in the research methodology and had data available for socio-economic indicators that aligned within the 2004-2013-time frame and matched data available for the United States as well. 

#### Part One

For part one analysis, the eleven countries were ranked by their 2004 Gini coefficient in descending order, so the most equal countries would be at the top and to serve as a baseline. A new column would be added calculating the change between 2004 to 2013 and the difference was graphed in a bar chart. Lastly, the Gini coefficients were graphed in a time series to illustrate the general trends and patterns income inequality change. 

#### Part Two

For part two analysis, ten metrics were selected from over the fifteen-thousand available from the World Bank database. These were metrics used were: Gross National Income (GNI) growth rate, GNI per capita, GNI, health expenditure per capita, Population in Poverty at $5.5/day, Population of internet users, Unemployment rate, Household consumption, Age dependency ratio, and HDI. All of these metrics were graphed on a time series to demonstrate the change over time, country-to-country comparison, and any trends or patterns. HDI in 2004 and the change in HDI from 2004 to 2013 were also graphed on bar charts so that they could be compared to each country’s 2004 and change in Gini coefficient.

#### Part Three

For part three analysis, the emphasis is only on the United States to see how it its own socio-economic indicator correlate with income inequality using the Gini index. More metrics were added, and some were dropped due to lack of data for some indicators as the time window expanded to 1991 to 2013. The full list of indictors used for correlation analysis are: Employment in industry sector, Age dependency, Unemployment rate, Youth unemployment rate, Tax revenue as GDP, Taxes on income and capital gains, Household Consumption, GDP growth, GDP per capita growth, Population in poverty at $5.5/day, Internet users, GNI per capita growth, GNI per capita, and HDI. Each of these variables were then correlated with the respective Gini index values from 1991 to 2013 to determine what kind of association they have with income inequality. The correlation coefficient of each metric were sorted and placed in a bar chart to show which indicators are negatively and positively correlated with increasing income inequality. 

### KEY FINDINGS

The results of part one analysis show that the United States stayed roughly the same in terms of income inequality, only slightly increasing between 2004 to 2013. However, as seen i n Figure.1 and Figure.2, the general trend for the other ten countries was to move towards the United States position, with low Gini countries like Denmark and Greece showing the greatest amount of increase in inequality, and high Gini countries like Honduras and Argentina showing the most decline in income inequality. The United Kingdom showed a significant reduction in income inequality as it has the most similar form economic market to the United States, yet both countries have vastly different results. Figure.3 shows all countries slightly increases in their Gini coefficient during the time of Great Recession. 
 
![alt text](https://github.com/mfarmer11/cs-foundations-final-project/blob/456a56ae40a34024dd34d6b00460fc9485769fff/images/g1.PNG)

				Figure 1

![alt text](https://github.com/mfarmer11/cs-foundations-final-project/blob/master/images/Figure2.png)
          
				Figure 2
 
![alt text](https://github.com/mfarmer11/cs-foundations-final-project/blob/master/images/po1.PNG)

				Figure.3

Results for the second part analysis show that the socio-economic standards of countries do not always align with their Gini coefficients. For example, Figure.4 illustrates the GNI/capita of each country. The Czech Republic, United Kingdom, Pakistan, and Ukraine score much lower than the United States on the Gini index, 26.5, 33.2, 30.7, 24.6, and 41.0 respectfully. Yet, the United States has a significantly much higher GNI/capita. This demonstrates that although the distribution of income is more unequal in the United States, on average its population makes more income than most other countries. Moreover, Figure. 5 shows the comparison of the unemployment rates of these countries. The United States placed in the middle at 7.38% unemployment in 2013. What was more surprising was the difference between Greece and Thailand, even though they were only a few tenths of percent apart in Gini index in 2013. Greece had an overwhelming high unemployment rate 27.47% unemployment, while Thailand had almost zero unemployment, at 0.49%. 
 
![alt text](https://github.com/mfarmer11/cs-foundations-final-project/blob/456a56ae40a34024dd34d6b00460fc9485769fff/images/gni.PNG)

				Figure. 4
 
![alt text](https://github.com/mfarmer11/cs-foundations-final-project/blob/456a56ae40a34024dd34d6b00460fc9485769fff/images/unemployment.PNG)

				Figure.5

When comparing the HDI across countries, Figure 6 shows the United States topped at number two between Denmark and the United Kingdom. Again, demonstrating that the United States has a relatively high standard of living, when compared with countries that have much lower income inequality. It also important to point out that countries with higher Gini coefficients such as Argentina have a higher HDI than more income equal countries such as Pakistan and Ukraine. Hence, the presence of high income inequality does not necessarily transcend to a lower standard of living. 
 
![alt text](https://github.com/mfarmer11/cs-foundations-final-project/blob/456a56ae40a34024dd34d6b00460fc9485769fff/images/HDI_one.PNG)

				Figure 6

Furthermore, comparing the change in HDI with the change in Gini from 2004-2013 in Figure 7 and Figure 8, the data shows that even as countries increase or decrease in their income inequality, their standard of living is still increasing. 

![alt text](https://github.com/mfarmer11/cs-foundations-final-project/blob/456a56ae40a34024dd34d6b00460fc9485769fff/images/hdi_change.PNG)
 
				Figure 7

![alt text](https://github.com/mfarmer11/cs-foundations-final-project/blob/master/images/Figure7.png)

				Figure 8

Focusing specifically on the United States, Table 1 shows various socio-economic metrics.   Figure 9, shows how these indicators have change between 1991-2013. The results show that HDI has increased the most and employment in the industrial sector has decreased the most. Most of the economic indicators show that the wealth and income of the United States has increased. However, poverty and unemployment rate has also slightly increased. 
 

![alt text](https://github.com/mfarmer11/cs-foundations-final-project/blob/456a56ae40a34024dd34d6b00460fc9485769fff/images/usa.PNG)

				Table 1
 
![alt text](https://github.com/mfarmer11/cs-foundations-final-project/blob/456a56ae40a34024dd34d6b00460fc9485769fff/images/us%20metric%20change.PNG)

				Figure 9

The results of these metrics correlated with Gini index or demonstrated in Figure 10. Most of the metrics used in this study were positively correlated with increasing Gini index, except for employment in the industrial sector, age dependency ratio. A negative association with unemployment rate is a positive relationship as that means more people are employed. 

![alt text](https://github.com/mfarmer11/cs-foundations-final-project/blob/master/images/Figure10.png)
				Figure 10

### RESEARCH LIMITATIONS

The main limitations with this research are the narrow time frame which the data analysis occurs and lack of more explicit education and health data. This is mainly due to the shortage of coherent historical data for these socio-economic metrics. With many countries missing key data, the range of available countries was limited. Other useful data would be to see more accurate poverty data and GNI data by lower and upper 20% of earners. It makes sense that aggregate GNI can be growing if the upper 20% of earners are the cause of this growth, thus increasing the Gini index of the United States if the lower 20% stay the same or decline.

### CONCLUSION

Overall, this paper succeeded in its task to demonstrate that even though the United States faces growing income inequality, it does not serve as a useful measurement describing the quality of its economy and society. Through country comparative analysis, there was no strong association or generalization that could be made about the negative effects of high income inequality, nor that countries low income inequality are better off. Instead, countries are increasing their standard of living, even in the face of growing income inequality. 

### Biographies

Fernando A. Zambrano, M.S.
Fernando is a graduate student enrolled in the Data Science Masters program at the George Washington University. He received his B.A. in International Affairs from the Elliott School of International Affairs at the George Washington University, with a second major in Geography and minor in Geographic Information Systems. Beyond his studies in the classroom, Fernando has worked in a variety of offices in Washington, D.C. At the Association of Global Automakers, he worked on the Trade & Competitiveness division analyzing auto production data, conducting research in support of the North American Free Trade Agreement (NAFTA), and strategizing in opposition of new trade tariffs. As a Junior Trade Analyst with the NAFTA desk at the Embassy of Mexico he created digital maps and visualizations illustrating trade flows and immigration between NAFTA member countries. In his free time, Fernando enjoys coaching Crossfit, training in Muay Thai boxing and Brazilian Jiu-Jitsu, and bartending at a neighborhood bar in Adams Morgan.

Nima Zahadat, Ph.D
Nima Zahadat is professor of data science, information systems, and computer science at the George Washington University and George Mason University. He has taught courses in the fields of information systems, engineering, data science, web development, and security. He has developed and taught over 100 different information systems, security, and project management curricula throughout his career. Dr. Zahadat has also held positions as Chief Security Officer, Chief Information Officer, Director of Security, Director of Training Solutions, Dean of Computer science, Program Chair of Information Systems, and Director of Operations. He has an undergraduate degree in Mathematics from George Mason, a graduate degree in Information Systems from George Washington, and a Ph.D. in Systems Engineering and Engineering Management from George Washington. Dr. Zahadat hobbies include biking, photography, travel, skiing, and writing.