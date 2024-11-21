import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import statsmodels.api as sm

'''
SMALL DATASET??
Modeller som kan funka:
- Random Forest
- Decision Trees
- Support vector machines
- K-Nearest Neighbors
- Poisson regression
- Linear Regression

'''
'''
Ladda 2 skapade .csv för skapa modell med:
- Antal skott Hemmalaget har gjort
- Antal skott Bortalaget tar emot skott från motståndaren har gjort
- Medelvärdet på hur mycket motståndaren skjuter & 
tar emot skott när de är bortalaget
Exempelvis:
Osasuna har gjort 18,11,16.... skott 
column team_shots i home_shots.csv

Almerias som är bortaplan har motståndaren skjutit mot Almeria 
15,30,19 osv column opponent_shots i away_shots.csv

Matchen när Osasuna har gjort 18 skott är mot Athletic club 
i bortaplan har medelvärdet 12,58 som låter hemma laget skjuta 
mot Athletic club

För förutse antal skott Osasuna gör mot Almera skapas:
model 1 för Osasuna skott i hemmaplan
model 2 för Almerias i bortaplan för motståndarens tillåtna 
skott mot Almeria

Adderar 2 modeller och delar med 2 för få fair nummer på hur mycket
Osasuna i hemmaplan gör mot Almeria

Plotta med matplotlib

EXTRA?:
'''

class DataPreperation:
    def __init__(self, merged_csv):
        self.scaler = StandardScaler()
        self.df = pd.read_csv(merged_csv)

    def preprocess_data(self):
         # Convert the date column to a numerical feature (e.g., UNIX timestamp or drop it)
        if 'date' in self.df.columns:
            self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
            self.df['date_numeric'] = self.df['date'].astype(np.int64) // 10**9  # UNIX timestamp
            self.df.drop(columns=['date'], inplace=True)

        # Drop any remaining non-numeric columns
        self.df = self.df.select_dtypes(include=[np.number])

        # Handle missing values by filling with 0
        self.df.fillna(0, inplace=True)

    def load_df(self):
            self.preprocess_data()
            
        
            X = self.df.drop('home_total_shots', axis=1)
            y = self.df['home_total_shots']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            X_train_scaled = self.scaler.fit_transform(X_train)
            X_test_scaled = self.scaler.transform(X_test)
            return X_train_scaled, X_test_scaled, y_train, y_test

class NeuralNetwork:
    def __init__(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(100, activation='relu',), 
            tf.keras.layers.Dense(100, activation='relu'),
            tf.keras.layers.Dense(1)
        ])
        
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
                          loss='mean_squared_error',
                          metrics=['mae'])
        
    def train(self, X_train, y_train):
        history = self.model.fit(X_train, y_train, batch_size=32, epochs=100, verbose=1)
        return history

        
    def evaluate(self, X_test, y_test):
        y_predict = self.model.predict(X_test)
        y_predict = np.array(y_predict, dtype=np.float32)
        loss, mae = self.model.evaluate(X_test, y_test, verbose=1)
        r2 = r2_score(y_test, y_predict)
        print(f"Neural Network- Loss: {loss}, MAE: {mae}, r2: {r2}")
            
        
    def predict(self, data):
            return self.model.predict(data)

    
def main():

    data_preperation = DataPreperation('fixed_merged_la_liga_results.csv')
    X_train_home, X_test_home, y_train_home, y_test_home = data_preperation.load_df()

    # ######## NEURAL NETWORK ############    
    # #Träna och förutse för Home modellen
    #    
    nn_model = NeuralNetwork()
    nn_history = nn_model.train(X_train_home, y_train_home)
    nn_model.evaluate(X_test_home, y_test_home)
    # home_avg_shots = data_preperation.df['team_shots'].mean()

    #Förutse hela test settet
    predict_test_home_shots = nn_model.predict(X_test_home)
    predict_test_home_shots = np.array(predict_test_home_shots)
    actual_test_home_shots = np.array(y_test_home)

    print("\nPredicted and Actual values (first 10 ex):")
    print("Predicted:\n", predict_test_home_shots[:10])
    print("Actual:\n", actual_test_home_shots[:10])

    # print("Home average shots: ", home_avg_shots)
    # print("Away average allow opponent to shoot: ", away_avg_opponent_shots)
    # print("Model prediction away allow opponent to shoot: ", predict_opponent_away_shots)

    #Förutse av genomsnitt på både predict
    # predict_shots_home = (predict_home_shots + predict_opponent_away_shots) / 2
    # print(f"Predicted shots for Osasuna in today's match against Almeria: {predict_shots_home}")

    #Plot history (Loss curve)
    plt.figure(figsize=(10,7))
    plt.plot(nn_history.history['loss'], label='Loss training')
    plt.ylabel("loss")
    plt.xlabel("epochs")
    plt.legend()
    plt.show()

    #plot training data
    xAxis = tf.range(0, len(X_test_home))
    xAxis, y_test_home[0:len(X_test_home)]

    xAxis = tf.range(0, len(X_test_home))

    yAxis = y_test_home.to_numpy()
    yAxis = tf.cast(yAxis, tf.float32)
    shot_modelPredictYAxis = tf.cast(predict_test_home_shots, tf.float32)
    
    plt.figure(figsize=(10,7))
    plt.scatter(xAxis, yAxis, c='g', label="Test data")
    #plot TEST data
    plt.scatter(xAxis, shot_modelPredictYAxis, c='r', label="predictions")
    #plot predictions
    plt.legend()
    plt.show()
    

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