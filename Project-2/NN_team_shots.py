import pandas as pd

'''
Fattas motståndarens tillåtna skott i både .csv
TODO
Exempelvis predikta Osasuna kommer skjuta i hemmaplan mot Almeria.
Behöver:

- Osasuna har gjort skott i hemmaplan mot motståndaren 
läggs i team_shots

- Hur mycket skott har gjort mot Osasuna 
(för predikta almeria skott) och läggs i läggs opponent_shots 

- Hur mycket average gör den motståndaren 
att skjuta & ta emot skott från andra lag när motståndaren är bortaplan
ocg lägger i home_shots.csv, 
 
Exempelvis (fantasi nummer) i home_shots.csv:
Osasuna	vs Athletic Club
Osasuna vs FC Barcelona
osv...

Osasuna har gjort 18 skott, Athletic club har gjort 8 skott, 
Athletic club har average 15,32 tillåtna skott som 
motståndaren skjuter när Athletic club är bortaplan.

team_shots,opponent_shots,opponent_allow_avg
18,8,15.32

- Samma princip för predikta Almeria kommer skjuta i bortaplan 
mot Osasuna
'''


class ShotsCSV:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

        self.df['home_total_shots'] = pd.to_numeric(self.df['home_total_shots'], errors='coerce').fillna(0).astype(int)
        self.df['away_total_shots'] = pd.to_numeric(self.df['away_total_shots'], errors='coerce').fillna(0).astype(int)

        self.home_avg_shots_allowed = self.df.groupby('hometeam')['away_total_shots'].mean()
        self.away_avg_shots_allowed = self.df.groupby('awayteam')['home_total_shots'].mean()

        self.home_avg_shots_for = self.df.groupby('hometeam')['home_total_shots'].mean()
        self.away_avg_shots_for = self.df.groupby('awayteam')['away_total_shots'].mean()

    def get_team_shots(self, team_name, home_or_away):
        if home_or_away == 'home':

            team_df = self.df[self.df['hometeam'] == team_name][['home_total_shots', 'away_total_shots', 'awayteam']]
            team_df.columns = ['team_shots', 'opponent_shots', 'opponent']
            team_df['opponent_against_shots_avg'] = team_df['opponent'].map(self.away_avg_shots_allowed)
            team_df['opponent_for_shots_avg'] = team_df['opponent'].map(self.away_avg_shots_for)

        elif home_or_away == 'away':
            team_df = self.df[self.df['awayteam'] == team_name][['away_total_shots', 'home_total_shots', 'hometeam']]
            team_df.columns = ['team_shots', 'opponent_shots', 'opponent']
            team_df['opponent_against_shots_avg'] = team_df['opponent'].map(self.home_avg_shots_allowed)
            team_df['opponent_for_shots_avg'] = team_df['opponent'].map(self.home_avg_shots_for)        
        else:
            raise ValueError("EXCEPTION: Neither 'home' or 'away")
        
        return team_df
    
    def save_csv(self, data, file):
        data.to_csv(file, index=False)


df = ShotsCSV('la_liga_results_2324.csv')

home_df = df.get_team_shots('Osasuna', 'home')
away_df = df.get_team_shots('Almería', 'away')

print("Osasuna Home Data:\n", home_df)
print("Almeria Away Data:\n", away_df)

df.save_csv(home_df, 'home_shots.csv')
df.save_csv(away_df, 'away_shots.csv')


# #Åtgärda fel från Str till NaN och fyll med heltal med 0
# df['home_total_shots'] = pd.to_numeric(df['home_total_shots'], errors='coerce').fillna(0).astype(int)
# df['away_total_shots'] = pd.to_numeric(df['away_total_shots'], errors='coerce').fillna(0).astype(int)

# #Funktion för att få motståndaren laget medelvärde 
# # av tillåtna skott skjutet mot dem
# def get_away_shots_allowed_avg(df):
#     away_avg = df.groupby('awayteam')['home_total_shots'].mean()
#     return df.groupby('awayteam')('home_total_shots').mean().to_dict()

# def get_home_shots_allowed_avg(df):
#     return df.groupby('hometeam')['away_total_shots'].mean().to_dict()

# #Funktion för att få lag och motståndarskott
# def get_team_shots(df, team_name, home_or_away):
#     if home_or_away == 'home':
#         team_df = df[df['hometeam'] == team_name][['home_total_shots', 'away_total_shots']]
#         #En ny kolumn med ett nytt namn
#         team_df.columns = ['team_shots', 'opponent_shots']
#     elif home_or_away == 'away':
#         team_df = df[df['awayteam'] == team_name][['away_total_shots', 'home_total_shots']]
#         #En ny kolumn med ett nytt namn
#         team_df.columns = ['team_shots', 'opponent_shots']
#     else:
#         #Om input anvöndning blir inkorrekt ENDAST 'home' eller 'away' en exception!
#         raise ValueError("home_or_away parameter should either 'home or 'away'")
    
#     return team_df

# #Funktion för data användning till modellen
# def get_data_prediction(home_team, away_team):
#     home_total_shots = get_team_shots(df, home_team, 'home')
#     away_total_shots = get_team_shots(df, away_team, 'away')
#     return home_total_shots, away_total_shots

# #Exempel användning, tas Osasuna som hemmaplan och Almeria som bortalag
# #För osasuna som hemmalag
# home_shots = get_team_shots(df, 'Osasuna', 'home')
# print("Home Shots and opponent Shots\n", home_shots)

# #För almeria som är bortalag
# away_shots = get_team_shots(df, 'Almería', 'away')
# print("Away Shots and opponent Shots:\n", away_shots)


# #Spara data för NN_model.py
# home_shots.to_csv('home_shots.csv', index=False)
# away_shots.to_csv('away_shots.csv', index=False)