import json
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from geopy.distance import geodesic


def is_within_radius(lat1, lon1, lat2, lon2, radius_km):
    distance = geodesic((lat1, lon1), (lat2, lon2)).kilometers
    return distance <= radius_km


def load_building_data(input_filename):
    with open(input_filename) as f:
        building_data = [json.loads(line) for line in f]
    building_df = pd.DataFrame(building_data)
    building_gdf = gpd.GeoDataFrame(
        building_df, geometry=gpd.points_from_xy(building_df.lon, building_df.lat))
    building_gdf.set_crs(epsg=4326, inplace=True)
    building_gdf = building_gdf.to_crs(epsg=3395)
    return building_gdf


def load_csv_data(input_filename):
    data_df = pd.read_csv(input_filename)
    data_gdf = gpd.GeoDataFrame(
        data_df, geometry=gpd.points_from_xy(data_df.lon, data_df.lat))
    data_gdf.set_crs(epsg=4326, inplace=True)
    data_gdf = data_gdf.to_crs(epsg=3395)
    return data_gdf


def update_scores(building_gdf, csv_gdf, score_increment, radius_km):
    for i in building_gdf.index:
        building_circle = building_gdf.loc[i, 'geometry'].buffer(radius_km * 1000)
        indices = list(csv_gdf.sindex.intersection(building_circle.bounds))
        if len(indices) > 0:
            building_gdf.loc[i, 'score'] += score_increment * len(indices)


def analyze_building_scores(building_data, education_data, healthcare_data, entertainment_data, shopMall_data):
    building_data['score'] = 0

    update_scores(building_data, education_data, 3, 2)
    update_scores(building_data, healthcare_data, 3, 2)
    update_scores(building_data, entertainment_data, 2, 2)
    update_scores(building_data, shopMall_data, 1, 2)

    building_data = building_data[building_data['score'] >= 50]

    return building_data


def plot_scores(building_data):
    colors = []
    for _, building in building_data.iterrows():
        score = building['score']
        if score > 200:
            colors.append('red')
        elif score > 150:
            colors.append('yellow')
        elif score > 100:
            colors.append('blue')
        else:
            colors.append('green')

    plt.scatter(building_data['lon'], building_data['lat'], color=colors)
    plt.show()


if __name__ == "__main__":
    print("Loading building data...")
    building_data = load_building_data('./data/Building.json')
    print("Building data loaded.")

    print("Loading education data...")
    education_data = load_csv_data('./data/After/education.csv')
    print("Education data loaded.")

    print("Loading healthcare data...")
    healthcare_data = load_csv_data('./data/After/healthcare.csv')
    print("healthcare data loaded.")

    print("Loading entertainment data...")
    entertainment_data = load_csv_data('./data/After/entertainment.csv')
    print("entertainment data loaded.")

    print("Loading shopMall data...")
    shopMall_data = load_csv_data('./data/After/shopMall.csv')
    print("shopMall data loaded.")

    print("Analyzing building scores...")
    building_data = analyze_building_scores(building_data, education_data, healthcare_data, entertainment_data,
                                            shopMall_data)
    print("Score analysis completed.")

    print("Plotting scores...")
    plot_scores(building_data)
    print("Scores plotted.")

    print("Generating map...")

    center_lat = building_data['lat'].mean()
    center_lon = building_data['lon'].mean()

    m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    for _, building_data in building_data.iterrows():
        if building_data['score'] > 200:
            color = 'red'
        elif building_data['score'] > 150:
            color = 'orange'
        elif building_data['score'] > 100:
            color = 'blue'
        else:
            color = 'green'

        folium.CircleMarker(
            location=(building_data['lat'], building_data['lon']),
            radius=building_data['score'] / 100,
            color=color,
            fill=True,
            fill_color=color,
            popup=f"Score: {building_data['score']}",
        ).add_to(m)
    print("Map generated.")

    m.save('./result/result_map.html')
