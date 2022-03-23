
import pandas as pd
import requests
import config_demo
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint

# info here: https://towardsdev.com/create-an-etl-pipeline-in-python-with-pandas-in-10-minutes-6be436483ec9

key = config_demo.api_key
url = config_demo.latest_quotes

parameters = {
  'slug': 'bitcoin,ethereum',  
  'convert': 'USD',
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY':  key,
}

session = Session()
session.headers.update(headers)


try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  pd.set_option("display.max_rows", None)
  pd.set_option("display.max_columns", None)
  df = pd.DataFrame.from_records(data)
  print(df['data'])

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


