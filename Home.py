import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(
  page_title='RagCalc',
  page_icon=':bar_chart:',
  layout='wide',
  initial_sidebar_state='collapsed'
)

with open('css/style.css') as f:
  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

with st.sidebar:
    choose = option_menu("App Gallery", ["About", "Photo Editing", "Project Planning", "Python e-Course", "Contact"],
                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
                                }
    )

st.header('Seja bem-vindo ao RagCalc!')
st.markdown('#')
st.markdown('''---''')
