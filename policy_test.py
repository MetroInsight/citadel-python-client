from citadel import Citadel
import json
import arrow
import traceback
import sys
import pdb
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open('config/citadel_config.json', 'r') as fp:
    config = json.load(fp)
apikey = config['apikey']

citadel = Citadel(config['hostname'], apikey, False)

point = {
    'name': 'test_sensor7',
    'unit': 'ppm',
    'pointType': 'air_quality'
}

# Query Test
res = citadel.query_points({
    'name': point['name']
})
uuid = res[0]
if uuid:
    print('Success: Point query')
else:
    print('Failed: Point query due to {0}')


# decide policy
citadel.register_policy([uuid], ['bk7749@gmail.com'])

if res:
    print("Success: register a policy")
else:
    print('Failed: register a policy')
