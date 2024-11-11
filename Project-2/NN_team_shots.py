import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import regularizers

df = pd.read_csv('spain-la-liga-matches-2023-to-2024-stats - spain-la-liga-matches-2023-to-2024-stats.csv')

#Åtgärda fel från Str till NaN och fyll med heltal med 0
#Statistiken i csv-filen har 1 för många bilder, vilket gör den korrekt med -1
df['home_team_shots'] = pd.to_numeric(df['home_team_shots'], errors='coerce').fillna(0).astype(int) - 1
df['away_team_shots'] = pd.to_numeric(df['away_team_shots'], errors='coerce').fillna(0).astype(int) - 1

#Funktion för att få lag- och motståndarskott
def get_team_shots(df, team_name, home_or_away):
    if home_or_away == 'home':
        team_df = df[df['home_team_name'] == team_name][['home_team_shots', 'away_team_shots']]
        #En ny kolumn med ett nytt namn
        team_df.columns = ['team_shots', 'opponent_shots']
    elif home_or_away == 'away':
        team_df = df[df['away_team_name'] == team_name][['away_team_shots', 'home_team_shots']]
        #En ny kolumn med ett nytt namn
        team_df.columns = ['team_shots', 'opponent_shots']
    else:
        #Om input anvöndning blir inkorrekt ENDAST 'home' eller 'away' en exception!
        raise ValueError("home_or_away parameter should either 'home or 'away'")
    
    return team_df

#Funktion för data användning till modellen
def get_data_prediction(home_team, away_team):
    home_team_shots = get_team_shots(df, home_team, 'home')
    away_team_shots = get_team_shots(df, away_team, 'away')
    return home_team_shots, away_team_shots

#Exempel användning, tas Osasuna som hemmaplan och Almeria som bortalag
#För osasuna som hemmalag
osasuna_home_shots = get_team_shots(df, 'CA Osasuna', 'home')
print("Osasuna Home Shots and opponent Shots\n", osasuna_home_shots)

#För almeria som är bortalag
almeria_away_shots = get_team_shots(df, 'Almería', 'away')
print("Almeria Away Shots and opponent Shots:\n", almeria_away_shots)

'''Nästa steg
Skapa modell, neural network
Predikta antal skott och se accuracy och försöker få ner absolute error 
'''
#Spara data för NN_model.py
# osasuna_home_shots.to_csv('osasuna_home_shots.csv', index=False)
# almeria_away_shots.to_csv('almeria_away_shots.csv', index=False)