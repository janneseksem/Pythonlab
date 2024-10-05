'''Skapa en 2x2 subplot med olika typer av diagram 
(linje, spridning, stapel och histogram) 
med data från DataFrame:n.'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sample_data0.csv')

fig, axes = plt.subplots(2, 2, figsize=(10,8))

sns.scatterplot(data=df, x='Performance_Score', y='Department', ax=axes[0,0])
axes[0, 0].set_title('Scatter Plot')
sns.histplot(data=df, x='Performance_Score', ax=axes[0,1])
axes[0, 1].set_title('History Plot')
sns.barplot(data=df, x='Department', y='Performance_Score', ax=axes[1,0])
axes[1, 0].set_title('Bar Plot')
sns.pointplot(data=df, x='Department', y='Performance_Score', ax=axes[1,1])
axes[1, 1].set_title('Point Plot')

plt.tight_layout()

plt.show()