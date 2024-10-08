'''Data: Use the Boston Housing dataset from Scikit-learn.
Task 1: Linjär regression med Scikit-learn
Task: Create a simple linear regression model to predict 
house prices.

Step:

 Load the Boston Housing dataset using 
 sklearn.datasets.load_boston(). // USE CALIFORNIA HOUSING INSTEAD
 Split the data into training and test sets.
 Create a LinearRegression model and fit it to the training data.
 Make predictions on the test set and 
 calculate the mean square error (MSE).
 '''
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#We load the cali housing dataset
california_housing = fetch_california_housing()

#Convert into pandas dataframe

df = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
df['target'] = california_housing.target

# print(df.head())

#split in features and target variables
X = df.drop('target', axis=1)
y = df['target']

#Split in training and testset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Creating a LinearRegression model
model = LinearRegression()
model.fit(X_train, y_train)

#Make prediction on the test set using MSE
predictions = model.predict(X_test)
accuracy = mean_squared_error(y_test, predictions)
print(f"Models accuracy: {accuracy}")

