import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

'''Använd Pandas för att beräkna korrelationsmatrisen för 
numeriska kolumner, använd sedan seaborn för att skapa en 
heatmap av denna matris.'''

# Creating a sample DataFrame
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Column1': [23, 34, 45, 56, 67, 78, 89, 90],
    'Column2': [45, 56, 67, 78, 89, 90, 12, 34],
    'Column3': [67, 78, 89, 90, 12, 34, 56, 78],
    'Column4': [12, 23, 34, 45, 56, 67, 78, 89]
}

df = pd.DataFrame(data)
#print(df)
corr = df.corr()
# print(corr)

plt.figure(figsize=(10,8))
heatmap = sns.heatmap(corr)
heatmap.set_title('Correlation Heatmap')
plt.show()
