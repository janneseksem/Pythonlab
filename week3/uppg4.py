#4.Hitta den anställda med högst prestationspoäng i varje stad.

import pandas as pd
df = pd.read_csv('sample_data0.csv')

highest_salary = df.groupby('City')['Performance_Score'].max()
highest_performers = pd.merge(highest_salary, df, on=['City', 'Performance_Score'], how='inner')



print(highest_performers[['Name', 'City', 'Performance_Score', 'Salary']])

