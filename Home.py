import streamlit as st

with open('style.css') as f:
  st.markdown('<style>{f.read()}</style>', unsafe_allow_html = True)

st.title('Seja bem-vindo ao RagCalc')
