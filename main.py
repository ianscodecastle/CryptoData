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

header_image = Image.open(urlopen('https://images.ctfassets.net/0idwgenf7ije/6OUAGu0C76BTCRaJ9t9rs7/9bcfc6d0ae3c0247a2d1b87157f964a3/Gemini-Non-Fungible_Token-_One_of_a_Kind_Assets_for_Collectibles_and_Rare_Items.png?fm=webp'))

st.image(header_image)
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