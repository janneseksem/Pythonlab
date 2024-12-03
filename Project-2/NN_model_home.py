import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report


#Class som förbereder data och kolla null värden
class DataPreperation:
    def __init__(self, merged_csv):
        self.scaler = StandardScaler()
        self.df = pd.read_csv(merged_csv)
    #One hot coding 
    def OneHot(self):
        self.df = pd.get_dummies(self.df)

        X = self.df.drop('home_total_shots', axis=1)
        y = self.df['home_total_shots']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        #Lösa alla null i .csv
        missing_cols = X_train.columns[X_train.isnull().any()]
        X_train = X_train.drop(columns=missing_cols)
        X_test = X_test.drop(columns=missing_cols)

        # #Lösa alla null i .csv alt.2
        # X_train = X_train.fillna(0)
        # X_test = X_test.fillna(0)

        #Scaling
        X_train_scaled = pd.DataFrame(self.scaler.fit_transform(X_train), columns=X_train.columns)
        X_test_scaled = pd.DataFrame(self.scaler.fit_transform(X_test), columns=X_test.columns)
        X_train_scaled.dropna(axis=1, inplace=True)
        X_test_scaled.dropna(axis=1, inplace=True)

        return X_train_scaled, X_test_scaled, y_train, y_test
    
#Class för Neural Network modellen
class NeuralNetwork:
    def __init__(self):
        #Skapa modellen
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(100, activation='relu',), 
            tf.keras.layers.Dense(100, activation='relu'),
            tf.keras.layers.Dense(1)
        ])
        
        self.model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.05),
                          loss='mean_squared_error',
                          metrics=['mae'])
        
    #Träna
    def train(self, X_train, y_train):
        history = self.model.fit(X_train, y_train, epochs=100, verbose=0)
        return history
    
    #Visa rapport om modellen, return predict
    def evaluate(self, X_test, y_test):
        y_predict = self.model.predict(X_test)
        loss, mae = self.model.evaluate(X_test, y_test, verbose=1)
        r2 = r2_score(y_test, y_predict)
        print(f"Neural Network- Loss: {loss}, MAE: {mae}, r2: {r2}")
        return y_predict
    
#Class för Random Forest modellen
class RandomForest:
    def __init__(self):
        #Parameter grid
        self.param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
         }
        self.grid_search = None

    #Träna modellen
    def train(self, X_train, y_train):
        rf = RandomForestRegressor(random_state=42)
        self.grid_search = GridSearchCV(estimator=rf, param_grid=self.param_grid, cv=5, n_jobs=-1, verbose=2, scoring='r2')
        self.grid_search.fit(X_train, y_train)
        return self.grid_search
    
    #Visa rapport om modellen, return predict
    def evaluate(self, X_test, y_test):
        if self.grid_search is not None:
             
            best_model = self.grid_search.best_estimator_
            y_predict = best_model.predict(X_test)
            mse = mean_squared_error(y_test, y_predict)
            print(f"Random Forest- MSE: {mse}")
        else:
             print("WARNING: Train the model first")
    


def main():
    #Ladda .csv in i vår class
    data_preperation = DataPreperation('fixed_merged_la_liga_results.csv')
    X_train_home, X_test_home, y_train_home, y_test_home = data_preperation.OneHot()
    '''
    Gör Comment out härifrån fram till Random Forest för testa fram Neural Network
    '''
    ######## NEURAL NETWORK ############
    #Neural Network- Loss: 37.224037170410156, 
    #MAE: 4.906871795654297, r2: -0.16855597496032715
    #Träna och förutse för Home modellen
    
    nn_model = NeuralNetwork()
    nn_history = nn_model.train(X_train_home, y_train_home)
    predict_test_home_shots = nn_model.evaluate(X_test_home, y_test_home)
    # home_avg_shots = data_preperation.df['team_shots'].mean()

    #Förutse hela test settet
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
    
    # #########RANDOM FOREST##########
    # rf_model = RandomForest()
    # grid_search = rf_model.train(X_train_home, y_train_home)
    # rf_model.evaluate(X_test_home, y_test_home)

    # #Skrivs ut bästa parametrar och score
    # print("Bästa parametrar:", grid_search.best_params_)
    # print("Bästa cross-validation score:", grid_search.best_score_)
    # print(f"Train Accuracy: {grid_search.score(X_train_home, y_train_home):.3f}")
    # print(f"Test Accuracy (r2): {grid_search.score(X_test_home, y_test_home):.3f}")

    # #utför bästa modellenn på test datan (X_test)
    # rf_y_predict = grid_search.best_estimator_.predict(X_test_home)

    # #Förutse hela test settet
    # rf_y_predict = np.array(rf_y_predict)
    # rf_actual_test_shots = np.array(y_test_home)
    # print("Predicted and actual values (first 10 example):")
    # print("Predicted: \n", rf_y_predict[:10])
    # print("Actual: \n", rf_actual_test_shots[:10])

    # #Plotta GridSearchCV resultat med MTS v Hyperparameterna
    # results = pd.DataFrame(grid_search.cv_results_)
    # plt.figure(figsize=(10,7))
    # plt.scatter(results['param_n_estimators'], results['mean_test_score'], c=results['param_max_depth'], cmap='viridis')
    # plt.colorbar(label='max_depth')
    # plt.xlabel('n_estimators')
    # plt.ylabel('Mean test score')
    # plt.title('GridSearchCV Results')
    # plt.show()

    # #plot training data
    # xAxis = tf.range(0, len(X_test_home))
    # xAxis, y_test_home[0:len(X_test_home)]
    # xAxis = tf.range(0, len(X_test_home))
    # yAxis = y_test_home.to_numpy()
    # yAxis = tf.cast(yAxis, tf.float32)
    # shot_modelPredictYAxis = tf.cast(rf_y_predict, tf.float32)

    # plt.figure(figsize=(10,7))
    # plt.scatter(xAxis, yAxis, c='g', label="Test data")
    # #plot TEST data
    # plt.scatter(xAxis, shot_modelPredictYAxis, c='r', label="predictions")
    # #plot predictions
    # plt.legend()
    # plt.show()


if __name__ == "__main__":
    main()
