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

def ticker():
    response = util.call_api("ticker")
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

def tobtc(ccy, value):
    return util.call_api("tobtc?currency={0}&value={1}".format(ccy, value))