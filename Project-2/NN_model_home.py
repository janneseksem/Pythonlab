import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error



class DataPreperation:
    def __init__(self, home_csv, away_csv):
        self.scaler = StandardScaler()
        
        self.home_data = pd.read_csv(home_csv)
        self.away_data = pd.read_csv(away_csv)

    def load_df(self, target):
        
        if target == 'home':
            X = pd.DataFrame({
                'team_shots': self.home_data['team_shots'], 
                'opponent_shots': self.away_data['opponent_shots']
            })
            y = self.home_data['team_shots']

        elif target == 'opponent_home':
            X = pd.DataFrame({
                'team_shots': self.home_data['team_shots'], 
                'opponent_shots': self.away_data['opponent_shots']
            })
            y = self.away_data['opponent_shots']
        # elif target == 'away':
        #      X = pd.DataFrame({
        #           'team_shots': self.away_data['team_shots'],
        #           'opponent_shots': self.home_data['opponent_shots']
        #      })
        #      y = self.away_data['team_shots']

        # elif target == 'opponent_away':
        #      X = pd.DataFrame({
        #           'team_shots': self.away_data['team_shots'],
        #           'opponent_shots': self.home_data['opponent_shots']

        #      })
        #      y = self.home_data['opponent_shots']
        else:
            raise ValueError("Target måste vara 'home' eller 'opponent")
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        return X_train_scaled, X_test_scaled, y_train, y_test
    
    def scaled_today_match_data(self, home_avg_shots, away_avg_opponent_shots):
        today_match_data = pd.DataFrame({
            'team_shots': [home_avg_shots],
            'opponent_shots': [away_avg_opponent_shots]
        })
        return self.scaler.transform(today_match_data)
    
class NeuralNetwork:
    def __init__(self):
        self.model = tf.keras.Sequential([
            tf.keras.Input(shape=(2,)),
            tf.keras.layers.Dense(100, activation='relu',), 
            tf.keras.layers.Dense(100, activation='relu'),
            tf.keras.layers.Dense(1, activation='linear')
        ])
        
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.05),
                          loss='mean_squared_error',
                          metrics=['mae'])
        
    def train(self, X_train, y_train):
            self.model.fit(X_train, y_train, epochs=100, verbose=1)

    def evaluate(self, X_test, y_test):
            y_predict = self.model.predict(X_test)
            mae = mean_absolute_error(y_test, y_predict)
            print(f"Neural Network: Mean absolute error Test set: {mae}")
            
        
    def predict(self, data):
            return self.model.predict(data)
        
def main():
    data_preperation = DataPreperation('home_shots.csv', 'away_shots.csv')
######### NEURAL NETWORK ############    
    #Träna och förutse för Home modellen
    X_train_home, X_test_home, y_train_home, y_test_home = data_preperation.load_df(target='home')
    nn_model = NeuralNetwork()
    nn_model.train(X_train_home, y_train_home)
    nn_model.evaluate(X_test_home, y_test_home)

    #Träna och förutse för Opponent för home modellen 
    #(Prediction for shots allowed from opponent when osasuna is at home)
    X_train_opponent_home, x_test_opponent_home, y_train_opponent_home, y_test_opponent_home = data_preperation.load_df(target='opponent_home')
    opponent_nn_model = NeuralNetwork()
    opponent_nn_model.train(X_train_opponent_home, y_train_opponent_home)
    opponent_nn_model.evaluate(x_test_opponent_home, y_test_opponent_home)

    #Förutse dagens match med genomsnitt på 2 modeller
    home_avg_shots = data_preperation.home_data['team_shots'].mean()
    away_avg_opponent_shots = data_preperation.away_data['opponent_shots'].mean()
    today_match_data_scaled = data_preperation.scaled_today_match_data(home_avg_shots, away_avg_opponent_shots)

    predict_home_shots = nn_model.predict(today_match_data_scaled)
    predict_opponent_away_shots = opponent_nn_model.predict(today_match_data_scaled)
    
    print("Home average shots: ", home_avg_shots)
    print("Away average allow opponent to shoot: ", away_avg_opponent_shots)
    print("-----")
    print("Model prediction at home: ", predict_home_shots)
    print("Model prediction away allow opponent to shoot: ", predict_opponent_away_shots)

    #Förutse av genomsnitt på både predict
    predict_shots_home = (predict_home_shots + predict_opponent_away_shots) / 2
    print(f"Predicted shots for Osasuna in today's match against Almeria: {predict_shots_home}")

###############################
######### DECISION TREE ############

    
    # away_avg_shots = data_preperation.away_data['team_shots'].mean()
    # home_avg_opponent_shots = data_preperation.home_data['opponent_shots'].mean()
    # today_match_data_scaled = data_preperation.scaled_today_match_data(away_avg_shots, home_avg_opponent_shots)

    # predict_away_shots = away_model.predict(today_match_data_scaled)
    # predict_opponent_away_shots = opponent_away_model.predict(today_match_data_scaled)
    
    # print("Home average shots: ", away_avg_shots)
    # print("Away average allow opponent to shoot: ", home_avg_opponent_shots)
    # print("-----")
    # print("Model prediction at home: ", predict_away_shots)
    # print("Model prediction away allow opponent to shoot: ", predict_opponent_home_shots)

    # #Förutse av genomsnitt på både predict
    # predict_shots_away = (predict_away_shots + predict_opponent_home_shots) / 2
    # print(f"Predicted shots for Almeria in today's match against Osasuna: {predict_shots_away}")

if __name__ == "__main__":
    main()



# #Ladda data för specifikt lag i 'home' och 'away' team från csv
# home_shots = pd.read_csv('home_shots.csv')
# away_shots = pd.read_csv('away_shots.csv')

# '''Målet är att vi ska skapa en modell där vi endast 
# förutse hur många skott laget kommer att göra baserad 
# på opponents lag och om laget är home/away'''

# #Definerar labels och Features för hemmaplan, model 1
# X_home = pd.DataFrame({
#     'home_shots': home_shots['team_shots'],
#     'opponent_shots': away_shots['opponent_shots']
# })
# #Osasuna faktiska skott i hemmaplan
# y_home = home_shots['team_shots']

# #Definerar labels och features för motståndarens skott, model 2
# X_opponent = pd.DataFrame({
#     'home_shots': home_shots['team_shots'],
#     'opponent_shots': away_shots['opponent_shots']
# })
# y_opponent = away_shots['opponent_shots']

# #Split train and test med 80% training och 20% testing
# X_train_home, X_test_home, y_train_home, y_test_home = train_test_split(X_home, y_home, test_size=0.2, random_state=42)


# #Normalisera data för model 1
# scaler_home = StandardScaler()
# X_train_scale_home = scaler_home.fit_transform(X_train_home)
# X_test_scale_home = scaler_home.transform(X_test_home)

# #Normalisera data för model 1
# scaler_home = StandardScaler()
# X_train_scale_home = scaler_home.fit_transform(X_train_home)
# X_test_scale_home = scaler_home.transform(X_test_home)

# '''Steg för skapa modell:

# 1. Skapa modellen
# 2. Kompilera modellen
# 3. Träna och utvärdera modellen

# '''

# #Skapa modellen med linear
# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(100, input_dim=2, activation='relu', ),
#     tf.keras.layers.Dense(100, activation='relu', ), 
#     tf.keras.layers.Dense(1, activation='linear')
# ])

# # Kompilera modellen
# model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.05), 
#               loss='mean_squared_error', 
#               metrics=['mae'])

# #Träna modellen
# history = model.fit(X_train_scale, y_train, epochs=150)

# #utvärdera modellen
# y_predict = model.predict(X_test_scale).flatten()
# mae = mean_absolute_error(y_test, y_predict)
# print(f"Mean absolute error Test set: {mae}")

# #Förutse
# model_predict = model.predict(X_test_scale)

# #print(predictions)
# print("Evaluation matrics: ", model.evaluate(X_test_scale, y_test))
# print("Predictions: ", y_predict)
# print("Actual values: ", y_test.values)


# #Få medelvärde data för Osasuna hemmaplan och motståndare mot Almeria i bortaplan
# home_avg_shots = home_shots['team_shots'].mean()
# away_avg_opponent_shots = away_shots['opponent_shots'].mean()

# #Inputs förutse Osasuna idag
# today_match_data_home = pd.DataFrame({
#     'home_shots': [home_avg_shots],
#     'opponent_shots': [away_avg_opponent_shots]
# })


# print(today_match_data_home)
# today_match_data_scaled = scaler.transform(today_match_data_home)
# print(today_match_data_scaled)
# #Förutse antak skott för dagens match
# predicted_shots = model.predict(today_match_data_scaled)
# print(f"Predicted shots for Osasuna in today's match against Almeria: {predicted_shots[0]}")

# '''
# Nästa steg: Plotta med matplot och förbättra accuracy på modellen
# '''

