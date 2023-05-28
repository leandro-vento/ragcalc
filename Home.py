import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

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

show_pages(
    [
        Page("streamlit_app.py", "Home", "🏠"),
        Page("other_pages/page2.py", "Page 2", ":books:"),
        Section("My section", icon="🎈️"),
        # Pages after a section will be indented
        Page("Another page", icon="💪"),
        # Unless you explicitly say in_section=False
        Page("Not in a section", in_section=False)
    ]
)