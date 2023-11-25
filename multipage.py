# Framework by Prakhar Rathi
# Imports
import streamlit as st

class MultiPage:

    def __init__(self):
        self.pages = []
    
    def add_page(self, title, function):
        self.pages.append({
            "title": title,
            "function": function
        })
    
    def run(self):
        page = st.sidebar.selectbox(
            'App Navigation',
            self.pages,
            format_func = lambda page: page['title']
        )
    
        page.get('function')()