import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

######RANDOM FOREST##########
# Bästa cross-validation score: 0.5033404958347004
# Train Accuracy: 0.838
# Test Accuracy (r2): 0.524
# Mean Squared Error: 15.15390049141198

# Ladda vår data till Dataframe
df = pd.read_csv('fixed_merged_la_liga_results.csv')

# one-hot coding till Features/Labels 
df_one_hot = pd.get_dummies(df)

#Definerar X som Feature och y som Label
X = df_one_hot.drop('home_total_shots', axis=1)
y = df_one_hot['home_total_shots']

# print(f'X: {X.shape}')

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Identifera null värden (finns vid yellow_red kolumn)
missing_cols = X_train.columns[X_train.isnull().any()]
X_train = X_train.drop(columns=missing_cols)
X_test = X_test.drop(columns=missing_cols)

# print(f"X_train : {X_train.shape}")
# print(f"y_train : {y_train.shape}")
# print(f"X_test : {X_test.shape}")
# print(f"y_test : {y_test.shape}")

#Normalisera datan
scaler = StandardScaler()
X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)

# Ta bort missing values
X_train_scaled.dropna(axis=1, inplace=True)
X_test_scaled.dropna(axis=1, inplace=True)

#Definerar parameterrutnät för tuning
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Skapar RandomforestClassifier
rf = RandomForestRegressor(random_state=42)

#Utförs GridSearchCV
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=1, scoring='r2')
grid_search.fit(X_train_scaled, y_train)

#Skrivs ut bästa parametrar o score
print("Bästa parametrar:", grid_search.best_params_)
print("Bästa cross-validation score:", grid_search.best_score_)
print(f"Train Accuracy: {grid_search.score(X_train_scaled, y_train):.3f}")
print(f"Test Accuracy (r2): {grid_search.score(X_test_scaled, y_test):.3f}")

#Utför bästa modellen på test datan (X_test)
best_model = grid_search.best_estimator_
y_predict = best_model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_predict)
print("Mean Squared Error:", mse)

#Förutse hela test settet
y_predict = np.array(y_predict)
actual_test_home_shots = np.array(y_test)
print("\nPredicted and Actual values (first 10 ex):")
print("Predicted:\n", y_predict[:10])
print("Actual:\n", actual_test_home_shots[:10])

#Plotta GridSearchCV resultat med MTS v Hyperparameterna
results = pd.DataFrame(grid_search.cv_results_)
plt.figure(figsize=(10,7))
plt.scatter(results['param_n_estimators'], results['mean_test_score'], c=results['param_max_depth'], cmap='viridis')
plt.colorbar(label='max_depth')
plt.xlabel('n_estimators')
plt.ylabel('Mean test score')
plt.title('GridSearchCV Results')
plt.show()

#plot training data
xAxis = tf.range(0, len(X_test))
xAxis, y_test[0:len(X_test)]
xAxis = tf.range(0, len(X_test))
yAxis = y_test.to_numpy()
yAxis = tf.cast(yAxis, tf.float32)
shot_modelPredictYAxis = tf.cast(y_predict, tf.float32)

plt.figure(figsize=(10,7))
plt.scatter(xAxis, yAxis, c='g', label="Test data")
#plot TEST data
plt.scatter(xAxis, shot_modelPredictYAxis, c='r', label="predictions")
#plot predictions
plt.legend()
plt.show()