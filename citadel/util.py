import json

def encode_name(name):
    return name.replace(' ', '_')\
               .replace('@', 'at')\
               .replace('/', '_')\
               .replace('&', 'and')\
               .replace('(', '_')\
               .replace(')', '_')\
               .replace('?', '_')
