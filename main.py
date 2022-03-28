import string
from nbformat import write
import streamlit as st
from PIL import Image
from etl import data_extract
from assets import images
from urllib.request import urlopen

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

buildHeader()
buildPages()
