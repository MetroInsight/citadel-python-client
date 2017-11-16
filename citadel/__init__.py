import requests
from copy import deepcopy
import time, random
import json
import pdb

from .errors import CitadelError

class Citadel():

    def __init__(self, base_url):
        self.base_url = base_url
        self.api_url = '{0}/api'.format(self.base_url)
        self.headers = {
            'content-type': 'application/json',
        }

    def get_point(self, uuid, headers=None):
        if not headers:
            headers = self.headers
        resp = requests.get(self.api_url + '/point/{0}'.format(uuid),
                            headers=headers)
        if resp.status_code in [400, 500]:
            raise CitadelError(resp)
        return resp.json()['results']

    def create_point(self, metadata, headers=None):
        if not headers:
            headers = self.headers
        resp = requests.post(self.api_url + '/point', 
                             json=metadata, 
                             headers=self.headers)
        if resp.status_code in [400, 500]:
            raise CitadelError(resp)
        resp_json = resp.json()
        if resp.status_code!=201:
            return {'success': False, 
                    'reason': resp_json['reason']
                   }
        else:
            return resp_json['uuid']

    def query_points(self, query, headers=None):
        if not headers:
            headers = self.headers
        query = {'query': query}
        query_url = self.api_url + '/query'
        resp = requests.post(query_url, json=query, headers=headers)
        if resp.status_code in [400, 500]:
            raise CitadelError(resp)
        points = resp.json()['results']
        return points

    def post_data(self, data, headers=None):
        if not headers:
            headers = self.headers
        data_url = self.api_url + '/data'
        resp = requests.post(data_url, json={'data': data}, headers=headers)
        if resp.status_code in [400, 500]:
            raise CitadelError(resp)
        elif resp.status_code in [200, 201]:
            return resp.json()['success']
        else:
            return False

    def query_data(self, uuid, start_time=None, end_time=None,
                       headers=None):
        if not headers:
            headers = self.headers
        query = {'query': {}}
        if start_time:
            query['query']['timestamp_min'] = start_time
        if end_time:
            query['query']['timestamp_max'] = end_time
        resp = requests.post(self.api_url + '/querydata',
                             json=query, 
                             headers=self.headers)
        if resp.status_code in [400, 500]:
            raise CitadelError(resp)
        return resp.json()['results']


    def query_bbox(self, begin_time, end_time, min_lng,
                   min_lat, max_lng, max_lat):
        pass

    def delete_timeseries(self, uuid, start_time, end_time):
        # TODO
        pass
