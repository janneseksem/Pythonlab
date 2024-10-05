'''
Pivota DataFrame:n för att visa genomsnittlig lön för varje 
kombination av Stad och Avdelning.
'''
#City:      Department:         Genomsnittlig lön:
#New york   Marketing           49391

import pandas as pd

df = pd.read_csv('sample_data0.csv')

pivot_table = pd.pivot_table(df, values='Salary', index='City', columns='Department', aggfunc='mean')

print(pivot_table)