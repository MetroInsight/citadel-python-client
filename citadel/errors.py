class CitadelError(Exception):
#class CitadelError(BaseException):
    def __init__(self, resp=None):
        if resp == None:
            return
        self.status_code = resp.status_code
        self.msg = {}
        self.reason = ''
        self.raw = ''
        try:
            json_resp = resp.json()
            self.reason = json_resp['reason']
            #self.msg['reason'] = json_resp['reason']
        except:
            self.raw = resp.text

    def __str__(self):
        prt = ['status code: {0}'.format(self.status_code)]
        if self.reason:
            prt.append('reason: {0}'.format(self.reason))
        else:
            prt.append('raw error text: {0}'.format(self.raw))
        return '\n'.join(prt)
