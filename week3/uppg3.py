#2. Beräkna och visa medianlönen för varje avdelning.
import pandas as pd

df = pd.read_csv('sample_data0.csv')


med_salary = df.groupby('Department')['Salary'].median()

print(med_salary)
