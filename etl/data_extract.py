# Imports
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import pprint as pp
from etl import config

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 50)

# Show latest listings
url = config.sandbox_latest_quotes
parameters = {
  'slug':'bitcoin,ethereum,chainlink,polkadot,cardano',
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
  
  # Specify which data from API response to store
  data = json.loads(response.text)['data']

  # Make data frame
  df = pd.DataFrame(data).T
  df = pd.json_normalize(list(data.values()))
  df.index = data.keys()

  # Display dataframe
  #display(df)
  df.rename(columns={'name': 'NAME', 'quote.USD.price':'Price (USD)','quote.USD.percent_change_24h':'24h Change (%)', 'quote.USD.percent_change_7d':'7d Change (%)', 'quote.USD.market_cap':'Market Cap (USD)'}, inplace=True)
  print(df)

  # Create views
  df_view1 = df[['slug', 'Price (USD)']] # all rows, specific columns
  print(df_view1)

  core_info = ['Price (USD)','24h Change (%)','7d Change (%)','Market Cap (USD)']

  df_btc = df.loc[['bitcoin'], core_info]
  df_eth = df.loc[['ethereum'], core_info]
  df_link = df.loc[['chainlink'], core_info]
  df_dot = df.loc[['polkadot'], core_info]
  df_ada = df.loc[['cardano'], core_info]

  df_chart1 = df.loc[:, ['24h Change (%)']]
  
  # Load to destination
  #df.to_csv('cmc_dataframe.csv', index=False)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
