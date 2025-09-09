import gzip
import shutil
import json

# Load JSON data
data = []
with open('./data/transformed_data.json') as f:
    for line in f:
        data.append(json.loads(line))
# Write data as gzip
with gzip.open('./data/transformed_data.json.gz', 'wt') as f:
    json.dump(data, f)

