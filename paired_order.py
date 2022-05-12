# Buy order with stop loss at day_low

def paired_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
        # "limit_price": string<number>, required if type is limit or stop_limit
        # "stop_price": string<number> required if type is stop or stop_limit
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force): 
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
        # "limit_price": string<number>, required if type is limit or stop_limit
        # "stop_price": string<number> required if type is stop or stop_limit
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)

response = create_order("AAPL", 1, "buy", "market", "gtc")
print(response)