import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

'''
Skapa en NumPy-array med slumpmässiga tal, använd sedan 
Pandas för att skapa en DataFrame från denna array och 
Matplotlib för att plotta ett histogram av värdena.
'''

arr = np.random.normal(0,10, 250)
# print(arr)

df = pd.DataFrame(arr)
# print(df)

plt.hist(df)

plt.show()