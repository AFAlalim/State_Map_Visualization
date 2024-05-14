import folium
import json



def generate_sudan_map(data, geojson_file):
  # Load Sudan GeoJSON data
  sudan_map = folium.Choropleth(
      geo_data=json.load(open(geojson_file)),
      fill_opacity=0.7,
      name='Sudan States Map',
      show_colorbar=True,
  )

  # Process and style data
  for state in data:
    state_id = state['id']  # Assuming your data has an 'id' field matching GeoJSON property
    state_color = state['color']
    state_value = state['value']

  # Find the feature corresponding to the state ID (assuming a 'properties.admin_code' property in GeoJSON)
    for feature in sudan_map.geo_features:
      if feature['properties']['admin_code'] == state_id:
        feature['fillColor'] = state_color
        feature['fillOpacity'] = 0.7
        feature['tooltip'] = f"{state['name']}: {state_value}"
        break  # Exit loop after finding the matching feature

  # Customize map appearance
  sudan_map.add_tile_layer('Stamen Toner')
  sudan_map.center = [15.5, 32.5]
  sudan_map.zoom_start = 4

  return sudan_map

# Example usage with sample data (assuming 'id' matches GeoJSON property)
sample_data = [
    {
        "id": "SD-KH",  # Replace with actual property name from your GeoJSON data
        "name": "Khartoum State",
        "color": "YlGn",
        "value": 100
    },
    {
        "id": "SD-KS",  # Replace with actual property name from your GeoJSON data
        "name": "Kassala State",
        "color": "YlGn",
        "value": 75
    },
    # ... add more states as needed
]

# Replace 'sdadmbndaadm1.geojson' with the actual filename you downloaded
sudan_map = generate_sudan_map(sample_data, 'sdadmbndaadm1.geojson')

# Display the map
sudan_map.save('sudan_kidney_density.html')
