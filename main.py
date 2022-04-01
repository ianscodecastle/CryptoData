# imports
import streamlit as st
from assets import images
from etl import data_extract, coin_info

# Spin up the dashboard using <streamlit run main.py> in terminal

def buildHeader():
    st.image(images.header_image)
    st.title('Crypto Prices Today')
    st.write("")

def buildPages():
    option = st.selectbox(
        'Select:',
        ('Show All', 'Trends','Bitcoin', 'Ethereum', 'Chainlink', 'Polkadot', 'Cardano', 'About Blockchain'))
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
        st.write(coin_info.btc_desc)
        st.markdown('**Links:**')
        st.markdown('[Source Code](https://github.com/bitcoin/bitcoin) | [Tecnical Docs](https://bitcoin.org/bitcoin.pdf) | [Twitter](https://twitter.com/bitcoin?lang=en) | [Reddit](https://www.reddit.com/r/Bitcoin/)')
        

    elif option == 'Ethereum': 
        st.image(images.eth_logo)
        st.subheader('Ethereum (ETH)')
        st.table(data_extract.df_eth)
        st.subheader('About Ethereum:')
        st.write(coin_info.eth_desc)
        st.markdown('**Links:**')
        st.markdown('[Source Code](https://github.com/ethereum/go-ethereum) | [Tecnical Docs](https://github.com/ethereum/wiki/wiki/White-Paper) | [Twitter](https://twitter.com/ethereum) | [Reddit](https://reddit.com/r/ethereum)')

    elif option == 'Chainlink': 
        st.image(images.link_logo)
        st.subheader('Chainlink (LINK)')
        st.table(data_extract.df_link)
        st.subheader('About Chainlink:')
        st.write(coin_info.link_desc)
        st.markdown('**Links:**')
        st.markdown('[Source Code](https://github.com/smartcontractkit/chainlink) | [Tecnical Docs](https://chain.link/whitepaper) | [Twitter](https://twitter.com/chainlink) | [Reddit](https://reddit.com/r/chainlink)')

    elif option == 'Polkadot': 
        st.image(images.dot_logo)
        st.subheader('Polkadot (DOT)')
        st.table(data_extract.df_dot)
        st.subheader('About Polkadot:')
        st.write(coin_info.dot_desc)
        st.markdown('**Links:**')
        st.markdown('[Source Code](https://github.com/paritytech/polkadot) | [Tecnical Docs](https://github.com/paritytech/polkadot) | [Twitter](https://twitter.com/Polkadot) | [Reddit](https://reddit.com/r/dot)')

    elif option == 'Cardano': 
        st.image(images.ada_logo)
        st.subheader('Cardano (ADA)')
        st.table(data_extract.df_ada)
        st.subheader('About Cardano:')
        st.write(coin_info.ada_desc)
        st.markdown('**Links:**')
        st.markdown('[Source Code](https://cardanoupdates.com/) | [Tecnical Docs](https://docs.cardano.org/en/latest/) | [Twitter](https://twitter.com/cardano) | [Reddit](https://reddit.com/r/cardano)')

    elif option == 'Trends':
        st.subheader('Biggest Movers Today')
        st.bar_chart(data_extract.movers_24h)
        st.subheader('Biggest Movers This Week')
        st.bar_chart(data_extract.movers_7d)
        st.subheader('Market Cap Dominance')
        st.area_chart(data_extract.mkd)

    elif option == 'About Blockchain':
        st.subheader('What is Blockchain?')
        st.image(images.blockchain_image)
        st.markdown('##')
        st.image(images.crypto_image)
        st.markdown('##')
        st.image(images.crypto_image_2)

buildHeader()
buildPages()
