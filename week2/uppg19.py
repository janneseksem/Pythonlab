'''I denna uppgift kan ni använda CSV-filen sales_data.csv som finns här i repot. Skapa ett program som använder Pandas för att analysera en CSV-fil med försäljningsdata:

    Läs in en CSV-fil med kolumner för datum, produkt och försäljningsbelopp.
    Visa de första 5 raderna.
    Beräkna total försäljning per produkt.
    Beräkna genomsnittlig försäljning per månad.
    Hitta den dag med högst total försäljning.
    Hitta produkten med högst total försäljning.
    Skapa ett enkelt linjediagram över försäljningen över tid med matplotlib.

Om du vill: 8. Programmet sparar diagrammet som en PNG-fil 5. Programmet skriver en sammanfattning av analysen till en ny textfil (du får bestämma vad analysen ska inkludera)

Använd klasser för att strukturera koden och inkludera felhantering för filoperationer.'''


import pandas as pd
import matplotlib.pyplot as plt

# Försök läsa in CSV-filen (kontrollera att den är i samma katalog)
df = pd.read_csv('sales_data.csv')

# Visa de första 5 raderna av data
print(df.head())
print("----------")

# Visa total försäljning per produkt
print(df['SalesAmount'])
print("----------")
#Beräkning genomsnittlig försäljning per månad
df['Date'] = pd.to_datetime(df['Date'])
df['YearMonth'] = df['Date'].dt.to_period('M')

median = df.groupby('YearMonth')['SalesAmount'].median()
print(median)
print("----------")

#Hitta den dag med mest försäljning
total_sales_per_day = df.groupby('Date')['SalesAmount'].sum()
highest_sales_day = total_sales_per_day.idxmax()
highest_sales_amount = total_sales_per_day.max()

print(f"Dagen med högst försäljning är {highest_sales_day.date()} med {highest_sales_amount} sålda units")
print("----------")

#Hitta produkten med högst total försäljning.
total_product = df.groupby('Product')['SalesAmount'].sum()
highest_product = total_product.idxmax()
highest_product_sales = total_product.max()

print(f"The product: {highest_product}, has the highest sales of: {highest_product_sales} sold units")

#Skapa ett enkelt linjediagram över försäljningen över tid med matplotlib.
plt.figure(figsize=(10, 6))
plt.plot(total_sales_per_day.index, total_sales_per_day.values, marker='o', linestyle='-', color='b')

plt.xlabel('Datum')
plt.ylabel('Försäljning')
plt.title("Försäljning över tid")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



