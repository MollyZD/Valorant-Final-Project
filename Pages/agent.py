import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Pages import data

def app():

    agent = st.selectbox(
        'Please Choose An Agent:',
        ('Brimstone','Viper','Omen','Killjoy','Cypher','Sova','Sage','Phoenix','Jett',
        'Reyna','Raze','Breach','Skye','Yoru','Asta','KAYO','Chamber','Neon','Fade','Harbor','Gekko'),
        index = None,
        placeholder = "Select Agent"
    )

    year = st.selectbox(
        'Please Choose A Year:',
        ('2021','2022','2023'),
        index = None,
        placeholder = "Select Year"
    )

    class Agent():

        def __init__(self, agent, year):
            self.agent = agent
            self.year = year
        
        def display_name(self):
            st.header(self.agent)
        
        def display_year(self):
            st.header(self.year)
        
        def show_image(self):
            st.image(f"{self.agent}.png")
        
        def filter_agent(self):
            agent_df = data.df[data.df["agent"] == self.agent]
            st.dataframe(agent_df)
        
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

    if agent:
        agent_name = Agent(agent, year)

        agent_name.display_name()
        agent_name.show_image()
        agent_name.filter_agent()
    
        if year:
            agent_name.display_year()
            agent_name.filter_agent_year()