import requests, json
from config import *
from market_data import or_hi, or_lo

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = BASE_URL + "/v2/account"
ORDERS_URL = BASE_URL + "/v2/orders"
HEADERS = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY,
    "Content-Type": "application/json"
}

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force): 
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force,
        "limit_price": limit_price, # string<number> required if type is limit or stop_limit
        "order_class": order_class, # string required if type is stop_limit
        "stop_loss": stop_loss
        #"stop_price":limit_price # string<number> required if type is stop or stop_limit
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)

# response = create_order("AAPL", 1, "buy", "market", "gtc")
response = create_order("AAPL", 10, "buy", "limit", "day", or_hi, "bracket", or_lo)
print(response)

if response["status"] == "rejected":
    print("Order rejected")
    print(response["reject_reason"])
else:
    print("Order submitted")
    print(response["id"])
    print(response["client_order_id"])
    print(response["symbol"])
    print(response["side"])
    print(response["type"])
    print(response["time_in_force"])
    print(response["limit_price"])
    print(response["stop_price"])
    print(response["qty"])
    print(response["filled_qty"])
    print(response["avg_price"])
    print(response["status"])
    print(response["time"])
    print(response["transact_time"])

# Get bars
# api.get_bars(stock, TimeFrame.Minute, (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'), adjustment='raw')[-1].c

symbol = "NVDA"
qty = 10
type = "limit"
limit_price = 250
order_class = "bracket"
take_profit = {"limit_price": limit_price * 1.10}    # 10% gain sets this value to $275
stop_loss = {"stop_price": limit_price * 0.95}       # 5% loss sets this value to $237.50
client_order_id=f"gcos_{random.randrange(100000000)}"

alpaca.submit_order(
                    symbol,
                    qty=qty, 
                    type=type,
                    limit_price=limit_price, 
                    order_class=order_class,
                    take_profit=take_profit,
                    stop_loss=stop_loss,
                    client_order_id=client_order_id
)