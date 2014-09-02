import urllib
import urllib2
import re

from .exceptions import *
from validation import validate
from urlparse import urlparse

BASE_URL = "https://blockchain.info/"

def call_api(resource, data = None):
    try:
        #print urllib.urlencode(data)
        return urllib2.urlopen(BASE_URL + resource,
                                None if data is None else urllib.urlencode(data)).read()
    except urllib2.HTTPError as e:
        raise APIException(e.read(), e.code)
    
def validate_address(address):
    if not validate(address):
        raise ValidationException("Invalid bitcoin address")
        
def validate_url(url):
    regex = re.compile(
        r'^(?:[a-z0-9\.\-]*)://' # scheme is validated separately
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}(?<!-)\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if url is None or not regex.search(url):
        raise ValidationException("Invalid URL")