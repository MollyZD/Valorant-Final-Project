# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Pages import data # Allow access to dataframe and base class

def app():

    # Teams in dataset
    team = st.selectbox(
        'Please Choose A Team:',
        data.team.drop_duplicates(),
        index = None,
        placeholder = "Select Team"
    )

    # List of years in dataset
    year = st.selectbox(
        'Please Choose A Year:',
        ('2021','2022','2023'),
        index = None,
        placeholder = "Select Year"
    )

    class Team(data.Entity):

        # Constructor
        def __init__(self, entity, year):
            data.Entity.__init__(self, entity, year)
        
        # Filter dataframe by team selected
        def filter_team(self):
            team_df = data.df[data.df["player-team"] == self.entity]
            st.dataframe(team_df)
        
        # Filter dataframe by team and year selected
        def filter_team_year(self):
            if self.year == "2021":
                team_year_df = data.df[(data.df["player-team"] == self.entity) & (data.df["match-datetime"].isin(data.y2021))]
                st.dataframe(team_year_df)
            elif self.year == "2022":
                team_year_df = data.df[(data.df["player-team"] == self.entity) & (data.df["match-datetime"].isin(data.y2022))]
                st.dataframe(team_year_df)
            elif self.year == "2023":
                team_year_df = data.df[(data.df["player-team"] == self.entity) & (data.df["match-datetime"].isin(data.y2023))]
                st.dataframe(team_year_df)
        
        # Filter dataframe by won games
        def filter_win(self):
            st.header("Won Games")
            team_win_df = data.df[(data.df["team1"] == self.entity) & (data.df["team1-score"] == "13") | (data.df["team2"] == self.entity) & (data.df["team2-score"] == "13")]
            st.dataframe(team_win_df)
        
        # Filter dataframe by lost games
        def filter_loss(self):
            st.header("Lost Games")
            team_lose_df = data.df[(data.df["team1"] == self.entity) & (data.df["team1-score"] != "13") | (data.df["team2"] == self.entity) & (data.df["team2-score"] != "13")]
            st.dataframe(team_lose_df)
    
    # Run if a team has been selected
    if team:
        team_name = Team(team, year)

        team_name.display_name()
        team_name.filter_team()

        # Stats Options
        stats = st.selectbox(
        'Please Choose A Statistic:',
        ("Wins","Losses"),
        index = None,
        placeholder = "Select Statistic"
    )
        if stats:
            if stats == "Wins":
                team_name.filter_win()
            elif stats == "Losses":
                team_name.filter_loss()

        # Run if a year has been selected
        if year:
            team_name.display_year()
            team_name.filter_team_year()

            # Stats Options
            stats2 = st.selectbox(
            'Please Choose A Statistic:',
            ("Yearly Wins","Yearly Losses"),
            index = None,
            placeholder = "Select Statistic"
        )
            if stats2:
                if stats2 == "Yearly Wins":
                    team_name.filter_win()
                elif stats2 == "Yearly Losses":
                    team_name.filter_loss()
 
