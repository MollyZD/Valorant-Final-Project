# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Pages import data # Allow access to dataframe and base class

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

    # Derived class from Entity
    class Player(data.Entity):

        # Constructor
        def __init__(self, entity, year):
            data.Entity.__init__(self, entity, year)
        
        # Filter dataframe by player selected
        def filter_player(self):
            player_df = data.df[data.df["player-name"] == self.entity]
            st.dataframe(player_df)
        
        # Filter dataframe by player and year selected
        def filter_player_year(self):
            if self.year == "2021":
                player_year_df = data.df[(data.df["player-name"] == self.entity) & (data.df["match-datetime"].isin(data.y2021))]
                st.dataframe(player_year_df)
            elif self.year == "2022":
                player_year_df = data.df[(data.df["player-name"] == self.entity) & (data.df["match-datetime"].isin(data.y2022))]
                st.dataframe(player_year_df)
            elif self.year == "2023":
                player_year_df = data.df[(data.df["player-name"] == self.entity) & (data.df["match-datetime"].isin(data.y2023))]
                st.dataframe(player_year_df)
        
        # Plot statistic
        def plot_stat(self, stat, type):
            st.header(stat)
            if self.year == "2021":
                player_year_df = data.df[(data.df["player-name"] == self.entity) & (data.df["match-datetime"].isin(data.y2021))]
                player_year_df.dropna()
            elif self.year == "2022":
                player_year_df = data.df[(data.df["player-name"] == self.entity) & (data.df["match-datetime"].isin(data.y2022))]
                player_year_df.dropna()
            elif self.year == "2023":
                player_year_df = data.df[(data.df["player-name"] == self.entity) & (data.df["match-datetime"].isin(data.y2023))]
                player_year_df.dropna()

            player_year_df["match-datetime"] = pd.to_datetime(player_year_df["match-datetime"])
            player_year_df.sort_values(by = stat, ascending = True, inplace = True)
            date = player_year_df["match-datetime"]
            value = player_year_df[stat]
            value = value.astype(float)

            fig, ax = plt.subplots(1, figsize = (20, 8))
            if type == "bar":
                ax.bar(date, value)
            elif type == "scatter":
                ax.scatter(date, value)
            fig.autofmt_xdate()
            st.pyplot(plt)
    
    # Run if a player is selected
    if player:
        player_name = Player(player, year)

        player_name.display_name()
        player_name.filter_player()

        # Run if a year is selected
        if year:
            player_name.display_year()
            player_name.filter_player_year()
            player_name.plot_stat("rating", "scatter")
            player_name.plot_stat("average-combat-score", "bar")
            player_name.plot_stat("kills", "bar")
            player_name.plot_stat("deaths", "bar")
            player_name.plot_stat("assists", "bar")
            player_name.plot_stat("headshot %", "scatter")
        
