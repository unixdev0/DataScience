# TORONTO ENTREPRENEURIAL

<hr>

# DATA REPORT

## CONTENT 
- INTRODUCTION - WE INTRODUCE THE PROBLEM 
- DATA - WHERE WE GET THE DATA
- DATA ANALYSIS - IDENTIFY SIGNIFICANT STATS INDICATORS
- METHODOLOGY - ROAD MAP TO SOLVING THE PROBLEM
- MACHINE LEARNING - WHAT ML ALGORITHMS WE USE
- DATA RESULTS - SHARE DATA FINDINGS 
- DISCUSSION - SHARE INVESTIGATING FINDINGS
- CONCLUSION - FINAL THOUGHTS


## INTRODUCTION
The city of Toronto has approached our company to help them develop a service that helps the entrepreneurs who want to establish new businesses in the city of Toronto select an ideal business location based on the ethnic communities they want to be a part of. 
This service will help find an ideal location for a new business based on such factors as business venue, population density in the area, the demographics in the area, average income, proximity to other business venues.

### PROBLEM STATEMENT
Business success/failure depends on a vast spectrum of economics and demographics factors. Entrepreneurs may want to find an optimal venue and geographic location for their new business venture. Such an optimal venue/place selection process has to consider various indicators that may deliver long and prosperous existence for any new business.
Successful businesses help the economy grow, lower the unemployment, and reduce crime. The multicultural city of Toronto wants to offer such an online service where the entrepreneurs can receive all the necessary information that will help them in picking the location for their new ventures based on their desire to support a specific ethnic community of Toronto.


### AUDIENCE
The target audience for this service: Business Entrepreneurs seeking to establish new businesses in the city of Toronto
Having a tool that can help the entrepreneurs to choose the right location for their business will assure long and prosperous existence for such businesses, serving the communities and helping them grow. 


### PROPOSED SOLUTION
The solution will leverage the Foursquare location data as well as the demographics open dataset available from Wikipedia.
In order to advise the entrepreneurs on a good location, we will consider the density (frequency) of similar business venues in various parts of Toronto that cater to preferred ethnic area/neighbourhoods, average income, population, population density, population growth rate, spoken languages in the same area.

## DATA SOURCES
To solve the problem our service will rely on open datasets generated from the following sources:
- Wikipedia
	-- Toronto Boroughs/Neighbourhoods
		https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M
	-- Canada Census - Toronto Demographics
		https://en.wikipedia.org/wiki/Demographics_of_Toronto_neighbourhoods
- GeoCoder/Google Geolocation APIs
- Foursquare APIs

Toronto Boroughs/Neighbourhoods: a list of postal codes in Canada where the first letter is M. Postal codes beginning with M are located within the city of Toronto in the province of Ontario
Canada Census - Toronto Demographics: a list of demographic data on each Toronto neighbourhood as taken from the Canadian Census.
GeoCoder/Google Geolocation APIs: converts addresses into geographic coordinates
Foursquare APIs: offers rich location-based experiences and enables access to millions of up to date business venues, tips, photos and many other helpful tips

## METHODOLOGY
REPORT - MAIN COMPONENTS
DATA [ACQUISITION/POST-PROCESSING/SUMMARY] - in order to perform statistical inference, and apply the machine learning algorithms, the data must be acquired and pre-processed based on the rules derived from the preliminary data analysis
DATA ANALYSIS - Identify the significant informational indicators to use in inferential statistics and machine learning algorithm [Unsupervised: K-Means]
DATA ANALYSIS - Statistical Validation: The datasets underwent statistical analysis and cross referencing in order to determine the data validity and proper distribution, mean and standard deviations, outlier identification.
MACHINE LEARNING - UNSUPERVISED MACHINE LEARNING K-MEANS: In order to cluster various regions of the city based on the business analysis requirements the solution utilizes the unsupervised machine learning algorithm K-MEANS
DATA RESULTS - Present the finding to the stakeholders
DISCUSSION - discuss data investigative findings based on the results
CONCLUSION - report conclusions

## MACHINE LEARNING
OUR DATA ANALYSIS SHOWS LACK OF PROPER DATA LABELING IN THE DATASETS USED BY THE SOLUTION
BASED ON THE DATA ANALYSIS AND THE SOLUTION REQUIREMENTS WE SUGGEST USING AN UNSUPERVISED MACHINE LEARNING APPROACH
WE SUGGEST USING K-MEANS UNSUPERVISED MACHINE LEARNING ALGORITHM TO IDENTIFY GEO CLUSTERS IN THE CITY OF TORONTO THAT ARE MOST SUITABLE FOR OPENING NEW SMALL BUSINESSES IN THE CITY OF TORONTO
IN ORDER TO PERFORM ACCURATE GEO CLUSTERING OUR ALGORITHM RELIES ON GOOGLE GEO LOCATIONS AND FOURSQUARE APIS

## DATA RESULTS
### SUGGESTED NEIGHBOURHOODS
- Westmount
- Bathurst Manor
- Newtonbrook
- Humber Bay Shores
- West Deane Park
- Runnymede
- The Kingsway
- Deer Park

Total Number of venues: 93
Total Number of unique categories: 54
Total Number of clusters: 8

Cluster 0: Etobicoke-Ukrainian
Recommendations for Cluster 0: 
American Restaurant
Ice Cream Shop	
Indie Movie Theater	
Intersection	
Italian Restaurant	
Latin American Restaurant	
Light Rail Station	
Liquor Store	
Mexican Restaurant	
Pharmacy


Cluster 1:Etobicoke-Ukrainian
Recommendations for Cluster 1:
American Restaurant	
Indie Movie Theater	
Intersection	
Italian Restaurant	
Latin American Restaurant	
Light Rail Station	
Liquor Store	
Metro Station	
Mexican Restaurant	
Pet Store


Cluster 2: West Toronto-Ukrainian
Recommendations for Cluster 2:
American Restaurant	
Frozen Yogurt Shop	
Gift Shop	
Video Store	
Intersection	
Light Rail Station	
Liquor Store	
Mexican Restaurant	
Park	
Pet Store

Cluster 3:Etobicoke-Ukrainian
Recommendations for Cluster 3:
American Restaurant	
Video Store	
Indie Movie Theater	
Italian Restaurant	
Latin American Restaurant	
Light Rail Station	
Liquor Store	
Metro Station	
Mexican Restaurant	
Park

Cluster 4:Etobicoke-Russian
Recommendations for Cluster 4:
Ice Cream Shop	
Grocery Store	
Video Store	
Indie Movie Theater	
Intersection	
Italian Restaurant	
Latin American Restaurant	
Light Rail Station	
Metro Station	
Park

Cluster 5:North York-Russian
Recommendations for Cluster 5:
American Restaurant	
Gastropub	
Gym	
Indie Movie Theater	
Intersection	
Italian Restaurant	
Latin American Restaurant	
Light Rail Station	
Liquor Store	
Mexican Restaurant

Cluster 6:North York-Russian
Recommendations for Cluster 6:

Cluster 7:Etobicoke-Ukrainian
Recommendations for Cluster 7:
American Restaurant	
Grocery Store	
Gym	
Ice Cream Shop	
Indie Movie Theater	
Italian Restaurant	
Latin American Restaurant	
Light Rail Station	
Liquor Store	
Mexican Restaurant


## DISCUSSION
THERE ARE VERY INTERESTING TRENDS SHOWING UP N THE DATA ANALYSIS THAT SUGGEST THAT IT IS POSSIBLE TO RECOMMEND NEW LOCATIONS TO BUSINESSES THAT WANT TO EXPAND OR NEW BUSINESSES LOOKING FOR THE FIRST LOCATION.
THERE ARE MULTIPLE STATISTICAL METHODOLOGIES THAT CAN BE EMPLOYED TO FORMULATE A SOUND BUSINESS HYPOTHESIS. SUCH FORMULATED HYPOTHESIS DO REQUIRE VALIDATION VIA GATHERING AND PROCESSING THE SUPPORTING EVIDENCE.
SUCH SUPPORTING EVIDENCE CAN BE PRODUCED BY EMPLOYING ONE OR MORE MACHINE LEARNING ALGORITHMS.
THERE IS ADDITIONAL POTENTIAL IN EMPLOYING A RECOMMENDER SYSTEM ALGORITHM TO FURTHER IMPROVE THE RECOMMENDATIONS REPORT BASED ON A NUMBER OF BUSINESS REQUIREMENTS.

## CONCLUSION
GIVEN ENOUGH RELEVANT DATA IT IS POSSIBLE TO GENERATE SUFFICIENT AMOUNT OF SUPPORTING EVIDENCE IN ORDER TO RECOMMEND WITH A HIGH LEVEL OF PRECISION GEO LOCATIONS FOR NEW OR GROWING BUSINESSES. 
THE CURRENT PROJECT DEMONSTRATES THAT A NEW LOCATION CAN BE SELECTED BASED ON A LIST OF INDICATORS DERIVED VIA INFERENTIAL STATISTICS AND THE RESULTS PROCESSED WITH K-MEANS CLUSTERING MACHINE LEARNING ALGORITHM.
BEING A BUSINESS WITH CLOSE TIES TO VARIOUS ETHNIC COMMUNITIES IN TORONTO WE DEFINITELY CONCUR THAT THE FINDINGS PRESENTED IN THIS REPORT HAVE STRONG MERITS.


