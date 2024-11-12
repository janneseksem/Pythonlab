import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from NN_team_shots import get_team_shots

#Ladda data för specifikt lag i 'home' och 'away' team från csv
home_shots = pd.read_csv('home_shots.csv')
away_shots = pd.read_csv('away_shots.csv')

'''Målet är att vi ska skapa en modell där vi endast 
förutse hur många skott laget kommer att göra baserad 
på opponents lag och om laget är home/away'''

#Definerar labels och Features
X = pd.DataFrame({
    #Osasuna historik data för osasuna skott i hemmaplan
    'away_shots': away_shots['team_shots'],
    #Skott från Almeria's motståndaren när almeria är i bortaplan
    'opponent_shots': home_shots['opponent_shots']
})
#Osasuna faktiska skott i hemmaplan
y = away_shots['team_shots']

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
    tf.keras.layers.Dense(64, input_dim=2, activation='relu',),
    tf.keras.layers.Dense(32, activation='relu', ), 
    tf.keras.layers.Dense(16, activation='relu', ),
    tf.keras.layers.Dense(1, activation='linear')
])

# Kompilera modellen
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.05), 
              loss='mean_squared_error', 
              metrics=['mae'])

#Träna modellen
model.fit(X_train_scale, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=0)

#utvärdera modellen
y_predict = model.predict(X_test_scale).flatten()
mae = mean_absolute_error(y_test, y_predict)
print(f"Mean absolute error Test set: {mae}")

#Förutse
model_predict = model.predict(X_test_scale)

#print(predictions)
print("Evaluation matrics: ", model.evaluate(X_test_scale, y_test))
print("Predictions: ", y_predict)
print("Actual values: ", y_test.values)


#Få medelvärde data för Almeria bortaplan och motståndare mot Osasuna i hemmaplan
away_avg_shots = away_shots['team_shots'].mean()
home_avg_opponent_shots = home_shots['opponent_shots'].mean()

#Inputs förutse Osasuna idag
today_match_data_away = pd.DataFrame({
    'away_shots': [away_avg_shots],
    'opponent_shots': [home_avg_opponent_shots]
})

today_match_data_scaled = scaler.transform(today_match_data_away)

#Förutse antal skott för dagens match
predicted_shots = model.predict(today_match_data_scaled)
print(f"Predicted shots for Almeria in today's match against Osasuna: {predicted_shots[0]}")

