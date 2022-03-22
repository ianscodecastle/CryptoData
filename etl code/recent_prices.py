# Imports
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint

# API Keys
my_key = '197d8494-cdfe-4ca3-aece-1aa263bed70b'
sandbox_key = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'

# URL for recent coin prices
latest_quotes = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Get quote
url = latest_quotes
parameters = {
  'slug': 'bitcoin,ethereum',  
  'convert': 'USD',
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
  print(json.dumps(data, indent = 2, sort_keys = True))

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

