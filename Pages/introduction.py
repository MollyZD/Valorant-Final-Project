import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Pages import data

def app():
    st.header("Valorant Dataset")
    st.subheader("This dataset contains pro match statistics from the game Valorant ranging from April 2021 to April 2023.")

    st.dataframe(data.df)