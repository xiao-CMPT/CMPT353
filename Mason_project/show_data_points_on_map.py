import pandas as pd
import folium

# Load data
education_data = pd.read_csv('./data/After/education.csv')
healthcare_data = pd.read_csv('./data/After/healthcare.csv')
entertainment_data = pd.read_csv('./data/After/entertainment.csv')
shopMall_data = pd.read_csv('./data/After/shopMall.csv')

# Calculate the average latitude and longitude across all datasets
avg_lat = pd.concat([education_data['lat'], healthcare_data['lat'], entertainment_data['lat'], shopMall_data['lat']]).mean()
avg_lon = pd.concat([education_data['lon'], healthcare_data['lon'], entertainment_data['lon'], shopMall_data['lon']]).mean()

# Create a map centered around the average latitude and longitude values
m = folium.Map(location=(avg_lat, avg_lon), zoom_start=13)

# Function to add markers to map
def add_markers(data, color):
    for _, row in data.iterrows():
        folium.Marker(
            location=(row['lat'], row['lon']),
            icon=folium.Icon(color=color)
        ).add_to(m)

# Add a circle with diameter 2000m (radius 1000m) at the center of your data points
folium.Circle(
    radius=2000,
    location=(avg_lat, avg_lon),
    color="crimson",
    fill=False,
).add_to(m)

# Add markers to map
add_markers(education_data, 'red')
add_markers(healthcare_data, 'blue')
add_markers(entertainment_data, 'green')
add_markers(shopMall_data, 'black')

# Save map to HTML
m.save('./result/data_map.html')
