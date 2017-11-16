class CitadelError(BaseException):
    def __init__(self, resp=None):
        if resp == None:
            return
        self.status_code = resp.status_code
        self.msg = {}
        try:
            json_resp = resp.json()
            self.msg['reason'] = json_resp['reason']
        except:
            self.msg['raw'] = resp.text

    def __str__(self):
        prt = ['status code: {0}'.format(self.status_code)]
        if 'reason' in self.msg:
            prt.append('Reason: {0}'.format(self.msg['reason']))
        else:
            prt.append('Raw Error Text: {0}'.format(self.msg['raw']))
        return '\n'.join(prt)
