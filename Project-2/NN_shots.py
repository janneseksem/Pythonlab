import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import regularizers


df = pd.read_csv('england-premier-league-matches-2018-to-2019-stats.csv')

#print(df.head())

df = df.drop(columns=['date_GMT', 'status', 'referee', 'stadium_name', 'home_team_goal_timings', 'away_team_goal_timings'])

'''Målet är att vi ska skapa en modell där vi endast 
förutse hur många skott laget kommer att göra baserad 
på opponents lag och om laget är home/away'''

#Skapar mean function där hur många skott varje match laget gör
#Baserad på home och away

df['home_team_avg_shots_allowed'] = df.groupby('away_team_name')['home_team_shots'].transform('mean')
df['away_team_avg_shots_allowed'] = df.groupby('home_team_name')['away_team_shots'].transform('mean')

#Skapa target variabel om laget är Home eller Away
df['Total_Shots'] = df.apply(lambda row: row['home_team_shots'] if row['home_team_shots'] is not None else row['away_team_shots'], axis=1)

#One Hot code 
df_one_hot_code = pd.get_dummies(df, columns=['home_team_name', 'away_team_name'])
# print(df_one_hot_code.head())

#Definerar labels och features

X = df_one_hot_code.drop(['Total_Shots', 'home_team_shots', 'away_team_shots'], axis=1)
y = df_one_hot_code['Total_Shots']

#Split train and test med 80% training och 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Verifera nummer av features
print(f"Shape of X_train after encoding: {X_train.shape}")

# #Använda bara nummer kolumn innan scaling (non-numeric data error)
# numeric_col = X_train.select_dtypes(include=['number']).columns
# X_train_num = X_train[numeric_col]
# X_test_num = X_test[numeric_col]

#Normalisera data
scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

#Kolla shape av normaliseringsdata - Output: Shape of X_train_scale: (304, 58)
print(f"Shape of X_train_scale: {X_train_scale.shape}")

'''Steg för skapa modell:

1. Skapa modellen
2. Kompilera modellen
3. Träna och utvärdera modellen

'''

#Skapa modellen med linear
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.01), input_shape=(X_train_scale.shape[1],)),
    tf.keras.layers.Dropout(0.3),  # Add a dropout layer to prevent overfitting
    tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.01)), 
    tf.keras.layers.Dropout(0.3),  # Add a dropout layer to prevent overfitting
    tf.keras.layers.Dense(1, activation='linear')
])

# Kompilera modellen

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.05), 
              loss='mean_squared_error', 
              metrics=['mae'])

#Träna modellen

model.fit(X_train_scale, y_train, epochs=200, batch_size=64, validation_split=0.2, verbose=1)

#utvärdera modellen

loss, mae = model.evaluate(X_test_scale, y_test)
print(f'Mean Absolute Error test accuracy: {mae}')

#förutse
model_predict = model.predict(X_test_scale[0:])

#print(predictions)

print(model.evaluate(X_test_scale, y_test))

print(model_predict[0:10])
print(y_test[0:10])

