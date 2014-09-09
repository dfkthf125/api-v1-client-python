import urllib
import urllib2

from .exceptions import *
from validation import validate
from urlparse import urlparse

BASE_URL = "https://blockchain.info/"

def call_api(resource, data = None):
    try:
        return urllib2.urlopen(BASE_URL + resource,
                                None if data is None else urllib.urlencode(data)).read()
    except urllib2.HTTPError as e:
        raise APIException(e.read(), e.code)