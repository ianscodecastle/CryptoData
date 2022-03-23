import streamlit as st
import data_extract

st.title('Bitcoin Price Today')
st.header('Main Dashboard')

st.dataframe(data_extract.df)