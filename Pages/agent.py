# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Pages import data # Allow access to dataframe and base class

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

    # Derived class from Entity
    class Agent(data.Entity):

        # Constructor
        def __init__(self, entity, year):
            data.Entity.__init__(self, entity, year)
        
        # Display image of agent selected
        def show_image(self):
            st.image(f"{self.entity}.png")
        
        # Filter dataframe by agent selected
        def filter_agent(self):
            agent_df = data.df[data.df["agent"] == self.entity]
            st.dataframe(agent_df)
        
        # Filter dataframe by agent and year selected
        def filter_agent_year(self):
            if self.year == "2021":
                agent_year_df = data.df[(data.df["agent"] == self.entity) & (data.df["match-datetime"].isin(data.y2021))]
                st.dataframe(agent_year_df)
            elif self.year == "2022":
                agent_year_df = data.df[(data.df["agent"] == self.entity) & (data.df["match-datetime"].isin(data.y2022))]
                st.dataframe(agent_year_df)
            elif self.year == "2023":
                agent_year_df = data.df[(data.df["agent"] == self.entity) & (data.df["match-datetime"].isin(data.y2023))]
                st.dataframe(agent_year_df)
        
        # Plot statistic
        def plot_stat(self, stat, type):
            st.header(stat)
            if self.year == "2021":
                agent_year_df = data.df[(data.df["agent"] == self.entity) & (data.df["match-datetime"].isin(data.y2021))]
                agent_year_df.dropna()
            elif self.year == "2022":
                agent_year_df = data.df[(data.df["agent"] == self.entity) & (data.df["match-datetime"].isin(data.y2022))]
                agent_year_df.dropna()
            elif self.year == "2023":
                agent_year_df = data.df[(data.df["agent"] == self.entity) & (data.df["match-datetime"].isin(data.y2023))]
                agent_year_df.dropna()
                
            agent_year_df["match-datetime"] = pd.to_datetime(agent_year_df["match-datetime"])
            agent_year_df.sort_values(by = stat, ascending = True, inplace = True)
            date = agent_year_df["match-datetime"]
            value = agent_year_df[stat]
            value = value.astype(float)

            fig, ax = plt.subplots(1, figsize = (20, 8))
            if type == "bar":
                ax.bar(date, value)
            elif type == "scatter":
                ax.scatter(date, value)
            fig.autofmt_xdate()
            st.pyplot(plt)

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
            agent_name.plot_stat("kills-attack","scatter")
            agent_name.plot_stat("kills-defend","scatter")
            agent_name.plot_stat("deaths-attack","scatter")
            agent_name.plot_stat("deaths-defend","scatter")
            agent_name.plot_stat("assists-attack","scatter")
            agent_name.plot_stat("assists-defend","scatter")