import streamlit as st

st.set_page_config(
  page_title='Seja bem-vindo ao RagCalc',
  page_icon=':bar_chart:',
  layout='wide'
)
with open('style.css') as f:
  st.markdown('<style>{f.read()}</style>', unsafe_allow_html = True)

st.button('Teste')
