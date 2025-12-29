
---

# Pythonlab  
**Pythonprogrammering för AI-utveckling - HT24**

---

## Project-2: Modeling for Home/Away Team Shots  

### Introduction  
The project aims to develop a model for predicting the number of shots a team will attempt during a match and the probabilities of achieving specific shot outcomes. By leveraging historical data from the provided CSV files, the model identifies significant patterns and trends affecting team performance.

---

### Start and Test the Program  

**Option 1**:  
1. Download `fixed_merged_la_liga_results.csv`.  
2. Run `team_model_home.py`.

**Option 2**:  
1. Download `la_liga_results_2324.csv` and `spain-la-liga-matches-2023-to-2024-stats.csv`.  
2. Run `csv_merge.py` to create a new file named `fixed_merged_la_liga_results.csv`.  
3. Run `team_model_home.py`.

---

### Data Analysis and Preprocessing  

The dataset from `spain-la-liga-matches-2023-to-2024-stats.csv` (from FootyStats) and `la_liga_results_2324.csv` (acquired from Kaggle) was analyzed for key factors influencing shot attempts.  

**Steps Involved**:
1. **Exploratory Data Analysis**: Identifying key features and trends in the dataset.  
2. **Preprocessing**:
   - Data cleaning.  
   - Handling missing values using `fillna` with median values.  
   - Normalizing variables for better model performance.  
3. **Feature Selection**: Relevant statistics like team performance metrics were selected for model input.

---

### Building the Predictive Model  

**Objective**: Predict the number of shots each team attempts in a match.  
1. **Features**: Includes home and away team shot counts, opponent stats, and other performance metrics.  
2. **Models Used**:
   - **Neural Network**: Trained using backpropagation, adaptive optimizers (e.g., Adam), and improved with techniques like dropout and batch normalization.  
   - **Random Forest**: Used as a comparative model, tuned with a parameter grid to find the best configuration.  
3. **Data Splitting**: The dataset is split into training and test sets.  

---

### Results  

#### Neural Network:  
- **Loss**: 17.66  
- **Mean Absolute Error (MAE)**: 3.27  
- **R² Score**: 0.445  

**Predicted vs Actual Values (First 10 Examples)**:
| **Predicted** | **Actual** |
|---------------|------------|
| 15.63         | 14         |
| 16.91         | 21         |
| 12.18         | 9          |
| 14.21         | 10         |
| 16.07         | 20         |
| 16.50         | 20         |
| 13.07         | 12         |
| 13.02         | 5          |
| 12.28         | 10         |
| 14.87         | 15         |

---

#### Random Forest:  
- **Mean Squared Error (MSE)**: 15.41  
- **Best Parameters**: `{'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 200}`  
- **Best Cross-Validation Score**: 0.498  
- **Train Accuracy**: 91.2%  
- **Test Accuracy (R²)**: 0.516  

**Predicted vs Actual Values (First 10 Examples)**:
| **Predicted** | **Actual** |
|---------------|------------|
| 14.73         | 14         |
| 17.83         | 21         |
| 11.28         | 9          |
| 12.99         | 10         |
| 13.59         | 20         |
| 18.55         | 20         |
| 12.41         | 12         |
| 12.53         | 5          |
| 11.98         | 10         |
| 13.57         | 15         |

---

### Improvements  

1. Handling `NaN` values using `fillna` with median values.  
2. Ensuring proper shape consistency for inputs and outputs.  
3. Using `transform` instead of `fit_transform` to avoid data leakage.  
4. Reducing the number of nodes due to the smaller dataset size.  
5. Adding dropout, batch normalization, and early stopping to improve accuracy.  
6. Hyperparameter tuning with a parameter grid for Random Forest.  
7. Applying one-hot encoding for categorical features.

---

### Summary  

This project leverages neural networks and Random Forest models to predict shot attempts in football matches and derive probabilities based on historical data. The predictive insights generated can help improve team strategy and risk evaluation. Various optimization techniques and hyperparameter tuning were implemented to achieve better model accuracy and performance.

---

## Project-1: Console-Based Blackjack Game  

### Overview  
This project is a simple console-based implementation of the popular card game **Blackjack**.

### How to Play  
1. The rules are implemented within the code.  
2. The game starts immediately: the player is dealt the first and third card, while the dealer receives the second card.  
3. Use the command `hit` to draw another card or `stand` to keep your current hand.  
4. The game ends when either the player or the dealer wins.  
5. After the game ends, the player can choose to play again by entering `y`, or exit the game with `n`.

### Getting Started  
To run the game, simply execute the Python script in a console. Ensure you have **Python 3.x** installed.

---
