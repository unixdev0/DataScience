# Applied Data Science - Capstone

# DATA

## DATA SOURCES

To solve the problem our service will rely on open datasets generated from the following sources:
- Wikipedia
-- Toronto Boroughs/Neighbourhoods
--- https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M
-- Canada Census - Toronto Demographics
--- https://en.wikipedia.org/wiki/Demographics_of_Toronto_neighbourhoods
- GeoCoder/Google Geolocation APIs
- Foursquare APIs

### Toronto Borouhs/Neighbourhoods

Toronto Borough/Neighbourhood table contains a list of postal codes in Canada where the first letter is M. Postal codes beginning with M are located within the city of Toronto in the province of Ontario. Only the first three characters are listed, corresponding to the Forward Sortation Area.

Note: There are no rural FSAs in Toronto, hence no postal codes start with M0.

### Canada Census - demographic data on each Toronto neighbourhood

The list of demographic data on each Toronto neighbourhood is taken from the 2006 Canadian census.

Note: Neighbourhood boundaries are approximated to the nearest census tract - https://en.wikipedia.org/wiki/Census_tract

### GeoCoder/Google Geolocation APIs

Geocoding is the process of converting addresses (like "1600 Amphitheatre Parkway, Mountain View, CA") into geographic coordinates (like latitude 37.423021 and longitude -122.083739), which you can use to place markers or position the map.

The Maps JavaScript API provides a geocoder class for geocoding and reverse geocoding dynamically from user input. If instead you wish to geocode static, known addresses, see the Geocoding web service.

### Foursquare APIs
Foursquare APIs offer rich location-based experiences and enable:
- Access to millions of fresh venue-related tips, tastes, photos & attributes from the Foursquare community
- Access places data - in real time - from any connected application
- Accurately assign a mobile app user to a specific location (Snap-to-Place)
- Enable users to search and discover venues via a mobile app or website
- Geo-tag content such as a photos, videos and more in your mobile app or website
- Know where your mobile app users go in the real world
- Build mobile audience segments for analysis, targeting and measurement
