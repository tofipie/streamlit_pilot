# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:23:05 2024

@author: user
"""


import streamlit as st
from PyPDF2 import PdfReader

#from streamlit_extras.add_vertical_space import add_vertical_space


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
 #   add_vertical_space(5)
    st.write('Made with ❤️ by [Livia Ellen](https://liviaellen.com/portfolio)')




def main():
    st.header("Talk to your PDF 💬")
    st.write("This app uses OpenAI's LLM model to answer questions about your PDF file. Upload your PDF file and ask questions about it. The app will return the answer from your PDF file.")

    st.header("1. Pass your OPEN AI API KEY here")
    v='demo'
    openai_key=st.text_input("**OPEN AI API KEY**", value=v)
    st.write("You can get your OpenAI API key from [here](https://platform.openai.com/account/api-keys)")

    if openai_key==v:
        openai_key=st.secrets["OPENAI_API_KEY"]
    # if openai_key=='':
    #     load_dotenv()
    os.environ["OPENAI_API_KEY"] = openai_key

    # upload a PDF file

    st.header("2. Upload PDF")
    pdf = st.file_uploader("**Upload your PDF**", type='pdf')

