'''
Använd scikit-learn:s train_test_split-funktion för att dela 
upp data i tränings- och testuppsättningar. 
Använd 'Salary' som målvariabel och 'Age', 'Years_Experience' 
och 'Performance_Score' som egenskaper.
'''
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('sample_data0.csv', encoding='latin-1')

#Features
X = df[['Age', 'Years_Experience', 'Performance_Score']]
y = df['Salary'] # Target variable

#Makes sure non values from salary drops
X = X.dropna(subset=['Performance_Score'])
y = y[X.index] #Make sure target 'Salary' aligns with the cleaned data

#Use train_test_split to split the dataset

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Features (X_train): ")
print(X_train)
print("\nTraining Features (y_train): ")
print(y_train)

print("\nTest Features (X_test): ")
print(X_test)
print("\nTest Features (y_test): ")
print(y_test)