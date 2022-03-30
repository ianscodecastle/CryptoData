from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
#import config # Use this import when running data_extract, comment out when running main
from etl import config # Use this import when running main, comment out when running data_extract

# Show metadata
url = config.pro_info
parameters = {
  'slug':'bitcoin,ethereum,chainlink,polkadot,cardano'
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
#   df.index = data.keys()

  df.rename(columns={'urls.website': 'Website', 'urls.source_code':'Source Code','urls.technical_doc':'Technical Docs', 'urls.reddit':'Reddit', 'urls.twitter':'Twitter', 'description':'Description', 'date_launched':'Date Launched', 'tags':'Tags', 'category':'Category'}, inplace=True)


  description = ['Description']
  btc_desc = df.loc[[0], description]
  print(btc_desc)

  core_info = ['Description','Website', 'Source Code','Technical Docs','Date Launched', 'Twitter', 'Reddit', 'Tags', 'Category']
  df_btc = df.loc[[0], core_info]
  df_eth = df.loc[[1], core_info]
  df_link = df.loc[[2], core_info]
  df_dot = df.loc[[3], core_info]
  df_ada = df.loc[[4], core_info]

  print(description)

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
