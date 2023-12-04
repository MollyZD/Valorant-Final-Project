# Imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Pages import data # Allow access to dataframe and base class

def app():

    # List of maps in Valorant
    map = st.selectbox(
        'Please Choose A Map:',
        ('Bind','Haven','Split','Ascent','Icebox','Breeze','Fracture',
        'Pearl','Lotus'),
        index = None,
        placeholder = "Select Map"
    )

    # List of years in dataset
    year = st.selectbox(
        'Please Choose A Year:',
        ('2021','2022','2023'),
        index = None,
        placeholder = "Select Year"
    )

    class Map(data.Entity):

        # Constructor
        def __init__(self, entity, year):
            data.Entity.__init__(self, entity, year)
        
        # Display image of map selected
        def show_image(self):
            st.image(f"{self.entity}.png")
        
        # Filter dataframe by map selected
        def filter_map(self):
            map_df = data.df[data.df["map"] == self.entity]
            st.dataframe(map_df)
        
        # Filter dataframe by map and year selected
        def filter_map_year(self):
            if self.year == "2021":
                map_year_df = data.df[(data.df["map"] == self.entity) & (data.df["match-datetime"].isin(data.y2021))]
                st.dataframe(map_year_df)
            elif self.year == "2022":
                map_year_df = data.df[(data.df["map"] == self.entity) & (data.df["match-datetime"].isin(data.y2022))]
                st.dataframe(map_year_df)
            elif self.year == "2023":
                map_year_df = data.df[(data.df["map"] == self.entity) & (data.df["match-datetime"].isin(data.y2023))]
                st.dataframe(map_year_df)
        
        # Plot statistic
        def plot_stat(self, stat, type):
            st.header(stat)
            if self.year == "2021":
                map_year_df = data.df[(data.df["map"] == self.entity) & (data.df["match-datetime"].isin(data.y2021))]
                map_year_df.dropna()
            elif self.year == "2022":
                map_year_df = data.df[(data.df["map"] == self.entity) & (data.df["match-datetime"].isin(data.y2022))]
                map_year_df.dropna()
            elif self.year == "2023":
                map_year_df = data.df[(data.df["map"] == self.entity) & (data.df["match-datetime"].isin(data.y2023))]
                map_year_df.dropna()

            map_year_df["match-datetime"] = pd.to_datetime(map_year_df["match-datetime"])
            map_year_df.sort_values(by = stat, ascending = True, inplace = True)
            date = map_year_df["match-datetime"]
            value = map_year_df[stat]
            value = value.astype(float)

            fig, ax = plt.subplots(1, figsize = (20, 8))
            if type == "bar":
                ax.bar(date, value)
            elif type == "scatter":
                ax.scatter(date, value)
            fig.autofmt_xdate()
            st.pyplot(plt)

    
    # Run if a map has been selected
    if map:
        map_name = Map(map, year)

        map_name.display_name()
        map_name.show_image()
        map_name.filter_map()

        # Run if a year has been selected
        if year:
            map_name.display_year()
            map_name.filter_map_year()
            map_name.plot_stat("kills-attack","scatter")
            map_name.plot_stat("kills-defend","scatter")
            map_name.plot_stat("deaths-attack","scatter")
            map_name.plot_stat("deaths-defend","scatter")
            map_name.plot_stat("assists-attack","scatter")
            map_name.plot_stat("assists-defend","scatter")