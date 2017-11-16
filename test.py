from citadel import Citadel
import json
import arrow

import pdb

with open('config/citadel_config.json', 'r') as fp:
    config = json.load(fp)

citadel = Citadel(config['hostname'])

# Create Test
point = {
    'name': 'test_sensor',
    'unit': 'ppm',
    'pointType': 'air_quality'
}

#res = citadel.create_point(point)
#print(res)

# Query Test
res = citadel.query_points({
    'unit': 'ppm'
})
print(res)
uuid = res[0]

# Get Point Test
res = citadel.get_point(uuid)
print(res)


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
data = citadel.query_data(uuid, None, None)
pdb.set_trace()




