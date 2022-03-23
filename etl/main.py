import streamlit as st
from PIL import Image
import data_extract
from urllib.request import urlopen

st.title('Crypto Prices Today')
st.header('Main Dashboard')

st.write('Bitcoin ($)')
btc_image = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
st.table(data_extract.df)