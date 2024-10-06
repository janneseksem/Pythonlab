from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

'''
Träna en enkel linjär regressionsmodell med scikit-learn för att 
förutsäga 'Salary' baserat på 'Years_Experience'. 
Plotta regressionslinjen tillsammans med ett spridningsdiagram 
av data.
'''

df = pd.read_csv('sample_data0.csv')
#Prepare for features (x) and target (y)
X = df['Years_Experience']
y = df['Salary']

#Handle missing values
df = df.dropna(subset=['Salary'])


#Prepare the features and target again after dropping rows with Nan in Salary
X = df['Years_Experience']
y = df['Salary']

#Reshape X as 2D array
X = X.values.reshape((-1, 1))

#split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=24)

#initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

#Make prediction on the test set
y_pred = model.predict(X_test)

print("Predicted Salaries:", y_pred)
plt.figure(figsize=(10,8))
plt.xlabel('Years Experience')
plt.ylabel('Salaries')
plt.scatter(X_test, y_test, color ='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', label='Regression Line')


plt.show()