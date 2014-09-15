"""This module corresponds to functionality documented
at https://blockchain.info/api/api_receive
"""

import urllib2
import util
import json

class ReceiveResponse:

    def __init__(self, fee_percent, dest, input, callback):
        self.fee_percent = fee_percent
        self.destination_address = dest
        self.input_address = input
        self.callback_url = callback

def receive(dest_addr, callback, api_code = None):
    """Call the 'api/receive' endpoint and create a forwarding address.
    
    :param str dest_addr: destination address where the payment should be sent
    :param str callback: callback URI that will be called upon payment
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`ReceiveResponse` class
    """
    
    params = { 'method': 'create', 'address': dest_addr, 'callback': callback }
    if api_code is not None:
        params['api_code'] = api_code
    resp = util.call_api('api/receive', params)
    json_resp = json.loads(resp)
    payment_response = ReceiveResponse(json_resp['fee_percent'],
                                        json_resp['destination'],
                                        json_resp['input_address'],
                                        json_resp['callback_url'])
    return payment_response
