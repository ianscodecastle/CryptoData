import imp
import streamlit as st
from PIL import Image
from etl import data_extract
from urllib.request import urlopen


btc_logo = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
eth_logo = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
link_logo = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1975.png'))
dot_logo = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/6636.png'))
ada_logo = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png'))

st.title('Crypto Prices Today')
st.write("")
#st.header('My Coins')

st.image(btc_logo)
st.subheader('Bitcoin ($)')
st.table(data_extract.df_btc)

st.image(eth_logo)
st.subheader('Ethereum ($)')
st.table(data_extract.df_eth)

st.image(link_logo)
st.subheader('Chainlink ($)')
st.table(data_extract.df_link)

st.subheader('Change Over 24HR')
st.bar_chart(data_extract.df_chart1)