# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Pages import data # Allow access to dataframe

def app():

    # List of agents in Valorant
    agent = st.selectbox(
        'Please Choose An Agent:',
        ('Brimstone','Viper','Omen','Killjoy','Cypher','Sova','Sage','Phoenix','Jett',
        'Reyna','Raze','Breach','Skye','Yoru','Asta','KAYO','Chamber','Neon','Fade','Harbor','Gekko'),
        index = None,
        placeholder = "Select Agent"
    )

    # List of years in dataset
    year = st.selectbox(
        'Please Choose A Year:',
        ('2021','2022','2023'),
        index = None,
        placeholder = "Select Year"
    )

    class Agent():

        # Constructor
        def __init__(self, agent, year):
            self.agent = agent
            self.year = year
        
        # Display name of agent selected
        def display_name(self):
            st.header(self.agent)
        
        # Display year selected
        def display_year(self):
            st.header(self.year)
        
        # Display image of agent selected
        def show_image(self):
            st.image(f"{self.agent}.png")
        
        # Filter dataframe by agent selected
        def filter_agent(self):
            agent_df = data.df[data.df["agent"] == self.agent]
            st.dataframe(agent_df)
        
        # Filter dataframe by agent and year selected
        def filter_agent_year(self):
            if self.year == "2021":
                agent_year_df = data.df[(data.df["agent"] == self.agent) & (data.df["match-datetime"].isin(data.y2021))]
                st.dataframe(agent_year_df)
            elif self.year == "2022":
                agent_year_df = data.df[(data.df["agent"] == self.agent) & (data.df["match-datetime"].isin(data.y2022))]
                st.dataframe(agent_year_df)
            elif self.year == "2023":
                agent_year_df = data.df[(data.df["agent"] == self.agent) & (data.df["match-datetime"].isin(data.y2023))]
                st.dataframe(agent_year_df)

    # Run if an agent has been selected
    if agent:
        agent_name = Agent(agent, year)

        agent_name.display_name()
        agent_name.show_image()
        agent_name.filter_agent()
    
        # Run if a year has been selected
        if year:
            agent_name.display_year()
            agent_name.filter_agent_year()