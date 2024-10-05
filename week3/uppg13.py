'''
Skapa ett staplat stapeldiagram som visar antalet anställda i varje
Experience_Category för varje Stad.
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sample_data0.csv')

df['Experience_Category'] = pd.cut(df['Years_Experience'], bins=[0,5,10,20], labels=['Low', 'Medium','High'])
experience_per_city = df.groupby(['City','Experience_Category']).size().unstack()

print(experience_per_city)


experience_per_city.plot(kind='bar', figsize=(10,9))
plt.xlabel("City")
plt.ylabel("Number of Employees")
plt.show()