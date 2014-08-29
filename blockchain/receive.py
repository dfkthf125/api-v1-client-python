import urllib2
import util
import json

class PaymentResponse:
    def __init__(self, fee, dest, input, callback):
        self.fee = fee
        self.destination_address = dest
        self.input_address = input
        self.callback_url = callback

def receive(dest_addr, callback):
    #util.validate_address(dest_addr)
    #util.validate_url(callback)
    resp = util.call_api("api/receive?method=create&address={0}&callback={1}".format(dest_addr, callback))
    json_resp = json.loads(resp)
    payment_response = PaymentResponse(json_resp['fee_percent'],
                                        json_resp['destination'],
                                        json_resp['input_address'],
                                        json_resp['callback_url'])
    return payment_response
