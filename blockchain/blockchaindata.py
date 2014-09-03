import util
import json

def get_block(block_idx = None, block_hash = None, api_code = None):
    resource = 'rawblock/'
    if block_hash is not None:
        resource += block_hash
    elif block_idx is not None:
        resource += block_idx
    if api_code is not None:
        resource += '?api_code=' + api_code
        
    response = util.call_api(resource)
    json_response = json.loads(response)
    print json_response
    #TODO

    
def parse_input(i):
    obj = i['prev_out']
    return Input(obj['n'], obj['value'], obj['addr'], obj['tx_index'], obj['type'], obj['script'])
    
def parse_output(o):
    return Output(o['n'], o['value'], o['addr'], o['tx_index'], o['type'], o['script'], o['spent'])

class Input:
        def __init__(self, n, value, address, tx_index, type, script):
            self.n = n
            self.value = value
            self.address = address
            self.tx_index = tx_index
            self.type = type
            self.script = script

class Output:
        def __init__(self, n, value, address, tx_index, type, script, spent):
            self.n = n
            self.value = value
            self.address = address
            self.tx_index = tx_index
            self.type = type
            self.script = script
            self.spent = spent
        
class Transaction:
    def __init__(self, double_spend, block_height, time, vout_sz, vin_sz,
                    relayed_by, hash, tx_index, version, inputs, outputs):
        self.double_spend = double_spend
        self.block_heigh = block_height
        self.time = time
        self.vout_sz = vout_sz
        self.vin_sz = vin_sz
        self.relayed_by = relayed_by
        self.hash = hash
        self.tx_index = tx_index
        self.version = version
        self.inputs = inputs
        self.outputs = outputs
        
class Block:
    def __init__(self, hash, version, previous_block, merkle_root, time,
                    bits, fee, nonce, n_tx, size, block_index, main_chain,
                    height, received_time, relayed_by, transactions):
        self.hash = hash
        self.version = version
        self.previous_block = previous_block
        self.merkle_root = merkle_root
        self.time = time
        self.bits = bits
        self.fee = fee
        self.nonce = noce
        self.n_tx = n_tx
        self.size = size
        self.block_index = block_index
        self.main_chain = main_chain
        self.height = height
        self.received_time = received_time
        self.relayed_by = relayed_by
        self.transactions = transactions
        