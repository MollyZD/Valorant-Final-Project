# Imports
import streamlit as st
from Pages import data # Allow access to dataframe

def app():
    # Introduction to dataset
    st.header("Valorant Dataset")
    st.subheader("This dataset contains pro match statistics from the game Valorant ranging from April 2021 to April 2023.")

    # Display dataframe
    st.dataframe(data.df)