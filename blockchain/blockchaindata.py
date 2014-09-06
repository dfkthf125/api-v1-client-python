import util
import json

def get_block(block_id, api_code = None):
    resource = 'rawblock/' + block_id
    if api_code is not None:
        resource += '?api_code=' + api_code
        
    response = util.call_api(resource)
    json_response = json.loads(response)
    return parse_block(json_response)

def get_tx(tx, api_code = None):
    resource = 'rawtx/' + tx
    if api_code is not None:
        resource += '?api_code=' + api_code
        
    response = util.call_api(resource)
    json_response = json.loads(response)
    return parse_tx(json_response)
    
def parse_input(i):
    obj = i.get('prev_out')
    if obj is not None:
        # regular TX
        return Input(obj['n'], obj['value'], obj['addr'], obj['tx_index'], obj['type'],
                    obj['script'], i['script'], i['sequence'])
    else:
        # coinbase TX
        return Input(None, None, None, None, None, None, i['script'], i['sequence'])
    
def parse_output(o):
    return Output(o['n'], o['value'], o['addr'], o['tx_index'], o['type'], o['script'], o['spent'])

def parse_tx(t):
    ins = [parse_input(i) for i in t['inputs']]
    outs = [parse_output(o) for o in t['out']]
    return Transaction(t.get('double_spend', False), t.get('block_height'), t['time'], t['vout_sz'], t['vin_sz'],
                        t['relayed_by'], t['hash'], t['tx_index'], t['ver'], t['size'], ins, outs)

def parse_block(b):
    block_height = b['height']
    txs = [parse_tx(t) for t in b['tx']]
    for tx in txs:
        tx.block_height = block_height
    return Block(b['hash'], b['ver'], b['prev_block'], b['mrkl_root'], b['time'], b['bits'],
                    b['fee'], b['nonce'], b['n_tx'], b['size'], b['block_index'], b['main_chain'],
                    b['height'], b['received_time'], b['relayed_by'], txs)
    
class Input:
        def __init__(self, n, value, address, tx_index, type, script, script_sig, sequence):
            self.n = n
            self.value = value
            self.address = address
            self.tx_index = tx_index
            self.type = type
            self.script = script
            self.script_sig = script_sig
            self.sequence = sequence

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
                    relayed_by, hash, tx_index, version, size, inputs, outputs):
        self.double_spend = double_spend
        self.block_height = block_height
        self.time = time
        self.vout_sz = vout_sz
        self.vin_sz = vin_sz
        self.relayed_by = relayed_by
        self.hash = hash
        self.tx_index = tx_index
        self.version = version
        self.size = size
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
        self.nonce = nonce
        self.n_tx = n_tx
        self.size = size
        self.block_index = block_index
        self.main_chain = main_chain
        self.height = height
        self.received_time = received_time
        self.relayed_by = relayed_by
        self.transactions = transactions
        