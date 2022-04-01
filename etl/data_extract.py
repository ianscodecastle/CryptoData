# Imports
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
#import config # Use this import when running data_extract, comment out when running main
from etl import config # Use this import when running main, comment out when running data_extract

# Show latest quotes
url = config.pro_latest_quotes
parameters = {
  'slug':'bitcoin,ethereum,chainlink,polkadot,cardano',
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.my_key,
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
  # df.index = data.keys()


  # Rename columns
  df.rename(columns={'name': 'Name', 'quote.USD.price':'Price (USD)','quote.USD.percent_change_24h':'24h Change (%)', 'quote.USD.percent_change_7d':'7d Change (%)', 'quote.USD.market_cap':'Market Cap (USD)', 'quote.USD.market_cap_dominance':'Market Cap Dominance'}, inplace=True)
  df.set_index('Name', inplace=True)

  # Array of desired columns
  core_info = ['Price (USD)','24h Change (%)','7d Change (%)','Market Cap (USD)']

  # Create dataframe views for each coin
  df_btc = df.loc[['Bitcoin'], core_info]
  df_eth = df.loc[['Ethereum'], core_info]
  df_link = df.loc[['Chainlink'], core_info]
  df_dot = df.loc[['Polkadot'], core_info]
  df_ada = df.loc[['Cardano'], core_info]

  # Dataframe views for graph data
  movers_24h = df.loc[:,['24h Change (%)']]
  movers_7d = df.loc[:,['7d Change (%)']]
  mkd = df.loc[:,['Market Cap Dominance']]

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
