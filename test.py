from citadel import Citadel
import json
import arrow
import traceback
import sys
import pdb
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open('config/citadel_config_local.json', 'r') as fp:
    config = json.load(fp)
apikey = config['apikey']

citadel = Citadel(config['hostname'], apikey, False)

point = config['point']

# Create Test
try:
    res = citadel.create_point(point)
    if res:
        print('Success: Point Creation')
    else:
        print('Failed: Point creation due to {0}')
except Exception as e:
    if e.reason == 'Existing name':
        pass
    else:
        traceback.print_exc()
        sys.exit()

# Query Test
res = citadel.query_points({
    'name': point['name']
})
if res:
    uuid = res[0]
    print('Success: Point query')
else:
    print('Failed: Empty point query')
    sys.exit()

# Get Point Test
res = citadel.get_point(uuid)
if uuid:
    print('Success: Get point', res)
else:
    print('Failed: Get point')

# Post Data Test
datapoint = config['datapoint']
t = datapoint['timestamp']
datapoint['uuid'] = uuid
data = [datapoint]
res = citadel.post_data(data)
assert res
if res:
    print('Success: post data')
else:
    print('Failed: post data')

# Get Data from a UUID
data = citadel.get_data(uuid, None, None)
if data:
    print(data)
    print("Success: retrieve data only with a UUID")
else:
    print('Failed: empty result')

begin_time = t - 1000000
end_time = t + 1000000
#min_lng = -120
#min_lat = 30
#max_lng = -110
#max_lat = 35
min_lng = -117.0848
max_lng = -116.98368
min_lat = 32.621090
max_lat = 33.623620
uuids = [uuid]
res = citadel.query_bbox(begin_time, end_time, min_lng, 
                         min_lat, max_lng, max_lat, uuids)
if res:
    print(res)
    print("Success: retrieve data with BBOX query")
else:
    print('Failed')
