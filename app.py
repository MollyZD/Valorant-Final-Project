import streamlit as st
import numpy as np
from PIL import Image

from multipage import MultiPage
from Pages import agent, map, player, team, introduction

# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('Valorant_Logo.png')
display = np.array(display)
col1, col2 = st.columns(2)
col1.image(display, width = 400)
col2.title("Valorant Data Application")

# Add all your application here
app.add_page("Introduction", introduction.app)
app.add_page("Team", team.app)
app.add_page("Player", player.app)
app.add_page("Agent", agent.app)
app.add_page("Map", map.app)

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

# The main app
app.run()