import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''

Skapa ett violindiagram som jämför fördelningen av 
Performance_Scores över olika Avdelningar.
'''

df = pd.read_csv('sample_data0.csv')


ax = sns.violinplot(x='Performance_Score', y='Department', data=df)
plt.show()