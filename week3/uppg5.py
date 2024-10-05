#5. skapa en ny kolumn 'Lön_per_År_Erfarenhet' 
# genom att dividera 'Salary' med 'Years_Experience'. 
# Hantera eventuella division-med-noll-fel.

import pandas as pd

df = pd.read_csv('sample_data0.csv')

df['Lön_per_År_Erfarenhet'] = df['Salary'] / df['Years_Experience']
df['Lön_per_År_Erfarenhet'] = df['Lön_per_År_Erfarenhet'].replace([float('inf'), -float('inf')], float('nan'))

print(df)

