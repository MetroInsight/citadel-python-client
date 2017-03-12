import requests
from copy import deepcopy
import time, random
import json
import pdb

class Citadel():

    def __init__(self, base_url):
        self.base_url = base_url

    def api_url(self):
        return '{0}/api'.format(self.base_url)

    def create_point(self, metadata):
        resp = requests.post(self.api_url() + '/point/', json=metadata)
        if resp.status_code!=201:
            return {'success': False, 
                    'result':{
                        'reason': resp.text
                        }
                    }
        else:
            return {'success': True, 
                    'result':{
                        'uuid': resp.json()['uuid']
                        }
                    }

    def query_points(self, name=None, tag_query=None, geo_query=None):
        params = dict()
        if name:
            params['name'] = name
        if tag_query:
            if not isinstance(tag_query,str):
                tag_query = json.dumps(tag_query)
            params['query'] = tag_query
        if geo_query:
            if not isinstance(geo_query,str):
                geo_query = json.dumps(geo_query)
            params['geo_query'] = geo_query

        resp = requests.get(self.api_url() + '/point', params=params)
        if resp.status_code==200:
            found_point = resp.json()['point_list']
            return {'success': True, 
                    'result':{
                        'point_list':found_point
                        }
                    }
        else:
            return {'success': False, 
                    'result':{
                        'reason': resp.text
                        }
                    }

    def delete_point(self, uuid):
        # delete the uuid
        resp = requests.delete('{0}/point/{1}'.format(self.api_url(), uuid))
        if resp.status_code==200:
            return {'success': True}
        else:
            return {'success': False,
                    'result':{
                        'reason': resp.text
                        }
                    }

    def put_timeseries(self, uuid, ts_data):
        data = {'samples': ts_data}
        ts_url = '{0}/point/{1}/timeseries'.format(self.api_url(), uuid)
        resp = requests.post(ts_url, json=data)
        if resp.status_code==200:
            return {'success':True}
        else:
            return {'success':False,
                    'result':{
                        'reason': resp.text
                        }
                    }

    def get_timeseries(self, uuid, start_time=None, end_time=None):
        params = dict()
        if start_time:
            params['start_time'] = str(int(start_time))
        if end_time:
            params['end_time'] = str(int(end_time))

        ts_url = '{0}/point/{1}/timeseries'.format(self.api_url(), uuid)
        resp = requests.get(ts_url, params=params)
        if resp.status_code==200:
            return {'success': True,
                    'result':{
                        'data': resp.json()['data']
                        }
                    }
        else:
            return {'success': False,
                    'result':{
                        'reason': resp.text
                        }
                    }

    def delete_timeseries(self, uuid, start_time, end_time):
        ts_url = '{0}/point/{1}/timeseries'.format(self.api_url(), uuid)
        params = {
                'start_time': start_time,
                'end_time': end_time
                }
        resp = requests.delete(ts_url, params=params)
        if resp.status_code==200:
            return {'success':True}
        else:
            return {'success':False,
                    'result':{
                        'reason': resp.text
                        }
                    }
