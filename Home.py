import streamlit as st

st.set_page_config(
  page_title='RagCalc',
  page_icon=':bar_chart:',
  layout='wide',
  initial_sidebar_state='collapsed'
)

with open('css/style.css') as f:
  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

st.header('Seja bem-vindo ao RagCalc!')
st.markdown('#')
st.markdown('''---''')

with st.sidebar:
  projeto = st.selectbox('Projeto', ['INFRA', 'GOINFRA'])
  if (projeto == 'INFRA'):
    op_ref = ['01/2023']
  elif (projeto == 'GOINFRA'):
    op_ref = ['04/2023']
  referencia = st.selectbox('Referência', op_ref)
    