import imp
import streamlit as st
from PIL import Image
import data_extract
from urllib.request import urlopen

st.title('Crypto Prices Today')
st.header('Main Dashboard')

st.write('Bitcoin ($)')
st.table(data_extract.df)