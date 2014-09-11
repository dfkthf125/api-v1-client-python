#Blockchain API library (Python, v1)

An official Python module for interacting with the Blockchain.info API.

##Getting started

The module consists of the following sub-modules:

* `blockchaindata` ([api/blockchain_api][api1])
* `createwallet` ([api/create_wallet][api2])
* `exchangerates` ([api/exchange\_rates\_api][api3])
* `receive` ([api/api_receive][api4])
* `statistics` ([api/charts_api][api5])
* `wallet` ([api/blockchain\_wallet\_api][api6])

The main module is called `blockchain`

##Usage


###`blockchaindata` module
All functions support an optional parameter called `api_code`

Get a single block based on a block index or hash:
```python
from blockchain import blockchaindata

block = blockchaindata.get_block('000000000000000016f9a2c3e0f4c1245ff24856a79c34806969f5084f410680')
```

Get a single transaction based on a transaction index or hash:
```python
tx = blockchaindata.get_transaction('d4af240386cdacab4ca666d178afc88280b620ae308ae8d2585e9ab8fc664a94')
```

Get an array of blocks at the specified height. Returns a `Block` object.
```python
blocks = blockchaindata.get_block_height(2570)
```

Get a single address and its transactions. Returns an `Address` object.
```python
address = blockchaindata.get_address('1HS9RLmKvJ7D1ZYgfPExJZQZA1DMU3DEVd')
```

Get an array of unspent outputs for an address. Returns an array of `UnspentOutput` objects.
```python
outs = blockchaindata.get_unspent_outputs('1HS9RLmKvJ7D1ZYgfPExJZQZA1DMU3DEVd')
```

Get the latest block on the main chain. Returns a `LatestBlock` object.
```python
latest_block = blockchaindata.get_latest_block()
```

Get a list of currently unconfirmed transactions. Returns an array of `Transaction` objects.
```python
txs = blockchaindata.get_unconfirmed_tx()
```

Get a list of blocks for a specific day or mining pool. Parameters are `time` (int, unix time in ms) and `pool_name` (str). Both parameters are optional but at least one is required. Returns an array of `SimpleBlock` objects.
```python
blocks = blockchaindata.get_blocks(pool_name = 'Discus Fish')
```

Get inventory data for recent blocks and addresses. Parameter is either a block or tx hash. Only objects up to one hour are returned. Returns an `InventoryData` object.

```python
inv = blockchaindata.get_inventory_data('d4af240386cdacab4ca666d178afc88280b620ae308ae8d2585e9ab8fc664a94')
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
block_height : int
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
type : int
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
probable_owners : array of ProbableOwner objects (ip : str, confidence : int)
mining_nodes : array of MiningNode objects (link : str, name : str)
```


[api1]: https://blockchain.info/api/blockchain_api
[api2]: https://blockchain.info/api/create_wallet
[api3]: https://blockchain.info/api/exchange_rates_api
[api4]: https://blockchain.info/api/api_receive
[api5]: https://blockchain.info/api/charts_api
[api6]: https://blockchain.info/api/blockchain_wallet_api