'''Använd funktionen pd.melt() för att omforma DataFrame:n, 
och gör 'Salary' och 'Performance_Score'
kolumnerna till variabler.'''

import pandas as pd

df = pd.read_csv('sample_data0.csv')

df_melt = pd.melt(df, value_vars=['Salary', 'Performance_Score'])

print(df_melt)