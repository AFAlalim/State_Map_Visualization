import folium
import json
import pandas as pd
# initialize the map and store it in a m object
m = folium.Map(location=[40, -95], zoom_start=4)

# show the map
m
geojson_file = 'sdadmbndaadm1.geojson'
states ='SD.csv' 
state_geo = json.load(open(geojson_file))
state_data = pd.read_csv(states)
state_data.head()