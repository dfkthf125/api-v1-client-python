##`blockexplorer` module
All functions support an optional parameter called `api_code`. It won't be listed with every function description.

####`get_block`
Get a single block based on a block index or hash. Returns a `Block` object.

Params: 
```
block_id : str - block index or hash
```

Usage:
```python
from blockchain import blockexplorer

block = blockexplorer.get_block('000000000000000016f9a2c3e0f4c1245ff24856a79c34806969f5084f410680')
```

####`get_transaction`
Get a single transaction based on a transaction index or hash. Returns a `Transaction` object.

Params:
```
tx_id : str - transaction index or hash
```

Usage:
```python
tx = blockexplorer.get_transaction('d4af240386cdacab4ca666d178afc88280b620ae308ae8d2585e9ab8fc664a94')
```

####`get_block_height`
Get an array of blocks at the specified height. Returns an array of `Block` objects.

Params:
```
height : int - block height
```

Usage:
```python
blocks = blockexplorer.get_block_height(2570)
```

####`get_address`
Get a single address and its transactions. Returns an `Address` object.

Params:
```
address : str - address in the base58 or hash160 format
```

Usage:
```python
address = blockexplorer.get_address('1HS9RLmKvJ7D1ZYgfPExJZQZA1DMU3DEVd')
```

####`get_unspent_outputs`
Get an array of unspent outputs for an address. Returns an array of `UnspentOutput` objects.

Params:
```
address : str - address in the base58 or hash160 format
```

Usage:
```python
outs = blockexplorer.get_unspent_outputs('1HS9RLmKvJ7D1ZYgfPExJZQZA1DMU3DEVd')
```

####`get_latest_block`
Get the latest block on the main chain. Returns a `LatestBlock` object.

Usage:
```python
latest_block = blockexplorer.get_latest_block()
```

####`get_unconfirmed_tx`
Get a list of currently unconfirmed transactions. Returns an array of `Transaction` objects.

Usage:
```python
txs = blockexplorer.get_unconfirmed_tx()
```

####`get_blocks`
Get a list of blocks for a specific day or mining pool. Returns an array of `SimpleBlock` objects.

Params:
```
time : int - unix time in ms (optional)
pool_name : str - pool name (optional)
```
At least one parameter is required.

Usage:
```python
blocks = blockexplorer.get_blocks(pool_name = 'Discus Fish')
```

####`get_inventory_data`
Get inventory data for recent blocks and addresses (up to 1 hour old). Returns an `InventoryData` object.

Params:
```
hash : str - tx or block hash
```

Usage:
```python
inv = blockexplorer.get_inventory_data('d4af240386cdacab4ca666d178afc88280b620ae308ae8d2585e9ab8fc664a94')
```

###Response object field definitions

####`Block`

```
hash : str
version : int
previous_block (str
merkle_root :str
time : int
bits : int
fee : int
nonce int
t_tx : int
size : int
block_index : int
main_chain : bool
height : int
received_time : int
relayed_by : string
transactions : array of Transaction objects
```

####`Transaction`

```
double_spend : bool
block_height : int (if -1, the tx is unconfirmed)
time : int
relayed_by : str
hash : str
tx_index : int
version : int
size : int
inputs : array of Input objects
outputs: array of Output objects
```

####`Input`

```
n : int
value : int
address : str
tx_index : int
type : int
script : str
script_sig : str
sequence : int
```

Note: if coinbase transaction, then only `script` and `script_siq` will be populated.

####`Output`

```
n : int
value : int
address : str
tx_index : int
script : str
spent : bool
```

####`Address`

```
hash160 : str
address : str
n_tx : int
total_received : int
total_sent : int
final_balance : int
transactions : array of Transaction objects

```

####`UnspentOutput`

```
tx_hash : str
tx_index : int
tx_output_n : int
script : str
value : int
value_hex : str
confirmations : int
```

####`LatestBlock`

```
hash : str
time : int
block_index : int
height : int
tx_indexes : array of TX indexes (integers)
```

####`SimpleBlock`

```
height : int
hash : str
time : int
main_chain : bool
```

####`InventoryData`

```
hash : str
type : str
initial_time : int
initial_ip : str
nconnected : int
relayed_count : int
relayed_percent : int
```
