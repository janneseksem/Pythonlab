'''Exercise 3: Multi-class classification with TensorFlow

Data: Use the Iris dataset from Scikit-learn.

Task: Create a TensorFlow multi-class classification model 
to predict the species of irises.

Step:

 Load the Iris dataset using sklearn.datasets.load_iris().
 One-hot encode the target variable.
 Build a TensorFlow model using the Keras API 
 with appropriate layers for multi-class classification.
 Train the model and plot the training history (accuracy and loss).
 Make predictions on a test set and create a confusion matrix.
 '''

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn import metrics

#Loading the Iris dataset
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
#Find appropriate Column names
#print(iris.target_names) /output: ['setosa' 'versicolor' 'virginica']

df['Target'] = iris.target

iris_encoder = OneHotEncoder(sparse_output=False) #Set sparse=False to get dense array
encoded_target = iris_encoder.fit_transform(df[['Target']])
encoded_target_df = pd.DataFrame(encoded_target, columns=['setosa', 'versicolor', 'virginica'])

#Concatenate the encoded target back to the original dataframe
df = pd.concat([df, encoded_target_df], axis=1)

#Build a Tensorflow using Keras API

X = df.drop(['Target', 'setosa', 'versicolor', 'virginica'], axis=1)
y = encoded_target #Using the one-hot encoded target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Normalise data by using StandardScaler()
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

keras_model = Sequential()

keras_model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
keras_model.add(Dense(64, activation='relu'))
keras_model.add(Dense(3, activation='softmax')) #For multi-class classification activation function should be softmax, 3 output units for multiclass classification

keras_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) #for multiclass, loss function: categorical_crossentropy
keras_model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, validation_split=0.2)

#Model accuracy. When using multiclass, using argmax to determine which class has the highest probability
keras_prediction = np.argmax(keras_model.predict(X_test_scaled), axis=1)
#Convert one-hot encoded y_test back to class labels for evaluation
y_test_labels = np.argmax(y_test, axis=1)

print("Keras model accuracy:", accuracy_score(y_test_labels, keras_prediction))
print(classification_report(y_test_labels, keras_prediction))

#Creating confusion matrix
confusion_matrix = metrics.confusion_matrix(y_test_labels, keras_prediction)
print("Confusion Matrix:")
print(confusion_matrix)

