'''Skapa en DataFrame från en dictionary av listor som innehåller information om 5 olika länder (namn, befolkning, yta, kontinent).

Ladda filen 'sample_data0.csv' och visa de sista 10 raderna.

Beräkna och visa medianlönen för varje avdelning.

Hitta den anställda med högst prestationspoäng i varje stad.

Skapa en ny kolumn 'Lön_per_År_Erfarenhet' genom att dividera 'Salary' med 'Years_Experience'. Hantera eventuella division-med-noll-fel.

Använd funktionen pd.melt() för att omforma DataFrame:n, och gör 'Salary' och 'Performance_Score' kolumnerna till variabler.

Pivota DataFrame:n för att visa genomsnittlig lön för varje kombination av Stad och Avdelning.
'''

import pandas as pd

country = {
    "namn" : ["Sverige", "Danmark", "Norge", "Findland", "Spanien"],
    "befolkning" : [10607000, 5960000, 5530000, 5580000, 48790000],
    "yta" : [450295, 42933, 323802, 338455, 505992],
    "kontinent" : ["Europa", "Europa", "Europa", "Europa", "Europa"]
}

df = pd.DataFrame(country)

print(df)