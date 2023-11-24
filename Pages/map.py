import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Pages import data

def app():

    map = st.selectbox(
        'Please Choose A Map:',
        ('Bind','Haven','Split','Ascent','Icebox','Breeze','Fracture',
        'Pearl','Lotus'),
        index = None,
        placeholder = "Select Map"
    )

    year = st.selectbox(
        'Please Choose A Year:',
        ('2021','2022','2023'),
        index = None,
        placeholder = "Select Year"
    )

    class Map():

        def __init__(self, map, year):
            self.map = map
            self.year = year
        
        def display_name(self):
            st.header(self.map)
        
        def display_year(self):
            st.header(self.year)
        
        def show_image(self):
            st.image(f"{self.map}.png")
        
        def filter_map(self):
            map_df = data.df[data.df["map"] == self.map]
            st.dataframe(map_df)
        
        def filter_map_year(self):
            if self.year == "2021":
                map_year_df = data.df[(data.df["map"] == self.map) & (data.df["match-datetime"].isin(data.y2021))]
                st.dataframe(map_year_df)
            elif self.year == "2022":
                map_year_df = data.df[(data.df["map"] == self.map) & (data.df["match-datetime"].isin(data.y2022))]
                st.dataframe(map_year_df)
            elif self.year == "2023":
                map_year_df = data.df[(data.df["map"] == self.map) & (data.df["match-datetime"].isin(data.y2023))]
                st.dataframe(map_year_df)

    if map:
        map_name = Map(map, year)

        map_name.display_name()
        map_name.show_image()
        map_name.filter_map()

        if year:
            map_name.display_year()
            map_name.filter_map_year()