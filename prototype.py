import geocoder
import time


g = geocoder.google('{}, Toronto, Ontario'.format('Yonge and St.Clair'))
lat_lng_coords = g.latlng
    
if lat_lng_coords != None:
    print(lat_lng_coords[0])
    print(lat_lng_coords[1])
print('Successfully populated geo locations')


import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get("https://en.wikipedia.org/wiki/Demographics_of_Toronto_neighbourhoods")
soup = BeautifulSoup(res.content,'lxml')
wikitables = soup.find_all('table') 
Toronto = pd.read_html(str(wikitables[1]), index_col=None, header=0)[0]
Toronto.head()

Toronto.drop(columns=['FM', 'Census Tracts', '% Change in Population since 2001', 'Land area (km2)', 'Transit Commuting\xa0%', '% Renters', 'Second most common language (after English) by name', 'Map'], inplace=True)

Toronto.drop([0], inplace=True)
