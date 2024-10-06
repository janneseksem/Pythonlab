from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

'''Skapa ett program som använder pandas, numpy och matplotlib 
för att analysera och visualisera data från en CSV-fil 
med aktiemarknadsdata. Programmet ska:

    Läsa in data och förbehandla den (hantera saknade värden, etc.)

    Beräkna rullande medelvärden och standardavvikelser

    Identifiera trender och anomalier

    Skapa visualiseringar som linjediagram, histogram 
    och scatterplots

    Spara resultaten i en ny CSV-fil och bilderna som PNG-filer

    Implementera en enkel linjär regression

'''
#Reading in data from .csv
df = pd.read_csv('stock_data_large.csv')



#Handling missing values
df = df.dropna()

#convert date to datetime formating
df['Date'] = pd.to_datetime(df['Date'])
#Rolling mean values
df['Rolling_Close_Mean'] = df['Close'].rolling(window=3).mean()
#Standard deviaion
df['Rolling_Standard_Deviation'] = df['Close'].rolling(window=3).std()


# print(df[['Close', 'Rolling_Close_Mean', 'Rolling_Standard_Deviation']])

#Identify trends methods, Moving average 5 and Moving average 20
#Making dates as the index
df.set_index('Date', inplace=True)

#Making Trend Moving Average 5 (sum of closing prices divided by five which needs atleast 5 data dates to return value)
df['MA_5'] = df['Close'].rolling(window=5).mean()
# print(df['MA_5'])

#Making Trend moving Average 20 (sum of closing prices divided by 20, which needs 20 data dates atleast to return value)
df['MA_20'] = df['Close'].rolling(window=20).mean()
# print(df['MA_20'])

#Identify normalization with Z-score method
#Calculate mean
mean = np.mean(df['Close'])

# print(mean)
#Calculate standard deviation
std_dev = np.std(df['Close'])

z_scores = (df['Close'] - mean) / std_dev

print("Orginal data:", df['Close'])
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("Z Score:", z_scores)

df['Z_Score'] = z_scores

print(df[['Close', 'Z_Score']])

#Finding anomalies flags as it over 3 and less than -3
anomaly_threshold = 3

df['Anomaly'] = np.where(np.abs(df['Z_Score']) > anomaly_threshold, True, False)
print(df[df['Anomaly']])

#Plotting to diagrams
fig, axes = plt.subplots(2, 2, figsize=(10,8))

sns.scatterplot(x=df.index, y=df['Close'], ax=axes[0,0], color='orange', s=50)
axes[0,0].set_title=('Scatter plot on Closing Prices')
axes[0,0].set_xlabel=('Date of closing price')
axes[0,0].set_title=('Closing price')
axes[0,0].tick_params(axis='x', rotation=45)

#lineplot with trends
axes[0,1].plot(df.index, df['Close'], color='blue', label='Close price')
axes[0,1].plot(df.index, df['MA_5'], color='yellow', label='5 day MA')
axes[0,1].plot(df.index, df['MA_20'], color='green', label='20 day MA')
axes[0,1].set_title=('Line plot on Closing Prices')
axes[0,1].set_xlabel=('Date of closing price')
axes[0,1].set_title=('Closing price')
axes[0,1].tick_params(axis='x', rotation=45)
axes[0,1].legend()

sns.histplot(df['Close'], bins=20, ax=axes[1,0], color='skyblue')
axes[1,0].set_title=('Histogram plot on Closing Prices')
axes[1,0].set_xlabel=('Close price')
axes[1,0].set_title=('Frequency')


#Anomaly scatter plot with z-scores
sns.scatterplot(x=df.index, y=df['Z_Score'], label='Closing prices', color='blue', s=50, ax=axes[1,1])
axes[1,1].axhline(y=3, color='red', linestyle='--', label='Threshold 3')
axes[1,1].axhline(y=-3, color='red', linestyle='--', label='Threshold -3')
axes[1,1].set_title('Scatter plot on Closing prices')
axes[1,1].xlabel = ('Date')
axes[1,1].ylabel = ('Z-score')
axes[1,1].tick_params(axis='x', rotation=45)
axes[1,1].legend()


#Plot results and saves it into .PNG and .CSV
plt.tight_layout()
plt.savefig('aktier.png', bbox_inches='tight')


df.to_csv('stock_analysis_result.csv', index=True)

#Implement a linear regression
df = df.dropna()

X = df[['Open', 'High', 'Low', 'Volume', 'MA_5', 'MA_20']]
y = df['Close'].loc[X.index]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=24)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure(figsize=(10, 8))
plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual Data')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], linestyle='--', color='red', label='Perfect fit')
plt.xlabel('Actual close prices')
plt.ylabel('Predicted close prices')
plt.title('Linear Regression: Actual vs Predicted close prices')
plt.legend()
plt.show()

