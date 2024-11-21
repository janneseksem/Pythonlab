import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error


'''
SMALL DATASET?
'''

class DataPreperation:
    def __init__(self, merged_csv):
        self.scaler = StandardScaler()
        self.df = pd.read_csv(merged_csv)

    def OneHot(self):
         #Konvertera date till numeric med UNIX timestamp
         #annars drop om det ej finns nummer kolumn
        if 'date' in self.df.columns:
            self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
            self.df['date_numeric'] = self.df['date'].astype(np.int64) // 10**9
            self.df.drop(columns=['date'], inplace=True)

        #One hot koda dataframe
        self.df = pd.get_dummies(self.df, drop_first=True)

        # Drop
        self.df = self.df.select_dtypes(include=[np.number])

        #NaN fylls med 0
        self.df.fillna(0, inplace=True)

    def load_df(self):
            self.OneHot()
            
            X = self.df.drop('home_total_shots', axis=1)
            y = self.df['home_total_shots']

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            X_train_scaled = self.scaler.fit_transform(X_train)
            X_test_scaled = self.scaler.transform(X_test)
            return X_train_scaled, X_test_scaled, y_train, y_test

class NeuralNetwork:
    def __init__(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(100, activation='elu',), 
            tf.keras.layers.Dense(100, activation='elu'),
            tf.keras.layers.Dense(1, activation='linear')
        ])
        
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.05),
                          loss='mean_squared_error',
                          metrics=['mae'])
        
    def train(self, X_train, y_train):
        history = self.model.fit(X_train, y_train, epochs=100, verbose=0)
        return history

        
    def evaluate(self, X_test, y_test):
        y_predict = self.model.predict(X_test)
        loss, mae = self.model.evaluate(X_test, y_test, verbose=1)
        r2 = r2_score(y_test, y_predict)
        print(f"Neural Network- Loss: {loss}, MAE: {mae}, r2: {r2}")
        
    def predict(self, data):
            return self.model.predict(data)

def main():

    data_preperation = DataPreperation('fixed_merged_la_liga_results.csv')
    X_train_home, X_test_home, y_train_home, y_test_home = data_preperation.load_df()

    # ######## NEURAL NETWORK ############
    # Neural Network- Loss: 28.1712589263916, 
    # MAE: 4.265266418457031, r2: 0.11563318967819214   
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