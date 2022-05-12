# Reminder: bring in market data using vectorbt
from alpaca_trade_api.rest import REST, TimeFrame
from alpaca_trade_api.stream import Stream
from config import *
from datetime import datetime
import pandas as pd
import numpy as np

rest_api = REST(API_KEY, SECRET_KEY, 'https://paper-api.alpaca.markets')

# retrieve daily bar data for SPY in a dataframe
spy_bars = rest_api.get_bars('SPY', TimeFrame.Day, '2021-01-01', '2021-03-30').df
spy_bars.head(3)
#print(spy_bars.head(3))

# quote and trade data also available for equities
# spy_quotes = rest_api.get_quotes('SPY', '2021-01-01', '2021-01-05', 5).df
spy_trades = rest_api.get_trades('SPY', '2021-01-01', '2021-01-05').df
# print(spy_quotes.quotes)
# print(spy_trades.head(2))
spy_trades.head(3)
print(len(spy_trades.head(3)))

# retrieve quote data for Bitcoin in a dataframe
bitcoin_quotes = rest_api.get_crypto_quotes('BTCUSD', '2021-01-01', '2021-01-02').df
bitcoin_quotes.head(3)
#print(bitcoin_quotes.head(3))

# bar and trade data also available for crypto
# bitcoin_bars = rest_api.get_crypto_bars('BTCUSD', TimeFrame.Day, '2020-01-01', '2021-01-05').df
# bitcoin_trades = rest_api.get_crypto_trades('BTCUSD', '2021-01-01', '2021-01-05').df

def main():
    # get the current price of SPY
    current_price = rest_api.get_bars('SPY', TimeFrame.Day, '2020-01-01', '2020-01-05').df['close'][0]
    print(current_price)

or_lo = None
or_hi = None

def set_bracket_orders(order_id):
    global or_lo
    global or_hi
    # get the current price of SPY
    current_price = rest_api.get_bars('SPY', TimeFrame.Day, '2020-01-01', '2020-01-05').df['close'][0]
    print(current_price)
    or_hi = max(ages.values())
    print(max_value)