# Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in dataframe from CSV file
df = pd.read_csv("valorant_data.csv", encoding='latin-1', dtype='unicode')

# Filter dataframe by columns
agent = df["agent"]
map = df["map"]
player = df["player-name"]
team = df["player-team"]
date = df["match-datetime"]

# Filter match-datetime column by year
y2021 = date.loc[date.str.contains("2021")]
y2022 = date.loc[date.str.contains("2022")]
y2023 = date.loc[date.str.contains("2023")]

# Base class
class Entity():

        # Constructor
        def __init__(self, entity, year):
            self.entity = entity
            self.year = year
        
        # Display name of entity selected
        def display_name(self):
            st.header(self.entity)
        
        # Display year selected
        def display_year(self):
            st.header(self.year)





