from citadel import Citadel
import json
import arrow
import traceback
import sys

import pdb

with open('config/citadel_config.json', 'r') as fp:
    config = json.load(fp)
apikey = config['apikey']

citadel = Citadel(config['hostname'], apikey, True)

# Create Test
point = {
    'name': 'test_sensor6',
    'unit': 'ppm',
    'pointType': 'air_quality'
}

try:
    res = citadel.create_points([point])
    print(res)
except Exception as e:
    #pdb.set_trace()
    if e.reason == 'Existing name':
        pass
    else:
        traceback.print_exc()
        sys.exit()
#pdb.set_trace()

# Query Test
res = citadel.query_points({
    'name': point['name']
})
print(res)
uuid = res[0]
#pdb.set_trace()

# Get Point Test
res = citadel.get_point(uuid)
print(res)
#pdb.set_trace()

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
#pdb.set_trace()


# Get Data from a UUID
#uuid = "744071ce-dc56-4798-9d25-397ce2df9baf"
data = citadel.get_data(uuid, None, None)
#pdb.set_trace()
if data:
    print("Success")
else:
    print('Failed: empty result')
