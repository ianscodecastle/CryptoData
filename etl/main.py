import imp
import streamlit as st
from PIL import Image
import data_extract
from urllib.request import urlopen

btc_logo = Image.open('/Users/ianrobinson/Projects/CryptoData/assets/bitcoin.png')
eth_logo = Image.open('/Users/ianrobinson/Projects/CryptoData/assets/ethereum.png')
link_logo = Image.open('/Users/ianrobinson/Projects/CryptoData/assets/chainlink.png')
dot_logo = Image.open('/Users/ianrobinson/Projects/CryptoData/assets/polkadot.png')
ada_logo = Image.open('/Users/ianrobinson/Projects/CryptoData/assets/cardano.png')

st.title('Crypto Prices Today')
st.header('My Coins')

st.image(btc_logo)
st.write('Bitcoin ($)')
st.table(data_extract.df_btc)

st.image(eth_logo)
st.write('Ethereum ($)')
st.table(data_extract.df_eth)

st.image(link_logo)
st.write('Chainlink ($)')
st.table(data_extract.df_link)

st.header('Change Over 24HR')
st.bar_chart(data_extract.df_chart1)