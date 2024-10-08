'''Exercise 2: Binary Classification with Keras

Data: Use the Breast Cancer Wisconsin dataset from Scikit-learn.

Task: Build a neural network for binary classification 
to predict whether a tumor is malignant or benign.

Step:

 Load the Breast Cancer dataset using 
 sklearn.datasets.load_breast_cancer().
 Normalize feature data with sklearn.preprocessing.StandardScaler.
 Create a sequential model in Keras with 
 two dense layers and a binary output.
 Compile the binary cross-entropy loss model 
 and train it on the data.
 Evaluate the accuracy of the model on a test set.
 '''

from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Loading the breast cancer dataset
breast_cancer = load_breast_cancer()

df = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
df['Target'] = breast_cancer.target
#Normalize feature data with sklearn.preprocessing.StandardScaler
X = df.drop('Target', axis=1)
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Keras sequentaial model with 2 dense layers and binary output
model = Sequential()

model.add(Input(shape=(X_train_scaled.shape[1],)))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))

model.add(Dense(1, activation='sigmoid'))


#Compile the binary _crossentropy loss model and train it in data
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, validation_split=0.2)

#Evaluate the accuracy of the model on a test set
from sklearn.metrics import accuracy_score, classification_report
predictions = (model.predict(X_test_scaled) > 0.5).astype(int)

print("Keras model accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))