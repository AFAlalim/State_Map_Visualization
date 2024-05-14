State Map Visualization:

State Map with Attribute Density Visualization (Python) 
This Python code generates a choropleth map of any country (E.g Sudan), visualizing the density of a specific attribute across its states. Users can provide data about each state (ID, value) and a GeoJSON file containing the country/state (Sudan)'s administrative boundaries.  

Functionality: 
* Leverages the Folium library to create an interactive map. 
* Uses a GeoJSON file to define the state boundaries. You can download it from (https://datacatalog.worldbank.org/home) OR any Geo data source.
* Assign colors to states based on the provided attribute values.  

Requirements: 
* Python 3 (tested with 3.x) 
* Folium library (pip install folium)


input: 
CSV/JSON file contains data about each state (ID, value) 

output:
State Map with Attribute Density Visualization as HTML file

