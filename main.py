from nbformat import write
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
#header_image = Image.open(urlopen('https://images.ctfassets.net/0idwgenf7ije/6X87du1QI3CqHWKgTtCeKS/f075ac8d834dba7c46615b8d0c79f23e/Gemini-Defi_Ethereum_A_Guide_to_the_global_supercomputer.png?fm=webp'))

st.image(header_image)
st.title('Crypto Prices Today')
st.write("")
#st.header('My Coins')

option = st.selectbox(
     'Select:',
     ('Bitcoin', 'Ethereum', 'Chainlink', 'Polkadot', 'Cardano', 'Show All'))
st.write("\n\n")

if option == 'Bitcoin':
    st.image(btc_logo)
    st.subheader('Bitcoin ($)')
    st.table(data_extract.df_btc)
    st.subheader('Biggest Movers Today')
    st.bar_chart(data_extract.movers_24h)
    st.subheader('Biggest Movers This Week')
    st.bar_chart(data_extract.movers_7d)
    st.area_chart(data_extract.mkd)

elif option == 'Ethereum': 
    st.image(eth_logo)
    st.subheader('Ethereum ($)')
    st.table(data_extract.df_eth)

elif option == 'Chainlink': 
    st.image(link_logo)
    st.subheader('Chainlink ($)')
    st.table(data_extract.df_link)

elif option == 'Polkadot': 
    st.image(dot_logo)
    st.subheader('Polkadot ($)')
    st.table(data_extract.df_ada)

elif option == 'Cardano': 
    st.image(ada_logo)
    st.subheader('Cardano ($)')
    st.table(data_extract.df_link)

elif option == 'Show All':
    st.subheader('Change Over 24HR')
    st.bar_chart(data_extract.df_chart1)