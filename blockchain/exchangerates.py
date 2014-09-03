import urllib2
import util
import json

class Currency:
    def __init__(self, last, buy, sell, symbol, p15min):
        self.last = last
        self.buy = buy
        self.sell = sell
        self.symbol = symbol
        self.p15min = p15min

def ticker(api_code = None):
    response = util.call_api('ticker' if api_code is None else 'ticker?api_code=' + api_code)
    json_response = json.loads(response)
    ticker = {}
    for key in json_response:
        json_ccy = json_response[key]
        ccy = Currency(json_ccy['last'],
                        json_ccy['buy'],
                        json_ccy['sell'],
                        json_ccy['symbol'],
                        json_ccy['15m'])
        ticker[key] = ccy
    return ticker

def to_btc(ccy, value, api_code = None):
    res = 'tobtc?currency={0}&value={1}'.format(ccy, value)
    if api_code is not None:
        res += '&api_code=' + api_code
    return util.call_api(res)