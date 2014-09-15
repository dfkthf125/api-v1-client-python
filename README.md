#Blockchain API library (Python, v1)

An official Python module for interacting with the Blockchain.info API.

###Getting started

The module consists of the following sub-modules:

* `blockchaindata` ([docs](docs/blockchaindata.md)) ([api/blockchain_api][api1])
* `createwallet` ([docs](docs/createwallet.md)) ([api/create_wallet][api2])
* `exchangerates` ([docs](docs/exchangerates.md)) ([api/exchange\_rates\_api][api3])
* `receive` ([docs](docs/receive.md)) ([api/api_receive][api4])
* `statistics` ([docs](docs/statistics.md)) ([api/charts_api][api5])
* `wallet` ([docs](docs/wallet.md)) ([api/blockchain\_wallet\_api][api6])

The main module is called `blockchain`

###Error handling

All functions may raise exceptions caused by incorrectly passed parameters or other problems. If a call is rejected server-side, the `APIException` exception will be raised.

###Request limits and API keys

In order to prevent abuse some API methods require an API key approved with some basic contact information and a description of its intended use. Please request an API key [here](https://blockchain.info/api/api_create_code).

The same API key can be used to bypass the request limiter.

[api1]: https://blockchain.info/api/blockchain_api
[api2]: https://blockchain.info/api/create_wallet
[api3]: https://blockchain.info/api/exchange_rates_api
[api4]: https://blockchain.info/api/api_receive
[api5]: https://blockchain.info/api/charts_api
[api6]: https://blockchain.info/api/blockchain_wallet_api