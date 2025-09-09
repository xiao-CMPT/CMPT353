import gzip
import shutil
import json

import json

# Load geojson file
with open('./data/total_data.geojson') as f:
    data = json.load(f)

# Save as json
with open('./data/total_data.json', 'w') as f:
    json.dump(data, f)

# Load JSON data
with open('./data/total_data.json') as f:
    data = json.load(f)

# Write data as gzip
with gzip.open('./data/total_data.json.gz', 'wt') as f:
    json.dump(data, f)
