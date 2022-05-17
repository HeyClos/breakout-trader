# breakout-trader

Algorithmic stock trading bot using Apaca API

- V1 focuses on opening range breakouts

### V1: May 17,2022 getting set up.
Trade.py generates a trade.
1. Clone this repo
2. Go to https://alpaca.markets/ create an account
3. Create a paper trading account(technically you could make a real account too, but I recommend you start with paper.) 
4. Alpaca will generate an API key and Secret Key, save those.
5. Create a config.py file locally, use this file to securely store your API and Secret keys. 
  In config.py:
  - "APCA-API-KEY-ID": "PASTE YOUR ALPACA API KEY HERE",
  - "APCA-API-SECRET-KEY": "PASTE YOUR ALPACA SECRET KEY HERE",
6. In the terminal, make sure you cd into breakout-trade, then run "python3 trade.py"

You will notice that line 34 of trade.py executes an buy order of Apple shares. 
You can alter line 34 to your liking, to buy or sell different stocks.
