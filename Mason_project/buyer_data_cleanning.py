import numpy as np
import os
import pandas as pd
import geopandas as gpd
from sklearn.neighbors import LocalOutlierFactor


# drop useless data
def drop_useless_amenities(data):
    # amenity data cleanning
    # sustenance

    data.drop(data.index[data['amenity'] == 'bar'], inplace=True)
    data.drop(data.index[data['amenity'] == 'biergarten'], inplace=True)
    data.drop(data.index[data['amenity'] == 'cafe'], inplace=True)
    data.drop(data.index[data['amenity'] == 'fast_food'], inplace=True)
    data.drop(data.index[data['amenity'] == 'food_court'], inplace=True)
    data.drop(data.index[data['amenity'] == 'ice_cream'], inplace=True)
    data.drop(data.index[data['amenity'] == 'pub'], inplace=True)
    data.drop(data.index[data['amenity'] == 'restaurant'], inplace=True)
    # Education
    data.drop(data.index[data['amenity'] == 'driving_school'], inplace=True)
    data.drop(data.index[data['amenity'] == 'research_institute'], inplace=True)
    data.drop(data.index[data['amenity'] == 'training'], inplace=True)
    data.drop(data.index[data['amenity'] == 'music_school'], inplace=True)
    data.drop(data.index[data['amenity'] == 'traffic_park'], inplace=True)
    # Transportation
    data.drop(data.index[data['amenity'] == 'bicycle_parking'], inplace=True)
    data.drop(data.index[data['amenity'] == 'bicycle_repair_station'], inplace=True)
    data.drop(data.index[data['amenity'] == 'bicycle_rental'], inplace=True)
    data.drop(data.index[data['amenity'] == 'boat_rental'], inplace=True)
    data.drop(data.index[data['amenity'] == 'boat_sharing'], inplace=True)
    data.drop(data.index[data['amenity'] == 'bus_station'], inplace=True)
    data.drop(data.index[data['amenity'] == 'car_rental'], inplace=True)
    data.drop(data.index[data['amenity'] == 'car_sharing'], inplace=True)
    data.drop(data.index[data['amenity'] == 'car_wash'], inplace=True)
    data.drop(data.index[data['amenity'] == 'compressed_air'], inplace=True)
    data.drop(data.index[data['amenity'] == 'vehicle_inspection'], inplace=True)
    data.drop(data.index[data['amenity'] == 'charging_station'], inplace=True)
    data.drop(data.index[data['amenity'] == 'driver_training'], inplace=True)
    data.drop(data.index[data['amenity'] == 'ferry_terminal'], inplace=True)
    data.drop(data.index[data['amenity'] == 'fuel'], inplace=True)
    data.drop(data.index[data['amenity'] == 'grit_bin'], inplace=True)
    data.drop(data.index[data['amenity'] == 'motorcycle_parking'], inplace=True)
    data.drop(data.index[data['amenity'] == 'parking'], inplace=True)
    data.drop(data.index[data['amenity'] == 'parking_entrance'], inplace=True)
    data.drop(data.index[data['amenity'] == 'parking_space'], inplace=True)
    data.drop(data.index[data['amenity'] == 'taxi'], inplace=True)
    # Financial
    data.drop(data.index[data['amenity'] == 'atm'], inplace=True)
    data.drop(data.index[data['amenity'] == 'bank'], inplace=True)
    data.drop(data.index[data['amenity'] == 'bureau_de_change'], inplace=True)
    # Healthcare
    data.drop(data.index[data['amenity'] == 'baby_hatch'], inplace=True)
    data.drop(data.index[data['amenity'] == 'nursing_home'], inplace=True)
    data.drop(data.index[data['amenity'] == 'social_facility'], inplace=True)
    data.drop(data.index[data['amenity'] == 'veterinary'], inplace=True)
    # Entertainment, Arts & Culture
    data.drop(data.index[data['amenity'] == 'arts_centre'], inplace=True)
    data.drop(data.index[data['amenity'] == 'brothel'], inplace=True)
    data.drop(data.index[data['amenity'] == 'casino'], inplace=True)
    data.drop(data.index[data['amenity'] == 'fountain'], inplace=True)
    data.drop(data.index[data['amenity'] == 'gambling'], inplace=True)
    data.drop(data.index[data['amenity'] == 'love_hotel'], inplace=True)
    data.drop(data.index[data['amenity'] == 'nightclub'], inplace=True)
    data.drop(data.index[data['amenity'] == 'planetarium'], inplace=True)
    data.drop(data.index[data['amenity'] == 'public_bookcase'], inplace=True)
    data.drop(data.index[data['amenity'] == 'stripclub'], inplace=True)
    data.drop(data.index[data['amenity'] == 'studio'], inplace=True)
    data.drop(data.index[data['amenity'] == 'swingerclub'], inplace=True)
    # Public Service
    data.drop(data.index[data['amenity'] == 'courthouse'], inplace=True)
    data.drop(data.index[data['amenity'] == 'post_box'], inplace=True)
    data.drop(data.index[data['amenity'] == 'post_depot'], inplace=True)
    data.drop(data.index[data['amenity'] == 'post_office'], inplace=True)
    data.drop(data.index[data['amenity'] == 'prison'], inplace=True)
    data.drop(data.index[data['amenity'] == 'ranger_station'], inplace=True)
    data.drop(data.index[data['amenity'] == 'townhall'], inplace=True)
    # Facilities
    data.drop(data.index[data['amenity'] == 'bbq'], inplace=True)
    data.drop(data.index[data['amenity'] == 'bench'], inplace=True)
    data.drop(data.index[data['amenity'] == 'dog_toilet'], inplace=True)
    data.drop(data.index[data['amenity'] == 'dressing_room'], inplace=True)
    data.drop(data.index[data['amenity'] == 'drinking_water'], inplace=True)
    data.drop(data.index[data['amenity'] == 'give_box'], inplace=True)
    data.drop(data.index[data['amenity'] == 'mailroom'], inplace=True)
    data.drop(data.index[data['amenity'] == 'parcel_locker'], inplace=True)
    data.drop(data.index[data['amenity'] == 'shelter'], inplace=True)
    data.drop(data.index[data['amenity'] == 'shower'], inplace=True)
    data.drop(data.index[data['amenity'] == 'toilets'], inplace=True)
    data.drop(data.index[data['amenity'] == 'water_point'], inplace=True)
    data.drop(data.index[data['amenity'] == 'watering_place'], inplace=True)
    # Waste Management
    data.drop(data.index[data['amenity'] == 'sanitary_dump_station'], inplace=True)
    data.drop(data.index[data['amenity'] == 'recycling'], inplace=True)
    data.drop(data.index[data['amenity'] == 'waste_basket'], inplace=True)
    data.drop(data.index[data['amenity'] == 'waste_disposal'], inplace=True)
    data.drop(data.index[data['amenity'] == 'waste_transfer_station'], inplace=True)
    # Others
    data.drop(data.index[data['amenity'] == 'animal_boarding'], inplace=True)
    data.drop(data.index[data['amenity'] == 'animal_breeding'], inplace=True)
    data.drop(data.index[data['amenity'] == 'animal_shelter'], inplace=True)
    data.drop(data.index[data['amenity'] == 'animal_training'], inplace=True)
    data.drop(data.index[data['amenity'] == 'baking_oven'], inplace=True)
    data.drop(data.index[data['amenity'] == 'clock'], inplace=True)
    data.drop(data.index[data['amenity'] == 'crematorium'], inplace=True)
    data.drop(data.index[data['amenity'] == 'dive_centre'], inplace=True)
    data.drop(data.index[data['amenity'] == 'grave_yard'], inplace=True)
    data.drop(data.index[data['amenity'] == 'hunting_stand'], inplace=True)
    data.drop(data.index[data['amenity'] == 'internet_cafe'], inplace=True)
    data.drop(data.index[data['amenity'] == 'kitchen'], inplace=True)
    data.drop(data.index[data['amenity'] == 'kneipp_water_cure'], inplace=True)
    data.drop(data.index[data['amenity'] == 'lounger'], inplace=True)
    data.drop(data.index[data['amenity'] == 'marketplace'], inplace=True)
    data.drop(data.index[data['amenity'] == 'monastery'], inplace=True)
    data.drop(data.index[data['amenity'] == 'photo_booth'], inplace=True)
    data.drop(data.index[data['amenity'] == 'place_of_mourning'], inplace=True)
    data.drop(data.index[data['amenity'] == 'public_bath'], inplace=True)
    data.drop(data.index[data['amenity'] == 'refugee_site'], inplace=True)
    data.drop(data.index[data['amenity'] == 'vending_machine'], inplace=True)
    data.drop(data.index[data['amenity'] == 'user defined'], inplace=True)
    # leisure data cleanning
    # comment
    data.drop(data.index[data['leisure'] == 'adult_gaming_centre'], inplace=True)
    data.drop(data.index[data['leisure'] == 'amusement_arcade'], inplace=True)
    data.drop(data.index[data['leisure'] == 'bandstand'], inplace=True)
    data.drop(data.index[data['leisure'] == 'bathing_place'], inplace=True)
    data.drop(data.index[data['leisure'] == 'beach_resort'], inplace=True)
    data.drop(data.index[data['leisure'] == 'bird_hide'], inplace=True)
    data.drop(data.index[data['leisure'] == 'bleachers'], inplace=True)
    data.drop(data.index[data['leisure'] == 'bowling_alley'], inplace=True)
    data.drop(data.index[data['leisure'] == 'common'], inplace=True)
    data.drop(data.index[data['leisure'] == 'dance'], inplace=True)
    data.drop(data.index[data['leisure'] == 'disc_golf_course'], inplace=True)
    data.drop(data.index[data['leisure'] == 'escape_game'], inplace=True)
    data.drop(data.index[data['leisure'] == 'firepit'], inplace=True)
    data.drop(data.index[data['leisure'] == 'fishing'], inplace=True)
    data.drop(data.index[data['leisure'] == 'fitness_centre'], inplace=True)
    data.drop(data.index[data['leisure'] == 'fitness_station'], inplace=True)
    data.drop(data.index[data['leisure'] == 'golf_course'], inplace=True)
    data.drop(data.index[data['leisure'] == 'hackerspace'], inplace=True)
    data.drop(data.index[data['leisure'] == 'horse_riding'], inplace=True)
    data.drop(data.index[data['leisure'] == 'ice_rink'], inplace=True)
    data.drop(data.index[data['leisure'] == 'marina'], inplace=True)
    data.drop(data.index[data['leisure'] == 'miniature_golf'], inplace=True)
    data.drop(data.index[data['leisure'] == 'nature_reserve'], inplace=True)
    data.drop(data.index[data['leisure'] == 'outdoor_seating'], inplace=True)
    data.drop(data.index[data['leisure'] == 'picnic_table'], inplace=True)
    data.drop(data.index[data['leisure'] == 'pitch'], inplace=True)
    data.drop(data.index[data['leisure'] == 'resort'], inplace=True)
    data.drop(data.index[data['leisure'] == 'sauna'], inplace=True)
    data.drop(data.index[data['leisure'] == 'slipway'], inplace=True)
    data.drop(data.index[data['leisure'] == 'summer_camp'], inplace=True)
    data.drop(data.index[data['leisure'] == 'swimming_area'], inplace=True)
    data.drop(data.index[data['leisure'] == 'tanning_salon'], inplace=True)
    data.drop(data.index[data['leisure'] == 'trampoline_park'], inplace=True)
    data.drop(data.index[data['leisure'] == 'water_park'], inplace=True)
    data.drop(data.index[data['leisure'] == 'wildlife_hide'], inplace=True)
    data.drop(data.index[data['leisure'] == 'user defined'], inplace=True)
    # shoppinhg data cleanning
    # food
    data.drop(data.index[data['shop'] == 'alcohol'], inplace=True)
    data.drop(data.index[data['shop'] == 'beverages'], inplace=True)
    data.drop(data.index[data['shop'] == 'brewing_supplies'], inplace=True)
    data.drop(data.index[data['shop'] == 'butcher'], inplace=True)
    data.drop(data.index[data['shop'] == 'cheese'], inplace=True)
    data.drop(data.index[data['shop'] == 'chocolate'], inplace=True)
    data.drop(data.index[data['shop'] == 'coffee'], inplace=True)
    data.drop(data.index[data['shop'] == 'confectionery'], inplace=True)
    data.drop(data.index[data['shop'] == 'dell'], inplace=True)
    data.drop(data.index[data['shop'] == 'ice_cream'], inplace=True)
    data.drop(data.index[data['shop'] == 'pasta'], inplace=True)
    data.drop(data.index[data['shop'] == 'pastry'], inplace=True)
    data.drop(data.index[data['shop'] == 'spices'], inplace=True)
    data.drop(data.index[data['shop'] == 'tea'], inplace=True)
    data.drop(data.index[data['shop'] == 'wine'], inplace=True)
    data.drop(data.index[data['shop'] == 'water'], inplace=True)
    # general store
    data.drop(data.index[data['shop'] == 'kiosk'], inplace=True)
    # clothing, shoes
    data.drop(data.index[data['shop'] == 'bag'], inplace=True)
    data.drop(data.index[data['shop'] == 'boutique'], inplace=True)
    data.drop(data.index[data['shop'] == 'fabric'], inplace=True)
    data.drop(data.index[data['shop'] == 'fashion_accessories'], inplace=True)
    data.drop(data.index[data['shop'] == 'jewelry'], inplace=True)
    data.drop(data.index[data['shop'] == 'leather'], inplace=True)
    data.drop(data.index[data['shop'] == 'sewing'], inplace=True)
    data.drop(data.index[data['shop'] == 'tailor'], inplace=True)
    data.drop(data.index[data['shop'] == 'watches'], inplace=True)
    data.drop(data.index[data['shop'] == 'wool'], inplace=True)
    # discount store
    data.drop(data.index[data['shop'] == 'charity'], inplace=True)
    data.drop(data.index[data['shop'] == 'second_hand'], inplace=True)
    data.drop(data.index[data['shop'] == 'variety_store'], inplace=True)
    # health and beauty
    data.drop(data.index[data['shop'] == 'beauty'], inplace=True)
    data.drop(data.index[data['shop'] == 'chemist'], inplace=True)
    data.drop(data.index[data['shop'] == 'cosmetics'], inplace=True)
    data.drop(data.index[data['shop'] == 'erotic'], inplace=True)
    data.drop(data.index[data['shop'] == 'hairdresser'], inplace=True)
    data.drop(data.index[data['shop'] == 'hairdresser_supply'], inplace=True)
    data.drop(data.index[data['shop'] == 'hearing_aids'], inplace=True)
    data.drop(data.index[data['shop'] == 'herbalist'], inplace=True)
    data.drop(data.index[data['shop'] == 'massage'], inplace=True)
    data.drop(data.index[data['shop'] == 'medical_supply'], inplace=True)
    data.drop(data.index[data['shop'] == 'nutrition_supplements'], inplace=True)
    data.drop(data.index[data['shop'] == 'optician'], inplace=True)
    data.drop(data.index[data['shop'] == 'perfumery'], inplace=True)
    data.drop(data.index[data['shop'] == 'tattoo'], inplace=True)
    # do - it - yourself
    data.drop(data.index[data['shop'] == 'agrarian'], inplace=True)
    data.drop(data.index[data['shop'] == 'appliance'], inplace=True)
    data.drop(data.index[data['shop'] == 'bathroom_furnishing'], inplace=True)
    data.drop(data.index[data['shop'] == 'doityourself'], inplace=True)
    data.drop(data.index[data['shop'] == 'electrical'], inplace=True)
    data.drop(data.index[data['shop'] == 'energy'], inplace=True)
    data.drop(data.index[data['shop'] == 'fireplace'], inplace=True)
    data.drop(data.index[data['shop'] == 'florist'], inplace=True)
    data.drop(data.index[data['shop'] == 'garden_centre'], inplace=True)
    data.drop(data.index[data['shop'] == 'garden_furniture'], inplace=True)
    data.drop(data.index[data['shop'] == 'gas'], inplace=True)
    data.drop(data.index[data['shop'] == 'glaziery'], inplace=True)
    data.drop(data.index[data['shop'] == 'groundskeeping'], inplace=True)
    data.drop(data.index[data['shop'] == 'hardware'], inplace=True)
    data.drop(data.index[data['shop'] == 'houseware'], inplace=True)
    data.drop(data.index[data['shop'] == 'locksmith'], inplace=True)
    data.drop(data.index[data['shop'] == 'paint'], inplace=True)
    data.drop(data.index[data['shop'] == 'pottery'], inplace=True)
    data.drop(data.index[data['shop'] == 'security'], inplace=True)
    data.drop(data.index[data['shop'] == 'trade'], inplace=True)
    # furniture
    data.drop(data.index[data['shop'] == 'antiques'], inplace=True)
    data.drop(data.index[data['shop'] == 'bed'], inplace=True)
    data.drop(data.index[data['shop'] == 'candles'], inplace=True)
    data.drop(data.index[data['shop'] == 'carpet'], inplace=True)
    data.drop(data.index[data['shop'] == 'curtain'], inplace=True)
    data.drop(data.index[data['shop'] == 'doors'], inplace=True)
    data.drop(data.index[data['shop'] == 'flooring'], inplace=True)
    data.drop(data.index[data['shop'] == 'furniture'], inplace=True)
    data.drop(data.index[data['shop'] == 'household_linen'], inplace=True)
    data.drop(data.index[data['shop'] == 'interior_decoration'], inplace=True)
    data.drop(data.index[data['shop'] == 'kitchen'], inplace=True)
    data.drop(data.index[data['shop'] == 'lighting'], inplace=True)
    data.drop(data.index[data['shop'] == 'tiles'], inplace=True)
    data.drop(data.index[data['shop'] == 'window_blind'], inplace=True)
    # Electronlcs
    data.drop(data.index[data['shop'] == 'computer'], inplace=True)
    data.drop(data.index[data['shop'] == 'electronics'], inplace=True)
    data.drop(data.index[data['shop'] == 'hifi'], inplace=True)
    data.drop(data.index[data['shop'] == 'mobile_phone'], inplace=True)
    data.drop(data.index[data['shop'] == 'radiotechnics'], inplace=True)
    data.drop(data.index[data['shop'] == 'telecommunication'], inplace=True)
    data.drop(data.index[data['shop'] == 'vacuum_cleaner'], inplace=True)
    # outdoors
    data.drop(data.index[data['shop'] == 'atv'], inplace=True)
    data.drop(data.index[data['shop'] == 'bicycle'], inplace=True)
    data.drop(data.index[data['shop'] == 'boat'], inplace=True)
    data.drop(data.index[data['shop'] == 'car'], inplace=True)
    data.drop(data.index[data['shop'] == 'car_repair'], inplace=True)
    data.drop(data.index[data['shop'] == 'car_parts'], inplace=True)
    data.drop(data.index[data['shop'] == 'caravan'], inplace=True)
    data.drop(data.index[data['shop'] == 'fuel'], inplace=True)
    data.drop(data.index[data['shop'] == 'fishing'], inplace=True)
    data.drop(data.index[data['shop'] == 'surf'], inplace=True)
    data.drop(data.index[data['shop'] == 'golf'], inplace=True)
    data.drop(data.index[data['shop'] == 'hunting'], inplace=True)
    data.drop(data.index[data['shop'] == 'jetski'], inplace=True)
    data.drop(data.index[data['shop'] == 'military_surplus'], inplace=True)
    data.drop(data.index[data['shop'] == 'motorcycle'], inplace=True)
    data.drop(data.index[data['shop'] == 'outdoor'], inplace=True)
    data.drop(data.index[data['shop'] == 'scuba_diving'], inplace=True)
    data.drop(data.index[data['shop'] == 'ski'], inplace=True)
    data.drop(data.index[data['shop'] == 'snowmobile'], inplace=True)
    data.drop(data.index[data['shop'] == 'sports'], inplace=True)
    data.drop(data.index[data['shop'] == 'swimming_pool'], inplace=True)
    data.drop(data.index[data['shop'] == 'trailer'], inplace=True)
    data.drop(data.index[data['shop'] == 'tyres'], inplace=True)
    # art
    data.drop(data.index[data['shop'] == 'art'], inplace=True)
    data.drop(data.index[data['shop'] == 'camera'], inplace=True)
    data.drop(data.index[data['shop'] == 'collector'], inplace=True)
    data.drop(data.index[data['shop'] == 'craft'], inplace=True)
    data.drop(data.index[data['shop'] == 'frame'], inplace=True)
    data.drop(data.index[data['shop'] == 'games'], inplace=True)
    data.drop(data.index[data['shop'] == 'model'], inplace=True)
    data.drop(data.index[data['shop'] == 'music'], inplace=True)
    data.drop(data.index[data['shop'] == 'musical_instrument'], inplace=True)
    data.drop(data.index[data['shop'] == 'photo'], inplace=True)
    data.drop(data.index[data['shop'] == 'trophy'], inplace=True)
    data.drop(data.index[data['shop'] == 'video'], inplace=True)
    data.drop(data.index[data['shop'] == 'video_games'], inplace=True)
    # stationery
    data.drop(data.index[data['shop'] == 'anime'], inplace=True)
    data.drop(data.index[data['shop'] == 'book'], inplace=True)
    data.drop(data.index[data['shop'] == 'gift'], inplace=True)
    data.drop(data.index[data['shop'] == 'lottery'], inplace=True)
    data.drop(data.index[data['shop'] == 'newsagent'], inplace=True)
    data.drop(data.index[data['shop'] == 'stationery'], inplace=True)
    data.drop(data.index[data['shop'] == 'ticket'], inplace=True)
    # Others
    data.drop(data.index[data['shop'] == 'bookmaker'], inplace=True)
    data.drop(data.index[data['shop'] == 'cannabis'], inplace=True)
    data.drop(data.index[data['shop'] == 'copyshop'], inplace=True)
    data.drop(data.index[data['shop'] == 'dry_cleaning'], inplace=True)
    data.drop(data.index[data['shop'] == 'e-cigarette'], inplace=True)
    data.drop(data.index[data['shop'] == 'funeral_directors'], inplace=True)
    data.drop(data.index[data['shop'] == 'insurance'], inplace=True)
    data.drop(data.index[data['shop'] == 'laundry'], inplace=True)
    data.drop(data.index[data['shop'] == 'money_lender'], inplace=True)
    data.drop(data.index[data['shop'] == 'outpost'], inplace=True)
    data.drop(data.index[data['shop'] == 'party'], inplace=True)
    data.drop(data.index[data['shop'] == 'pawnbroker'], inplace=True)
    data.drop(data.index[data['shop'] == 'pest_control'], inplace=True)
    data.drop(data.index[data['shop'] == 'pet'], inplace=True)
    data.drop(data.index[data['shop'] == 'pet_grooming'], inplace=True)
    data.drop(data.index[data['shop'] == 'pyrotechnics'], inplace=True)
    data.drop(data.index[data['shop'] == 'religion'], inplace=True)
    data.drop(data.index[data['shop'] == 'storage_rental'], inplace=True)
    data.drop(data.index[data['shop'] == 'tobacco'], inplace=True)
    data.drop(data.index[data['shop'] == 'toy'], inplace=True)
    data.drop(data.index[data['shop'] == 'travel_agency'], inplace=True)
    data.drop(data.index[data['shop'] == 'weapons'], inplace=True)
    data.drop(data.index[data['shop'] == 'vacant'], inplace=True)
    data.drop(data.index[data['shop'] == 'user defined'], inplace=True)
    # building data cleanning
    data = data.drop('building', axis=1)

    return data


# combine similar data: 'education' 'healthcare' 'entertainment' 'shopMall'
def combine_samilar_amenities(data):
    # Education
    data.loc[data.index[data['amenity'] == 'childcare'], ['amenity']] = ['education']
    data.loc[data.index[data['amenity'] == 'place_of_worship'], ['amenity']] = ['education']
    data.loc[data.index[data['amenity'] == 'kindergarten'], ['amenity']] = ['education']
    data.loc[data.index[data['amenity'] == 'language_school'], ['amenity']] = ['education']
    data.loc[data.index[data['amenity'] == 'library'], ['amenity']] = ['education']
    data.loc[data.index[data['amenity'] == 'toy_library'], ['amenity']] = ['education']
    data.loc[data.index[data['amenity'] == 'school'], ['amenity']] = ['education']
    data.loc[data.index[data['amenity'] == 'university'], ['amenity']] = ['education']

    # Healthcare
    data.loc[data.index[data['amenity'] == 'clinic'], ['amenity']] = ['healthcare']
    data.loc[data.index[data['amenity'] == 'dentist'], ['amenity']] = ['healthcare']
    data.loc[data.index[data['amenity'] == 'doctors'], ['amenity']] = ['healthcare']
    data.loc[data.index[data['amenity'] == 'hospital'], ['amenity']] = ['healthcare']
    data.loc[data.index[data['amenity'] == 'pharmacy'], ['amenity']] = ['healthcare']

    # entertainment
    data.loc[data.index[data['amenity'] == 'cinema'], ['amenity']] = ['entertainment']
    data.loc[data.index[data['amenity'] == 'community_centre'], ['amenity']] = ['entertainment']
    data.loc[data.index[data['amenity'] == 'conference_centre'], ['amenity']] = ['entertainment']
    data.loc[data.index[data['amenity'] == 'events_venue'], ['amenity']] = ['entertainment']
    data.loc[data.index[data['amenity'] == 'exhibition_centre'], ['amenity']] = ['entertainment']
    data.loc[data.index[data['amenity'] == 'music_venue'], ['amenity']] = ['entertainment']
    data.loc[data.index[data['amenity'] == 'theatre'], ['amenity']] = ['entertainment']
    data.loc[data.index[data['amenity'] == 'police'], ['amenity']] = ['entertainment']
    data.loc[data.index[data['amenity'] == 'social_centre'], ['amenity']] = ['entertainment']

    data.loc[data.index[data['leisure'] == 'playground'], ['leisure']] = ['entertainment']
    data.loc[data.index[data['leisure'] == 'garden'], ['leisure']] = ['entertainment']
    data.loc[data.index[data['leisure'] == 'sports_centre'], ['leisure']] = ['entertainment']
    data.loc[data.index[data['leisure'] == 'sports_hall'], ['leisure']] = ['entertainment']
    data.loc[data.index[data['leisure'] == 'stadium'], ['leisure']] = ['entertainment']
    data.loc[data.index[data['leisure'] == 'swimming_pool'], ['leisure']] = ['entertainment']
    data.loc[data.index[data['leisure'] == 'park'], ['leisure']] = ['entertainment']
    data.loc[data.index[data['leisure'] == 'track'], ['leisure']] = ['entertainment']

    data.loc[data.index[data['amenity'] == 'gym'], ['amenity']] = ['entertainment']

    # shopping_Mall
    data.loc[data.index[data['shop'] == 'department_store'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'wholesale'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'supermarket'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'bakery'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'convenience'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'dairy'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'farm'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'frozen_food'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'greengrocer'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'health_food'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'seafood'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'general'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'mall'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'baby_goods'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'clothes'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'shoes'], ['shop']] = ['shopMall']
    data.loc[data.index[data['shop'] == 'clothes'], ['shop']] = ['shopMall']

    return data


# remove null name rows
def remove_null_name(data):
    return data[data['name'].notna()].reset_index(drop=True)


# remove outlier
def remove_outlier(data):
    X = np.stack([data['lat'], data['lon']], axis=1)
    model = LocalOutlierFactor()
    y = model.fit_predict(X)

    for index, row in data.iterrows():
        if y[index] == -1:
            data.loc[index, ['lat']] = [0]

    data = data[data['lat'] != 0].reset_index(drop=True)

    return data


def store_partial_data(data):
    education_data = data[data['amenity'] == 'education'].reset_index(drop=True)
    healthcare_data = data[data['amenity'] == 'healthcare'].reset_index(drop=True)
    entertainment_data = data[(data['amenity'] == 'entertainment') | (data['leisure'] == 'entertainment')].reset_index(
        drop=True)
    shopping_banking_data = data[data['shop'] == 'shopMall'].reset_index(drop=True)

    education_data.to_csv('data/After/education.csv')
    healthcare_data.to_csv('data/After/healthcare.csv')
    entertainment_data.to_csv('data/After/entertainment.csv')
    shopping_banking_data.to_csv('data/After/shopMall.csv')


def main():
    # print(os.path.exists("./data/total_data.json.gz"))
    data = pd.read_json("./data/transformed_data.json", lines=True)
    # print(data.columns)
    # # print(data['elements'].iloc[0])
    # data = extract_tags(data)
    drop_useless_data = drop_useless_amenities(data)
    combine_samilar_data = combine_samilar_amenities(drop_useless_data)
    not_null_data = remove_null_name(combine_samilar_data)
    not_outlier_data = remove_outlier(not_null_data)

    not_outlier_data.to_csv('data/cleaned_data.csv')
    store_partial_data(not_outlier_data)


if __name__ == '__main__':
    main()
