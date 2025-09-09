import sys
import numpy as np
import pandas as pd
import json

def get_amenity_list(data):
    amenities_list = data['tags.amenity'].unique()
    # print(amenities_list)
    return  amenities_list

def get_leisure_list(data):
    leisure_list = data['tags.leisure'].unique()
    # print(leisure_list)
    return  leisure_list

def separate_data_by_amenity(data):
    separated_data = {}
    for amenity in data['tags.amenity'].unique():
        separated_data[amenity] = data[data['tags.amenity'] == amenity]
    return separated_data

def keep_specific_amenities(data, amenities_to_keep):
    data = data[data['tags.amenity'].isin(amenities_to_keep)]
    return data

def keep_specific_leisures(data, leisures_to_keep):
    data = data[data['tags.leisure'].isin(leisures_to_keep)]
    return data

# def main():
#     with open('./data/total_data.json') as f:
#         d = json.load(f)
        
#     # with open('./data/export.json') as f:
#     #     d = json.load(f)
    
#     data = pd.json_normalize(d, record_path=['elements'])
#     data = data.filter(items=['lat', 'lon', 'tags.amenity', 'tags.leisure','tags.name'])
#     # data = data.dropna(thresh = 3)
#     data = data.dropna(subset=['lat', 'lon'])
#     print(data)
    
#     # List of amenities selected only specific amenities
#     amenities_to_keep = ['restaurant', 'cafe', 'parking', 'bank', 'library', 
#                          'arts_centre', 'pub', 'bus_station', 'bicycle_parking', 
#                          'atm', 'social_facility', 'theatre', 'university','bar', 
#                          'car_rental', 'boat_rental', 'car_sharing', 'dive_centre']
#     cleaned_data = keep_specific_amenities(data, amenities_to_keep)
#     print(cleaned_data)

#     # # Separate the cleaned data by 'tags.amenity'
#     # separated_data = separate_data_by_amenity(cleaned_data)
#     # print(separated_data)
    
#     # get_amenities_list(data)

#     # # Print the separated data
#     # for amenity, data in separated_data.items():
#     #     print(f"Filtered data for '{amenity}':\n{data}\n")

def main():
    with open('./data/original_data.json') as f:
        d = json.load(f)

    data = pd.json_normalize(d, record_path=['elements'])
    # node_data = pd.json_normalize(node_data)
    # way_data = pd.json_normalize(way_data)
    
    # print(data)
    
    # Cleaning node data
    node_data = data.filter(items=['id', 'lat', 'lon', 'tags.amenity', 'tags.leisure', 'tags.name'])
    # node_data = node_data.dropna(subset=['lat', 'lon'])
    data = data.dropna(thresh = 3)
    amenities_to_keep = ['restaurant', 'cafe', 'parking', 'bank', 'library', 
                            'arts_centre', 'pub', 'bus_station', 'bicycle_parking', 
                            'atm', 'social_facility', 'theatre', 'university','bar', 
                            'car_rental', 'boat_rental', 'car_sharing', 'dive_centre']
    # amenities_to_keep = ['restaurant']
    cleaned_node_data = keep_specific_amenities(node_data, amenities_to_keep)
    
    # leisures_to_keep = ['park' , 'playground', 'picnic_table', 'bowling_alley', 'swimming_pool', 
    #                     'disc_golf_course', 'golf_course', 'garden', 'swimming_area', 'outdoor_seating']
    # cleaned_node_data = keep_specific_leisures(node_data, leisures_to_keep)

    print(cleaned_node_data)
    # print(cleaned_way_data)
    
    cleaned_node_data.to_json('./output/cleaned_node_data.json', orient='records', lines=True)

    
    # Cleaning way data
    with open('./data/housing_data.json') as f:
        d = json.load(f)

    data = pd.json_normalize(d, record_path=['elements'])
    # node_data = pd.json_normalize(node_data)
    # way_data = pd.json_normalize(way_data)
    
    # print(data)
    
    # Cleaning apartments data
    buliding_data = data.filter(items=['id', 'nodes', 'tags.building', 'tags.name'])
    buliding_data["node"] = buliding_data["nodes"].str[0]
    buliding_data = buliding_data.drop(columns=["nodes"])
    buliding_data = buliding_data.loc[buliding_data["tags.building"] == "apartments"]
    # print(buliding_data)

    with open('./data/housing_node.json') as f:
        d = json.load(f)

    data = pd.json_normalize(d, record_path=['elements'])
    buliding_data = buliding_data.merge(data, left_on='node', right_on='id')
    buliding_data = buliding_data.filter(items=['tags.building', 'tags.name', 'lat', 'lon'])
    print(buliding_data)
    
    buliding_data.to_json('./output/buliding_data.json', orient='records', lines=True)
    
    


if __name__=='__main__':
    main()