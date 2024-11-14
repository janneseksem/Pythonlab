import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor


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
            tf.keras.layers.Dense(10, activation='relu',), 
            tf.keras.layers.Dense(10, activation='relu'),
            tf.keras.layers.Dense(1, activation='linear')
        ])
        
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
                          loss='mean_squared_error',
                          metrics=['mae'])
        
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train, epochs=100, verbose=1)
    
    def relative_accuracy(self, y_true, y_predict):
        relative_accuracies = [abs(y_t / y_p) / y_t if y_t !=0 else 0 for y_t, y_p in zip(y_true, y_predict)]
        avg_relative_accuracy = 1 - (sum(relative_accuracies) / len(relative_accuracies))
        print(f"Neural Network- Relative Accuracy: {avg_relative_accuracy}")
        
    def evaluate(self, X_test, y_test):
        y_predict = self.model(X_test)
        loss, mae = self.model.evaluate(X_test, y_test, verbose=1)
        print(f"Neural Network- Loss: {loss}, MAE: {mae}")
        self.relative_accuracy(y_test, y_predict)
            
        
    def predict(self, data):
            return self.model.predict(data)

class DecisionTree:
    def __init__(self):
          self.model = DecisionTreeRegressor(random_state=42)
    
    def train(self, X_train, y_train):
         self.model.fit(X_train, y_train)
    
    def relative_accuracy(self, y_true, y_predict):
        relative_accuracies = [abs(y_t / y_p) / y_t if y_t !=0 else 0 for y_t, y_p in zip(y_true, y_predict)]
        avg_relative_accuracy = 1 - (sum(relative_accuracies) / len(relative_accuracies))
        print(f"Decision Tree- Relative Accuracy: {avg_relative_accuracy}")
    
    def evaluate(self, X_test, y_test):
        y_predict = self.model(X_test)
        mae = mean_absolute_error(y_test, y_predict)
        print(f"Decision Tree- MAE: {mae}")
        self.relative_accuracy(y_test, y_predict)

    def predict(self, data):
         return self.model.predict(data)

class RandomForest:
    def __init__(self):
          self.model = RandomForestRegressor(random_state=42)

    def train(self, X_train, y_train):
         self.model.fit(X_train, y_train)

    def relative_accuracy(self, y_true, y_predict):
        relative_accuracies = [abs(y_t / y_p) / y_t if y_t !=0 else 0 for y_t, y_p in zip(y_true, y_predict)]
        avg_relative_accuracy = 1 - (sum(relative_accuracies) / len(relative_accuracies))
        print(f"Random Forest- Relative Accuracy: {avg_relative_accuracy}")

    def evaluate(self, X_test, y_test):
        y_predict = self.model(X_test)
        mae = mean_absolute_error(y_test, y_predict)
        print(f"Random forest- MAE: {mae}")
        self.relative_accuracy(y_test, y_predict)

    def predict(self, data):
         return self.model.predict(data)

class KNearestNeighbors:
    def __init__(self):
          self.model = KNeighborsRegressor(n_neighbors=5)
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def relative_accuracy(self, y_true, y_predict):
        relative_accuracies = [abs(y_t / y_p) / y_t if y_t !=0 else 0 for y_t, y_p in zip(y_true, y_predict)]
        avg_relative_accuracy = 1 - (sum(relative_accuracies) / len(relative_accuracies))
        print(f"K Nearest- Relative Accuracy: {avg_relative_accuracy}")

    def evaluate(self, X_test, y_test):
        y_predict = self.model.predict(X_test)
        mae = mean_absolute_error(y_test, y_predict)
        print(f"K Nearest- Loss: MAE: {mae}")
        self.relative_accuracy(y_test, y_predict)

    def predict(self, data):
         return self.model.predict(data)

def main():
    data_preperation = DataPreperation('home_shots.csv', 'away_shots.csv')
    X_train_home, X_test_home, y_train_home, y_test_home = data_preperation.load_df(target='home')
    ######### NEURAL NETWORK ############    
    #Träna och förutse för Home modellen    
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

    # ###############################
    # ######### DECISION TREE ############
    # dt_model = DecisionTree()
    # dt_model.train(X_train_home, y_train_home)
    # dt_model.evaluate(X_test_home, y_test_home)
    
    # predict_dt_shots = dt_model.predict(today_match_data_scaled)
    # print(f"Decision Tree prediction for Osasuna: {predict_dt_shots}")

    # ###############################
    # ######### RANDOM FOREST ############
    # rf_model = RandomForest()
    # rf_model.train(X_train_home, y_train_home)
    # rf_model.evaluate(X_test_home, y_test_home)

    # predict_rf_shots = rf_model.predict(today_match_data_scaled)
    # print(f"Random Forest prediction for Osasuna: {predict_rf_shots}")

    ###############################
    #####K-Nearest Neighbors#######
    knn_model = KNearestNeighbors()
    knn_model.train(X_train_home, y_train_home)
    knn_model.evaluate(X_test_home, y_test_home)

    opponent_knn_model = KNearestNeighbors()
    opponent_knn_model.train(X_train_opponent_home, y_train_opponent_home)
    opponent_knn_model.evaluate(x_test_opponent_home, y_test_opponent_home)

    predict_knn_shots = knn_model.predict(today_match_data_scaled)
    predict_knn_opponent = opponent_knn_model.predict(today_match_data_scaled)

    print(f"K Nearest prediction for Osasuna: {predict_knn_shots}")
    print(f"K Nearest prediction for opponent: {predict_knn_opponent}")

    predict_knn_total = (predict_knn_shots + predict_knn_opponent) / 2
    print(f"K Nearest predicted shots for Osasuna in today's match against Almeria: {predict_knn_total}") 
    
if __name__ == "__main__":
    main()



'''1.4 Tekniker i Machine Learning

    Neurala nätverk och djupinlärning (deep learning)
    Beslutsträd och slumpmässiga skogar (decision trees and random forests)
    Support Vector Machines (SVM)
    K-Nearest Neighbors (KNN)
    Bayesianska metoder

1.5 Vanliga algoritmer

    Linjär regression
    Logistisk regression
    K-means klustring
    Principal Component Analysis (PCA)
    Convolutional Neural Networks (CNN)
    Recurrent Neural Networks (RNN)
'''