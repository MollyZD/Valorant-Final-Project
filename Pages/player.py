# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Pages import data # Allow access to dataframe

def app():

    # Players in dataset
    player = st.selectbox(
        'Please Choose A Player:',
        data.player.drop_duplicates(),
        index = None,
        placeholder = "Select Player"
    )

    # List of years in dataset
    year = st.selectbox(
        'Please Choose A Year:',
        ('2021','2022','2023'),
        index = None,
        placeholder = "Select Year"
    )

    class Player():

        # Constructor
        def __init__(self, player, year):
            self.player = player
            self.year = year

        # Display name of player selected
        def display_name(self):
            st.header(self.player)
        
        # Display year selected
        def display_year(self):
            st.header(self.year)
        
        # Filter dataframe by player selected
        def filter_player(self):
            player_df = data.df[data.df["player-name"] == self.player]
            st.dataframe(player_df)
        
        # Filter dataframe by player and year selected
        def filter_player_year(self):
            if self.year == "2021":
                player_year_df = data.df[(data.df["player-name"] == self.player) & (data.df["match-datetime"].isin(data.y2021))]
                st.dataframe(player_year_df)
            elif self.year == "2022":
                player_year_df = data.df[(data.df["player-name"] == self.player) & (data.df["match-datetime"].isin(data.y2022))]
                st.dataframe(player_year_df)
            elif self.year == "2023":
                player_year_df = data.df[(data.df["player-name"] == self.player) & (data.df["match-datetime"].isin(data.y2023))]
                st.dataframe(player_year_df)
    
    # Run if a player is selected
    if player:
        player_name = Player(player, year)

        player_name.display_name()
        player_name.filter_player()
        
        # Run if a year is selected
        if year:
            player_name.display_year()
            player_name.filter_player_year()
        
