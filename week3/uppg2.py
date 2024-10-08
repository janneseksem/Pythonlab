#1. Ladda filen 'sample_data0.csv' och visa de sista 10 raderna.

import pandas as pd

df = pd.read_csv('sample_data0.csv')
#print(df)

print(df.tail(10))

