import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
'''

Gör ett cirkeldiagram som visar andelen anställda i 
varje Avdelning.

'''
df = pd.read_csv('sample_data0.csv')

total_employ_department = df.groupby(['Department']).size()
print(total_employ_department)



plt.pie(total_employ_department, labels=total_employ_department.index, autopct='%1.1f%%')

plt.show()

