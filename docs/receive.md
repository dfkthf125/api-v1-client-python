##`receive` module

####`receive`
Call the 'api/receive' endpoint and create a forwarding address. Returns a `ReceiveResponse` object.

Params:
```
dest_addr : str
callback : str
api_code : str (optional)
```

Usage:
```python
from blockchain import receive

resp = receive.receive('1hNapz1CuH4DhnV1DFHH7hafwDE8FJRheA', 'http://your.url.com')

```

###Response object field definitions

####`ReceiveResponse`

```
fee_percent : int
destination_address : str
input_address : str
callback_url : str
```
