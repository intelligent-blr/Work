import requests
import json
import datetime as dt


url = 'https://api.binance.com/api/v3/klines'
symbol = 'BTCBUSD'
interval = '1d'

end = dt.datetime.now()
start = end - dt.timedelta(days=1)  # начало за последний день
start = str(int(dt.datetime(2021, 1, 1).timestamp() * 1000))
end = str(int(dt.datetime(2021, 12, 31).timestamp() * 1000))

params = {'symbol': symbol, 'interval': interval, 'startTime':
    start, 'endTime': end}

response = requests.get(url, params = params).json()
print(1)
