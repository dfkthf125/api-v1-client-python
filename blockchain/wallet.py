"""The wallet module corresponds to the API functionality documented
at https://blockchain.info/api/blockchain_wallet_api

"""
import util
import json
from .exceptions import *
 
class Wallet:
    """The Wallet class mirrors operations listed on the wallet API page.
    It needs to be initialized on a per-wallet basis and will cache the wallet
    identitifer, password and second password (if provided).
    
    """
    
    def __init__(self, identifier, password, second_password = None):
        """Initializes a wallet object.
        
        Parameters
        ----------
        identifier : string
            Wallet identifier (GUID)
        password : string
            Decryption password. Required.
        second_password : string
            Second password. Optional.
        
        """
        self.identifier = identifier
        self.password = password
        self.second_password = second_password
    
    def send(self, to, amount, from_address = None, shared = False, fee = None, note = None):
        """
        TODO
        
        """
        recipient = { to: amount }
        return self.send_many(recipient, from_address, shared, fee, note)

    def send_many(self, recipients, from_address = None, shared = False, fee = None, note = None):
        params = self.build_basic_request()
        method = ''
        
        if len(recipients) == 1:
            to_address, amount = recipients.popitem()
            params['to'] = to_address
            params['amount'] = amount
            method = 'payment'
        else:
            params[''] = json.dumps(recipients)
            method = 'sendmany'
        
        if from_address is not None:
            params['from'] = from_address
        if shared is True:
            params['shared'] = 'true'
        if fee is not None:
            params['fee'] = fee
        if note is not None:
            params['note'] = note
        if self.second_password is not None:
            params['second_password'] = self.second_password
            
        response = util.call_api("merchant/{0}/{1}".format(self.identifier, method), params)
        json_response = json.loads(response)
        
        self.parse_error(json_response)
        payment_response = PaymentResponse(
                                            json_response['message'],
                                            json_response['tx_hash'],
                                            json_response.get('notice'))
        return payment_response
        
    def balance(self):
        response = util.call_api("merchant/{0}/balance".format(self.identifier), self.build_basic_request())
        json_response = json.loads(response)
        self.parse_error(json_response)
        return json_response.get('balance')
    
    def list_addresses(self, confirmations = 0):
        params = self.build_basic_request()
        params['confirmations'] = confirmations
        response = util.call_api("merchant/{0}/list".format(self.identifier), params)
        json_response = json.loads(response)
        self.parse_error(json_response)
        
        addresses = []
        for a in json_response['addresses']:
            address = Address(a['balance'], a['address'], a['label'], a['total_received'])
            addresses.append(address)
            
        return addresses
        
    def address_balance(self, address, confirmations = 0):
        params = self.build_basic_request()
        params['address'] = address
        params['confirmations'] = confirmations
        response = util.call_api("merchant/{0}/address_balance".format(self.identifier), params)
        json_response = json.loads(response)
        self.parse_error(json_response)
        return Address(json_response['balance'],
                        json_response['address'],
                        None,
                        json_response['total_received'])
    
    def new_address(self, label = None):
        params = self.build_basic_request()
        if label is not None:
            params['label'] = label
        response = util.call_api("merchant/{0}/new_address".format(self.identifier), params)
        json_response = json.loads(response)
        self.parse_error(json_response)
        return Address(0,
                        json_response['address'],
                        json_response['label'],
                        0)
                        
    def archive_address(self, address):
        params = self.build_basic_request()
        params['address'] = address
        response = util.call_api("merchant/{0}/archive_address".format(self.identifier), params)
        json_response = json.loads(response)
        self.parse_error(json_response)
        return json_response['archived']
    
    def unarchive_address(self, address):
        params = self.build_basic_request()
        params['address'] = address
        response = util.call_api("merchant/{0}/unarchive_address".format(self.identifier), params)
        json_response = json.loads(response)
        self.parse_error(json_response)
        return json_response['active']
        
    def consolidate(self, days):
        params = self.build_basic_request()
        params['days'] = days
        response = util.call_api("merchant/{0}/auto_consolidate".format(self.identifier), params)
        json_response = json.loads(response)
        self.parse_error(json_response)
        return json_response['consolidated']
    
    def build_basic_request(self):
        params = { 'password': self.password }
        if self.second_password is not None:
            params['second_password'] = self.second_password
        return params
        
    def parse_error(self, json_response):
        error = json_response.get('error')
        if error is not None:
            raise APIException(error, 0)
            
class PaymentResponse:
    
    def __init__(self, message, tx_hash, notice):
        self.message = message
        self.tx_hash = tx_hash
        self.notice = notice
        
class Address:
    def __init__(self, balance, address, label, total_received):
        self.balance = balance
        self.address = address
        self.label = label
        self.total_received = total_received