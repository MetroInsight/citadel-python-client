import requests
from copy import deepcopy
import time, random
import json
import pdb

from .errors import CitadelError

class Citadel():

    def __init__(self, base_url, apikey, verify=True):
        self.base_url = base_url
        self.api_url = '{0}/api'.format(self.base_url)
        self.headers = {
            'content-type': 'application/json',
        }
        self.apikey = apikey
        self.verify = verify

    def get_point(self, uuid, headers=None):
        if not headers:
            headers = self.headers
        resp = requests.get(self.api_url + '/point/{0}'.format(uuid),
                            headers=headers, verify=self.verify)
        if resp.status_code in [400, 500]:
            raise CitadelError(resp)
        return resp.json()['results'][0]
    
    def upsert_metadata(self, uuid, metadata, headers=None):
        if not headers:
            headers = self.headers
        body = {}
        body['metadata'] = metadata
        body['userToken'] = self.apikey
        resp = requests.post(self.api_url + '/point/' + uuid, 
                             json=body, 
                             headers=self.headers, verify=self.verify)
        if resp.status_code in [400, 500]:
            err = CitadelError(resp)
            raise err
        resp_json = resp.json()
        if resp.status_code!=200:
            return {'success': False, 
                    'reason': resp_json['reason']
                   }
        else:
            return True

    def create_point(self, metadata, headers=None):
        if not headers:
            headers = self.headers
        body = {}
        body['point'] = metadata
        body['userToken'] = self.apikey
        resp = requests.post(self.api_url + '/point', 
                             json=body, 
                             headers=self.headers, verify=self.verify)
        if resp.status_code in [400, 500]:
            err = CitadelError(resp)
            raise err
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
        resp = requests.post(query_url, json=query, 
                             headers=headers, verify=self.verify)
        if resp.status_code in [400, 500]:
            raise CitadelError(resp)
        points = resp.json()['results']
        return points

    def post_data(self, data, headers=None):
        if not headers:
            headers = self.headers
        data_url = self.api_url + '/data'
        body = {
            'data': data,
            'userToken': self.apikey
        }
        resp = requests.post(data_url, json=body, headers=headers,
                             verify=self.verify)
        if resp.status_code in [400, 500]:
            raise CitadelError(resp)
        elif resp.status_code in [200, 201]:
            return resp.json()['success']
        else:
            return False

    def get_data(self, uuid, start_time=None, end_time=None,
                       headers=None):
        if not headers:
            headers = self.headers
        query = {
                    'query': {},
                    'userToken': self.apikey
                }
        if start_time:
            query['query']['timestamp_min'] = start_time
        if end_time:
            query['query']['timestamp_max'] = end_time
        query['query']['uuids'] = [uuid]
        resp = requests.post(self.api_url + '/querydata',
                             json=query, 
                             headers=self.headers,
                             verify=self.verify)
        if resp.status_code in [400, 500]:
            raise CitadelError(resp)
        return resp.json()['results']


    def query_bbox(self, begin_time=None, end_time=None, min_lng=None,
                   min_lat=None, max_lng=None, max_lat=None, uuids=[]):
        """
        begin_time timestamp (ms) in long (in python just int)
        end_time timestamp (ms) in long
        min_lng float
        min_lat float
        max_lng float
        max_lat float
        uuids [str]
        """
        query = {}
        if begin_time:
            query['timestamp_min'] = begin_time
        if end_time:
            query['timestamp_max'] = end_time
        if min_lng:
            query['min_lng'] = min_lng
        if min_lat:
            query['min_lat'] = min_lat
        if max_lng:
            query['max_lng'] = max_lng
        if max_lat:
            query['max_lat'] = max_lat
        if uuids:
            query['uuids'] = uuids
        body = {
            'query': query,
            'userToken': self.apikey
        }
        resp = requests.post(self.api_url + '/querydata', 
                             json=body, 
                             headers=self.headers, verify=self.verify)
        if resp.status_code != 200:
            raise CitadelError(resp)
        return resp.json()['results']

    def register_policy(self, sensors, users):
        body = {}
        body['userToken'] = self.apikey
        policy = {
            'sensors': sensors,
            'users': users
        }
        body['policy'] = policy
        resp = requests.post(self.api_url + '/registerPolicy',
                             json=body, 
                             headers=self.headers,
                             verify=self.verify)
        if resp.status_code != 200:
            raise CitadelError(resp)
        return resp.json()['success']

    def delete_timeseries(self, uuid, start_time, end_time):
        # TODO
        pass
