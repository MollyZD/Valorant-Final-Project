import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("valorant_data.csv", encoding='latin-1', dtype='unicode')

agent = df["agent"]
map = df["map"]
player = df["player-name"]
team = df["player-team"]
date = df["match-datetime"]

y2021 = date.loc[date.str.contains("2021")]
y2022 = date.loc[date.str.contains("2022")]
y2023 = date.loc[date.str.contains("2023")]





