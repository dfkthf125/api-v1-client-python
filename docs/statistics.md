##`statistics` module

####`get`
Get network statistics. Returns a `Stats` object.

Params:
```
api_code : str (optional)
```

Usage:
```python
from blockchain import statistics

stats = statistics.get()
```


###Response object field definitions

####`Stats`

```
trade_volume_btc : float
miners_revenue_usd : float
n_btc_mined : long
trade_volume_usd : float
difficulty : float
minutes_between_blocks : float
days_destroyed : float
n_tx : int
hash_rate : float
timestamp : long
n_blocks_mined : int
blocks_size : int
total_fees_btc : int
total_btc_sent : long
estimated_btc_sent : long
totalbtc : long
n_blocks_total :int
nextretarget : int
estimated_transaction_volume_usd : float
miners_revenue_btc : int
market_price_usd : float
```
