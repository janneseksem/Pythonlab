'''
Generera ett par-plot med seaborn för de numeriska kolumnerna i DataFrame:n.
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sample_data0.csv')
numerical_df = df.select_dtypes(include=['float64', 'int64'])


sns.pairplot(numerical_df)
plt.show()

