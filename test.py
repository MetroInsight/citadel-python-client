from citadel import Citadel
import json
import arrow
import traceback

import pdb

with open('config/citadel_config.json', 'r') as fp:
    config = json.load(fp)
apikey = config['apikey']

citadel = Citadel(config['hostname'], apikey, False)

# Create Test
point = {
    'name': 'test_sensor',
    'unit': 'ppm',
    'pointType': 'air_quality'
}

try:
    res = citadel.create_points([point])
    print(res)
except Exception as e:
    if e.reason == 'Existing name':
        pass
    else:
        traceback.print_exc()

# Query Test
res = citadel.query_points({
    'name': 'test_sensor'
})
print(res)
uuid = res[0]

# Get Point Test
res = citadel.get_point(uuid)
print(res)


# decide policy
# TODO


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

