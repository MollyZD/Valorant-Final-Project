# Valorant-Data-Application
Final Project for CSC 360: Python Programming Fall 2023

This project is an interactive data explorer for the game Valorant using Streamlit.
The dataset contains data on pro match statistics from April 2021 to April 2023.

The app has 4 main pages: Team, Player, Agent, & Map
Each page allows the user to filter the dataframe based on an instance of each topic/selected year.
Each page then provides various visualizations of different statistics provided in the dataset
based on the instance and year chosen.

To run this project, Python & Streamlit must be installed.
After installing Streamlit, running:

streamlit run app.py

in a command prompt will open the app.

After opening the app, the user can navigate between the different pages using the dropdown menu
in App Navigation. The user can select an instance of the topic and a year using dropdown menus
on each page when prompted, which will then display filtered dataframes/visualizations.

For example, if the user selects 'Viper' and '2021' on the Agent page, two dataframes will be shown:
the first will be the entire dataframe filtered only by Viper, and the second will be the entire
dataframe filtered by Viper and 2021. Statistics related to Viper will then be shown below the dataframes.

If there is no data in the dataframe for the selected year, an empty dataframe will be returned.
Visualizations may appear blank if the app has not loaded them in time before the user scrolls to them.