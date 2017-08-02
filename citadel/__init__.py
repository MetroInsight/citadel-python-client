import requests
from copy import deepcopy
import time, random
import json
import pdb

class Citadel():

    def __init__(self, base_url):
        self.base_url = base_url
        self.api_url = '{0}/api'.format(self.base_url)
        self.headers = {
            'content-type': 'application/json',
        }

    def create_point(self, metadata):
        resp = requests.post(self.api_url() + '/point/', 
                             json=metadata, 
                             headers=headers)
        if resp.statuc_code in [400, 500]:
            #TODO: define better behavior
            return False
        resp = resp.json()
        if resp.status_code!=201:
            return {'success': False, 
                    'reason': resp['reason']
                   }
        else:
            return resp['uuid']

    def query_points(self, query):
        query = {'query': query}
        resp = requests.post(query_url, json=query, headers=headers)
        pdb.set_trace()
        points = resp.json()['results']
        return points


    def delete_point(self, uuid):
        #TODO

    def post_data(data, headers=headers):
        resp = requests.post(data_url, json={'data': data}, headers=headers)
        return resp.json()['success']

    def get_timeseries(self, uuid, start_time=None, end_time=None):
        # TODO

    def delete_timeseries(self, uuid, start_time, end_time):
        # TODO
