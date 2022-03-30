# imports
import json
import string
from urllib.request import urlopen
import pandas as pd
import streamlit as st
from nbformat import write
from PIL import Image
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from assets import images
from etl import config, data_extract, coin_info

def buildHeader():
    st.image(images.header_image)
    st.title('Crypto Prices Today')
    st.write("")

def buildPages():
    option = st.selectbox(
        'Select:',
        ('Show All', 'Bitcoin', 'Ethereum', 'Chainlink', 'Polkadot', 'Cardano', 'Trends'))
    st.write("\n\n")

    if option == 'Show All':
        st.image(images.btc_logo)
        st.subheader('Bitcoin (BTC)')
        st.table(data_extract.df_btc)

        st.image(images.eth_logo)
        st.subheader('Ethereum (ETH)')
        st.table(data_extract.df_eth)

        st.image(images.link_logo)
        st.subheader('Chainlink (LINK)')
        st.table(data_extract.df_link)

        st.image(images.dot_logo)
        st.subheader('Polkadot (DOT)')
        st.table(data_extract.df_dot)

        st.image(images.ada_logo)
        st.subheader('Cardano (ADA)')
        st.table(data_extract.df_ada)


    elif option == 'Bitcoin':
        st.image(images.btc_logo)
        st.subheader('Bitcoin (BTC)')
        st.table(data_extract.df_btc)
        st.subheader('About Bitcoin:')
        st.write(coin_info.df_btc)

    elif option == 'Ethereum': 
        st.image(images.eth_logo)
        st.subheader('Ethereum (ETH)')
        st.table(data_extract.df_eth)

    elif option == 'Chainlink': 
        st.image(images.link_logo)
        st.subheader('Chainlink (LINK)')
        st.table(data_extract.df_link)

    elif option == 'Polkadot': 
        st.image(images.dot_logo)
        st.subheader('Polkadot (DOT)')
        st.table(data_extract.df_dot)

    elif option == 'Cardano': 
        st.image(images.ada_logo)
        st.subheader('Cardano (ADA)')
        st.table(data_extract.df_ada)

    elif option == 'Trends':
        st.subheader('Biggest Movers Today')
        st.bar_chart(data_extract.movers_24h)
        st.subheader('Biggest Movers This Week')
        st.bar_chart(data_extract.movers_7d)
        st.subheader('Market Cap Dominance')
        st.area_chart(data_extract.mkd)

def extractData():
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
    response = session.get(url, params=parameters)

    # Specify which data from API response to store
    data = json.loads(response.text)['data']

    # Make data frame
    df = pd.DataFrame(data).T
    df = pd.json_normalize(list(data.values()))
    df.index = data.keys()

    # Display dataframe
    #display(df)
    df.rename(columns={'name': 'NAME', 'quote.USD.price':'Price (USD)','quote.USD.percent_change_24h':'24h Change (%)', 'quote.USD.percent_change_7d':'7d Change (%)', 'quote.USD.market_cap':'Market Cap (USD)', 'quote.USD.market_cap_dominance':'Market Cap Dominance'}, inplace=True)

    # Create views
    df_view1 = df[['slug', 'Price (USD)']] # all rows, specific columns

    core_info = ['Price (USD)','24h Change (%)','7d Change (%)','Market Cap (USD)']
    df_btc = df.loc[['bitcoin'], core_info]
    df_eth = df.loc[['ethereum'], core_info]
    df_link = df.loc[['chainlink'], core_info]
    df_dot = df.loc[['polkadot'], core_info]
    df_ada = df.loc[['cardano'], core_info]

    movers_24h = df.loc[:,['24h Change (%)']]
    movers_7d = df.loc[:,['7d Change (%)']]

    mkd = df.loc[:,['Market Cap Dominance']]

extractData()
buildHeader()
buildPages()
