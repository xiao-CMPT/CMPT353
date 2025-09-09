import json


def transform_json_file(input_filename, output_filename):
    with open(input_filename) as f:
        json_data = json.load(f)

    with open(output_filename, 'w') as f:

        for element in json_data['elements']:

            if element['type'] == 'node' and 'tags' in element:
                new_element = {
                    'lat': element['lat'],
                    'lon': element['lon'],
                    'timestamp': json_data['osm3s']['timestamp_osm_base'],
                    'amenity': element['tags'].get('amenity'),
                    'shop': element['tags'].get('shop'),
                    'leisure': element['tags'].get('leisure'),
                    'building': element['tags'].get('building'),
                    'name': element['tags'].get('name'),
                    'tags': element['tags']
                }

                json.dump(new_element, f)

                f.write('\n')


transform_json_file('./data/total_data.json', './data/transformed_data.json')
