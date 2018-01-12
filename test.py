from citadel import Citadel
import json
import arrow

import pdb

with open('config/citadel_config.json', 'r') as fp:
    config = json.load(fp)
apikey = config['apikey']

citadel = Citadel(config['hostname'], apikey)

# Create Test
point = {
    'name': 'test_sensor',
    'unit': 'ppm',
    'pointType': 'air_quality'
}

res = citadel.create_point(point)
print(res)
"""

# Query Test
res = citadel.query_points({
    'name': 'test_sensor'
})
print(res)
uuid = res[0]

# Get Point Test
#res = citadel.get_point(uuid)
#print(res)


# Post Data Test
t = 1510791536000
data = [
    {
        'geometryType': 'point',
        'coordinates': [[-117.0, 33.0]],
        'uuid': uuid,
        'value': 90,
        'timestamp': t
    }
]
resp = citadel.post_data(data)
assert resp

# Get Data from a UUID
#uuid = "744071ce-dc56-4798-9d25-397ce2df9baf"
data = citadel.get_data(uuid, None, None)
pdb.set_trace()


# Data Query
"""
