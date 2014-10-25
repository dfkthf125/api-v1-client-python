from .exceptions import *
import sys

BASE_URL = "https://blockchain.info/"

py_version = sys.version_info[0]
if py_version >= 3:
    # Python 3.0 and later
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from urllib.parse import urlencode
else:
    # Python 2.x
    from urllib2 import urlopen
    from urllib2 import HTTPError
    from urllib import urlencode

def call_api(resource, data = None):
    try:
        payload = None if data is None else urlencode(data)
        if py_version >= 3 and payload is not None: payload = payload.encode('UTF-8')
        response = urlopen(BASE_URL + resource, payload).read()
        return handle_response(response)
            
    except HTTPError as e:
        raise APIException(handle_response(e.read()), e.code)

def handle_response(response):
    #urllib returns different types in Python 2 and 3 (str vs bytes)
    if isinstance(response, str):
        return response
    else:
        return response.decode('utf-8')
