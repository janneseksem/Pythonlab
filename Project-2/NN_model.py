import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from tensorflow.keras import regularizers
from NN_team_shots import get_data_prediction

#Ladda data för specifikt lag i 'home' och 'away' team
home_team = 'CA Osasuna'
away_team = 'Almería'

'''Målet är att vi ska skapa en modell där vi endast 
förutse hur många skott laget kommer att göra baserad 
på opponents lag och om laget är home/away'''

#Få shot datan för speciferad lag
#Baserad på home och away
home_team_shots, away_team_shots = get_data_prediction(home_team, away_team)

#Definerar labels och Features

X = np.concatenate((home_team_shots['opponent_shots'].values.reshape(-1, 1),
                    away_team_shots['opponent_shots'].values.reshape(-1, 1)), axis=0)
y = np.concatenate((home_team_shots['team_shots'].values,
                    away_team_shots['team_shots'].values), axis=0)

#Split train and test med 80% training och 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#Normalisera data
scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)


'''Steg för skapa modell:

1. Skapa modellen
2. Kompilera modellen
3. Träna och utvärdera modellen

'''

#Skapa modellen med linear
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.01), input_shape=(1,)),
    tf.keras.layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01)), 
    tf.keras.layers.Dense(16, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    tf.keras.layers.Dense(1, activation='linear')
])

# Kompilera modellen
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.05), 
              loss='mean_squared_error', 
              metrics=['mae'])

#Träna modellen
model.fit(X_train_scale, y_train, epochs=200, batch_size=64, validation_split=0.2, verbose=1)

#utvärdera modellen
y_predict = model.predict(X_test)
mae = mean_absolute_error(y_test, y_predict)
print(f"Mean absolute error Test set: {mae}")

#Exempel förutse: Predict shots Osasuna kommer göra i hemma plan mot Almeria i bortaplan
opponent_shots_example = np.array([[away_team_shots['opponent_shots'].mean()]])
opponent_shots_example_scaled = scaler.transform(opponent_shots_example)
predicted_shots_osassuna = model.predict(opponent_shots_example_scaled)
print(f"Prediction shots for Osasuna at home against Almera: {predicted_shots_osassuna[0][0]}")

# #förutse
model_predict = model.predict(X_test_scale[0:])

#print(predictions)

print(model.evaluate(X_test_scale, y_test))

print(model_predict[0:10])
print(y_test[0:10])

