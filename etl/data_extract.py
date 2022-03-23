# Imports
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import pprint as pp
import config


# Show latest listings
url = config.latest_listings
parameters = {
  'slug':'bitcoin',
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.sandbox_key,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  df = pd.DataFrame.from_records(data)
  pp.pprint(df.loc['bitcoin','data'])
  #df.to_csv('cmc_dataframe.csv', index=False)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
