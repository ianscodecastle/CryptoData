import imp
import streamlit as st
from PIL import Image
import data_extract
from urllib.request import urlopen

st.title('Crypto Prices Today')
st.header('My Coins')

st.write('Bitcoin ($)')
st.table(data_extract.df_btc)

st.write('Ethereum ($)')
st.table(data_extract.df_eth)

st.write('Chainlink ($)')
st.table(data_extract.df_link)

st.header('Change Over 24HR')
st.bar_chart(data_extract.df_chart1)