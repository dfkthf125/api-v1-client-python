"""This module corresponds to functionality documented
at https://blockchain.info/api/blockchain_wallet_api

"""

import util
import json
from .exceptions import *
 
class Wallet:
    """The :class:`Wallet` class mirrors operations listed on the wallet API page.
    It needs to be initialized on a per-wallet basis and will cache the wallet
    identitifer, password, second password and API key (if provided).
    
    """
    
    def __init__(self, identifier, password, second_password = None, api_code = None):
        """Initializes a wallet object.
        
        :param str identifier: wallet identifier (GUID)
        :param str password : decryption password
        :param str second_password: second password (optional)
        :param str api_code: Blockchain.info API code
        """
        
        self.identifier = identifier
        self.password = password
        self.second_password = second_password
        self.api_code = api_code
    
    def send(self, to, amount, from_address = None, shared = False, fee = None, note = None):
        """Send bitcoin from your wallet to a single address.

        :param str to: recipient bitcoin address
        :param int amount: amount to send (in satoshi)
        :param str from_address: specific address to send from (optional)
        :param bool shared: indicating whether the transaction should be sent through
                            a shared wallet (optional)
        :param int fee: transaction fee in satoshi. Must be greater than the default
                        fee (optional).
        :param str note: public note to include with the transaction (optional)
        :return: an instance of :class:`PaymentResponse` class
        """
        
        recipient = { to: amount }
        return self.send_many(recipient, from_address, shared, fee, note)

    def send_many(self, recipients, from_address = None, shared = False, fee = None, note = None):
        """Send bitcoin from your wallet to multiple addresses.

        :param str to: recipient bitcoin address
        :param dictionary recipients: dictionary with the structure of 'address':amount
        :param str from_address: specific address to send from (optional)
        :param bool shared: indicating whether the transaction should be sent through
                            a shared wallet (optional)
        :param int fee: transaction fee in satoshi. Must be greater than the default
                        fee (optional).
        :param str note: public note to include with the transaction (optional)
        :return: an instance of :class:`PaymentResponse` class
        """
        
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
        
    def get_balance(self):
        """Fetch the wallet balance. Includes unconfirmed transactions
        and possibly double spends.
        
        :return: wallet balance in satoshi
        """
        
        response = util.call_api("merchant/{0}/balance".format(self.identifier), self.build_basic_request())
        json_response = json.loads(response)
        self.parse_error(json_response)
        return json_response.get('balance')
    
    def list_addresses(self, confirmations = 0):
        """List all active addresses in the wallet.
        
        :param int confirmations: minimum number of confirmations transactions 
                                    must have before being included in balance of 
                                    addresses (optional)
        :return: an array of :class:`Address` objects
        """
        
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
        
    def get_address_balance(self, address, confirmations = 0):
        """Retrieve the balance of a bitcoin address in the wallet.
        
        :param str address: address in the wallet to look up
        :param int confirmations: minimum number of confirmations transactions 
                                    must have before being included in the balance
                                    (optional)
        :return: an instance of :class:`Address` class
        """
        
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
        """Generate a new address.
        
        :param str label:  label to attach to this address (optional)
        :return: an instance of :class:`Address` class
        """
        
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
        """Archive an address.
        
        :param str address: address to archive
        :return: string representation of the archived address
        """
        
        params = self.build_basic_request()
        params['address'] = address
        response = util.call_api("merchant/{0}/archive_address".format(self.identifier), params)
        json_response = json.loads(response)
        self.parse_error(json_response)
        return json_response['archived']
    
    def unarchive_address(self, address):
        """Unarchive an address.
        
        :param str address: address to unarchive
        :return: string representation of the unarchived address
        """
        
        params = self.build_basic_request()
        params['address'] = address
        response = util.call_api("merchant/{0}/unarchive_address".format(self.identifier), params)
        json_response = json.loads(response)
        self.parse_error(json_response)
        return json_response['active']
        
    def consolidate(self, days):
        """Consolidate the wallet addresses.
        
        :param int days: addresses which have not received any
                            transactions in at least this many days will be consolidated.
        :return: a string array of addresses
        """
        
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
        if self.api_code is not None:
            params['api_code'] = self.api_code
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