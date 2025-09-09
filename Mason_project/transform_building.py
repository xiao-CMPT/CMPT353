import json


def transform_json_file(input_filename, output_filename):
    with open(input_filename) as f:
        json_data = json.load(f)

    with open(output_filename, 'w') as f:

        for element in json_data['elements']:

            if element['type'] == 'way' and 'tags' in element:

                node_id = element['nodes'][0]

                node_element = next((n for n in json_data['elements'] if n['type'] == 'node' and n['id'] == node_id),
                                    None)

                if node_element:
                    new_element = {
                        'lat': node_element['lat'],
                        'lon': node_element['lon'],
                        'timestamp': json_data['osm3s']['timestamp_osm_base'],
                        'building': element['tags'].get('building'),
                        'name': element['tags'].get('name'),
                        'tags': element['tags']
                    }

                    json.dump(new_element, f)

                    f.write('\n')


transform_json_file('./data/Building.json', './data/transformed_building_data.json')
