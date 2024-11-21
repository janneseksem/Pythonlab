import pandas as pd

# Ladda csv filer som ska mergas
footstats_df = pd.read_csv('spain-la-liga-matches-2023-to-2024-stats.csv')
kaggle_df = pd.read_csv('la_liga_results_2324.csv')

# Datum till datetime
footstats_df['date'] = pd.to_datetime(footstats_df['date_GMT'], format='%b %d %Y - %I:%M%p')
kaggle_df['date'] = pd.to_datetime(kaggle_df['date'])

# Mapping för namn differenser i de .csv filerna
team_name_mapping = {
    'Athletic Club': 'Athletic Club Bilbao',
    'Osasuna': 'CA Osasuna',
    'Getafe': 'Getafe CF',
    'Girona': 'Girona FC',
    'Granada': 'Granada CF',
    'Las Palmas': 'UD Las Palmas',
    'Mallorca': 'RCD Mallorca',
    'Sevilla': 'Sevilla FC',
    'Valencia': 'Valencia CF',

}

# Normalisera lagnamn med mapping
footstats_df['home_team_name'] = footstats_df['home_team_name'].replace(team_name_mapping)
footstats_df['away_team_name'] = footstats_df['away_team_name'].replace(team_name_mapping)
kaggle_df['hometeam'] = kaggle_df['hometeam'].replace(team_name_mapping)
kaggle_df['awayteam'] = kaggle_df['awayteam'].replace(team_name_mapping)

# Column för features och läggs till possession 
merge_columns = ['date', 'home_team_name', 'away_team_name', 'home_team_possession', 'away_team_possession']

# Välj och byts ut namnet
footstats_df_subset = footstats_df[merge_columns].rename(
    columns={
        'home_team_name': 'hometeam',
        'away_team_name': 'awayteam',
    }
)

# Merging datumet samt lagnamnet
merged_df = pd.merge(
    kaggle_df,
    footstats_df_subset,
    on=['date', 'hometeam', 'awayteam'],
    how='left'
)

#NaN värde i home_yellow_reds och away_yellow_reds
merged_df['home_yellow_reds'] = merged_df['home_yellow_reds'].fillna(0)
merged_df['away_yellow_reds'] = merged_df['away_yellow_reds'].fillna(0)

# Spara nya CSV
output_file_path = 'fixed_merged_la_liga_results.csv'
merged_df.to_csv(output_file_path, index=False)
