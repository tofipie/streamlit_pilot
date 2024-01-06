# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:23:05 2024

@author: user
"""


import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


st.set_page_config(page_title='🤗💬 PDF Chat App - GPT')

# Sidebar contents
with st.sidebar:
    st.title('🤗💬 PDF Chat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model

    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by [Livia Ellen](https://liviaellen.com/portfolio)')

