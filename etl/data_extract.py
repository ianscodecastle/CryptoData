# Imports
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import pprint as pp
import config

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 50)

# Show latest listings
url = config.latest_quotes
parameters = {
  'slug':'bitcoin,ethereum,chainlink,polkadot,cardano',
  #'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.sandbox_key,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  
  # Specify which data from API response to store
  data = json.loads(response.text)['data']

  # Make data frame
  df = pd.DataFrame(data).T
  df = pd.json_normalize(list(data.values()))
  #df.index = data.keys()

  # Display dataframe
  #display(df)

  # Load to destination
  #df.to_csv('cmc_dataframe.csv', index=False)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
