import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("csv/soccer21-22.csv")

print("Basic Information:\n", df.info())
print("Team stats for the season:\n", df.head(10))

#checks for missing values
print("Missing values:\n", df.isnull().sum(axis=1))

#check for duplicates and removes duplicate data
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

#Calculation for home and away wins using numpy
home_wins = np.sum(df["FTHG"] > df["FTAG"])
away_wins = np.sum(df["FTAG"] > df["FTHG"])
draws = np.sum(df["FTHG"] == df["FTAG"])

#total matches played
total_matches = df.shape[0]

#calculation of win percentage
home_win_percentage = np.round((home_wins / total_matches) * 100 , 2)
away_win_percentage = np.round((away_wins / total_matches) * 100 , 2)
draw_percentage = np.round(((home_win_percentage + away_win_percentage) / total_matches) * 100, 2)
print("Home win percentage:", home_win_percentage, "%")
print("Away win percentage:", away_win_percentage, "%")
print("Draw percentage:", draw_percentage, "%")

#what I am visualising
name = ["Home Wins", "Away Wins", "Draws"]
total_win_percentage = [home_win_percentage, away_win_percentage, draw_percentage ]

#creating a bar plot for total home and away wins
plt.figure(figsize=(8, 5))
sns.barplot(x=name, y=total_win_percentage, palette="viridis")
plt.title("Home vs Away Win Percentage in Premier League 2021-2022")
plt.ylabel("Win Percentage (%)")
plt.ylim(0, 100)
plt.show()


