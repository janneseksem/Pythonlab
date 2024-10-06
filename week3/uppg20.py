'''
Använd Pandas för att gruppera data efter 'City' och 'Department'
beräkna genomsnittlig 'Salary' för varje grupp, 
använd sedan dessa data för att skapa ett grupperat 
stapeldiagram med Matplotlib.
'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('sample_data0.csv')

data_department = df.groupby(['City','Department'])['Salary'].mean()
# print(data_department)

group_data = data_department.unstack()

group_data.plot(kind='bar', figsize=(10,8))

plt.title('Median of Average Salaries each department each cities in USA')
plt.xlabel=('Cities')
plt.ylabel=('Average salaries')

plt.show()

