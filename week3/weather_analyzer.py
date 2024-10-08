from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Load weather data from CSV file Handle any missing values 
# ​Calculate average temperature per dag

df = pd.read_csv('Extended_Weather_Data.csv')

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna()

#Create a line chart showing temperature trend over time 
# Make a bar chart for monthly precipitation 
# Show a scatter chart for temperature vs humidity 
# Create a heat map for correlation between different weather 
# parameters

plt.figure(figsize=(10,8))
plt.plot(df['Date'], df['Temperature'], marker='o')
plt.title('Temperature trend over time in 2023')
plt.xlabel('Date of the temperature')
plt.ylabel('Temperature in Celcius')
plt.xticks(rotation=45)

month_avg_temp = df.groupby(df['Date'].dt.to_period('M'))['Temperature'].mean()
#convert the periodindex to timestamp
month_avg_temp.index = month_avg_temp.index.to_timestamp()

plt.figure(figsize=(10,8))
plt.bar(month_avg_temp.index, month_avg_temp, color='red', width=0.8)
plt.title('Montly Average Temperature bar chart')
plt.xlabel('Montly date')
plt.ylabel('Temperature celcius °C')

#Scatterplot for temperature cs humidity
plt.figure(figsize=(10,8))
#using temperature as color mapping
scatter = plt.scatter(df['Humidity'], df['Temperature'], c=df['Temperature'], cmap='coolwarm')
plt.colorbar(scatter, label='Temperature °C')
plt.title('Temperature vs Humidity scatter chart (Colored by Temperature)')
plt.xlabel('Humidity %')
plt.ylabel('Temperature °C')

#Heatmap for correlation between different weather parameters
plt.figure(figsize=(10,8))

#Calculate the correlation matrix for weather parameters
corr_matrix = df[['Temperature', 'Humidity', 'Pressure', 'WindSpeed', 'Precipitation']].corr()
heatmap = sns.heatmap(corr_matrix, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.5)
heatmap.set_title('Correlation in Temperature')

#Use a simple method (e.g. moving average 5) to predict tomorrow's 
# temperature Show the forecast compared to actual temperatures
df['MA_5'] = df['Temperature'].rolling(window=5).mean()
#Shows the plot between actual vs predicted forecasting
plt.figure(figsize=(10,8))
plt.plot(df['Date'], df['Temperature'], label='Actual')
plt.plot(df['Date'], df['MA_5'], label='Moving Average 5 Days')
plt.legend()
plt.title('Actual vs Moving average Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature')
#Generate TLDR on the whole report including Moving average 5
print(df)

#Outdata, Four visualizations in PNG format 
# (trend, Humidity,Pressure,WindSpeed,Precipitation) 
# A text file with summary statistics and forecast performance

fig, axes = plt.subplots(2,2, figsize=(10,8))
#Trend line
sns.lineplot(x='Date', y='Precipitation', data=df, ax=axes[0,0])
axes[0,0].set_title('Trend over time in Precipitation')
axes[0,0].set_xlabel('Date')
axes[0,0].set_ylabel('Precipitation')
axes[0,0].tick_params(axis='x', rotation=45)
#Barplot
sns.barplot(x='Date', y='Precipitation', data=df, ax=axes[0,1])
axes[0,1].set_title('The amount of Precipitation')
axes[0,1].set_xlabel('Date')
axes[0,1].set_ylabel('Precipitation')
#Histogram
sns.histplot(df['WindSpeed'], ax=axes[1,0]) #Histogram for windspeed
axes[1,0].set_title('Histogram for Windspeed')
#Scatter 
sns.scatterplot(x='WindSpeed', y='Pressure', data=df, ax=axes[1,1])
axes[1,1].set_title('Correlation between relation in Windspeed and pressure')
axes[1,1].set_xlabel('Windspeed')
axes[1,1].set_ylabel('Pressure')

#Saves outdata in PNG
plt.tight_layout()
plt.savefig('weather_analysis_plots.png', bbox_inches='tight')

#Saves dataframe to a .txt file
df.to_csv('weather_data.txt', sep='\t', index=False)

plt.show()
plt.close()#Avoid memory leak