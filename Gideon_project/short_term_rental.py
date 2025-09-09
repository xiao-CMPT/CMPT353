import numpy as np
import pandas as pd
from numpy import cos, arcsin, sqrt, pi
import folium
from folium.plugins import HeatMap

cleaned_data_bby = './output/cleaned_node_data.json'
rental_data_bby = './output/buliding_data.json'
bby_central_location = [49.151501, -122.595903]


# from https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/21623206
# change it to numpy verison
def locations_distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * arcsin(sqrt(a))


def amenity_density(x, y, scope_radius, data):
    data['distance'] = locations_distance(x, y, data['lat'], data['lon']) * 1000
    # Filter amenities within the scope
    # Calculate the area of the circular scope (in square meters)
    # Calculate the density by dividing the number of amenities within the scope by the area of the scope
    target_within_scope = data[data['distance'] <= scope_radius]
    scope_area_sqm = pi * (scope_radius ** 2)
    amenity_density = len(target_within_scope) / scope_area_sqm * 10000
    return amenity_density


    

def weighted_amenity_density(x, y, scope_radius, data):
    data['distance'] = locations_distance(x, y, data['lat'], data['lon']) * 1000
    # Filter amenities within the scope
    # Calculate the area of the circular scope (in square meters)
    # Calculate the density by dividing the number of amenities within the scope by the area of the scope
    target_within_scope = data[data['distance'] <= scope_radius]
    
    weigthed_target = target_within_scope['weighted'].sum()
    scope_area_sqm = pi * (scope_radius ** 2)
    amenity_density = weigthed_target / scope_area_sqm * 10000
    return amenity_density




def main():
    rental = pd.read_json(rental_data_bby, lines=True)
    data = pd.read_json(cleaned_data_bby, lines=True)
    print(data)
    print(rental)
    
    scope = 1000

    count_list = []
    count_list = rental.apply(lambda row: amenity_density(row['lat'], row['lon'], scope, data), axis=1)
    rental['num_of_amenity'] = count_list
    sorted_rental = rental.sort_values(by='num_of_amenity', ascending=False)
    hit_not_weighted = sorted_rental.head(50)
    print(sorted_rental.head(10))

    # add weighted
    data['weighted'] = 1
    data.loc[data['tags.amenity'] == 'bank', 'weighted'] = 2
    data.loc[data['tags.amenity'] == 'atm', 'weighted'] = 2
    data.loc[data['tags.amenity'] == 'restaurant', 'weighted'] = 3
    data.loc[data['tags.amenity'] == 'bus_station', 'weighted'] = 5
    data.loc[data['tags.amenity'] == 'theatre', 'weighted'] = 4
    data.loc[data['tags.amenity'] == 'dive_centre', 'weighted'] = 4
    # print(data)

    print()

    count_list = []
    count_list = rental.apply(lambda row: weighted_amenity_density(row['lat'], row['lon'], scope, data), axis=1)
    rental['num_of_amenity'] = count_list
    sorted_rental = rental.sort_values(by='num_of_amenity', ascending=False)
    hit_weighted = sorted_rental.head(50)
    print(sorted_rental.head(10))


    # heatmap ref1: https://wellsr.com/python/plotting-geographical-heatmaps-with-python-folium-module/
    # heatmap ref2: https://www.kaggle.com/code/daveianhickey/how-to-folium-for-maps-heatmaps-time-data
    data_apartment = pd.DataFrame(rental, columns=['lat','lon'])
    data_apartment = data_apartment.dropna()
    # print(data_apartment)
  
    map_obj = folium.Map(location = bby_central_location, tiles = "Stamen Terrain", zoom_start = 10)
    HeatMap(np.array(data_apartment).tolist()).add_to(map_obj)

    no_weighted = pd.DataFrame(hit_not_weighted, columns=['lat','lon'])
    no_weighted = no_weighted.dropna()

    for point in np.array(no_weighted).tolist():
        folium.Marker(point,
              popup=folium.Popup('no_weighted', max_width=100),
              icon=folium.Icon(color='blue')
             ).add_to(map_obj)
        
    
    weighted = pd.DataFrame(hit_weighted, columns=['lat','lon'])
    weighted = weighted.dropna()

    for point in np.array(weighted).tolist():
        folium.Marker(point,
              popup=folium.Popup('weighted', max_width=100),
              icon=folium.Icon(color='red')
             ).add_to(map_obj)

    map_obj.save("./output/heatmap_apartments.html")




if __name__=='__main__':
    main()