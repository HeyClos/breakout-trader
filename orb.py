# from nsepython import *
from alpaca_trade_api.rest import REST, TimeFrame
from datetime import datetime, timedelta
from config import *

# #opening range breakout

# todays_date = datetime.now().strftime("%Y-%m-%d")
delta = datetime.now() - timedelta(days = 5)
five_days_ago = delta.strftime("%Y-%m-%d")

rest_api = REST(API_KEY, SECRET_KEY, 'https://paper-api.alpaca.markets')

# week_movement = spy_bars['close'].pct_change(periods = 5)

# catalyst

six_month_high = 0.0
three_month_high = 0.0
one_month_high = 0.0
current_price = 0.0
tight_price = False

# True if price has dropped more than 10% in last 6 or 3 or 1 month(s)
catalyst = six_month_high * 0.9 > current_price or three_month_high * 0.9 > current_price or one_month_high * 0.1 > current_price

spy_bars = rest_api.get_bars('SPY', TimeFrame.Day, five_days_ago).df
# spy_bars.head(5)

# for i in range(len(spy_bars)):
#     if spy_bars['high'][i] > six_month_high:
#         six_month_high = spy_bars['high'][i]
#     if spy_bars['high'][i] > three_month_high:
#         three_month_high = spy_bars['high'][i]
#     if spy_bars['high'][i] > one_month_high:
#         one_month_high = spy_bars['high'][i]
#     if spy_bars['close'][i] > current_price:
#         current_price = spy_bars['close'][i]
#     if spy_bars['close'][i] < current_price * 0.9:
#         tight_price = True

# when i place a buy order, i want to know the price at which i placed the order
# when i place a sell order, i want to know the price at which i placed the order

