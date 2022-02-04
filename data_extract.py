# Imports
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

# API Keys
my_key = '197d8494-cdfe-4ca3-aece-1aa263bed70b'
sandbox_key = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'

# Sandbox URLs 
latest_listings = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
latest_quotes = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
gainers_losers_trending = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/trending/gainers-losers'
price_preformance = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/price-performance-stats/latest'

# Show latest listings
url = latest_listings
parameters = {
  'start':'1',
  'limit':'3',
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': sandbox_key,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)