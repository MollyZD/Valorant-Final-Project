# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Pages import data # Allow access to dataframe

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

    class Team():

        # Constructor
        def __init__(self, team, year):
            self.team = team
            self.year = year
        
        # Display name of team selected
        def display_name(self):
            st.header(self.team)
        
        # Display year selected
        def display_year(self):
            st.header(self.year)
        
        # Filter dataframe by team selected
        def filter_team(self):
            team_df = data.df[data.df["player-team"] == self.team]
            st.dataframe(team_df)
        
        # Filter dataframe by team and year selected
        def filter_team_year(self):
            if self.year == "2021":
                team_year_df = data.df[(data.df["player-team"] == self.team) & (data.df["match-datetime"].isin(data.y2021))]
                st.dataframe(team_year_df)
            elif self.year == "2022":
                team_year_df = data.df[(data.df["player-team"] == self.team) & (data.df["match-datetime"].isin(data.y2022))]
                st.dataframe(team_year_df)
            elif self.year == "2023":
                team_year_df = data.df[(data.df["player-team"] == self.team) & (data.df["match-datetime"].isin(data.y2023))]
                st.dataframe(team_year_df)
    
    # Run if a team has been selected
    if team:
        team_name = Team(team, year)

        team_name.display_name()
        team_name.filter_team()

        # Run if a year has been selected
        if year:
            team_name.display_year()
            team_name.filter_team_year()
