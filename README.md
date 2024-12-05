# Pythonlab
Pythonprogrammering-for-AI-utveckling-HT24 

Project-1: Console-Based Blackjack Game
Overview

This project is a simple console-based implementation of the popular card game Blackjack.
How to Play

    The rules are implemented within the code.
    The game starts immediately: the player is dealt the first and third card, while the dealer receives the second card.
    Use the command hit to draw another card or stand to keep your current hand.
    The game ends when either the player or the dealer wins.
    After the game ends, the player can choose to play again by entering y, or exit the game with n.

Getting Started

To run the game, simply execute the Python script in a console. Make sure you have Python 3.x installed.

Project-2: Modeling for Home/Away team shots

Introduktion och översikt över projektidén

Projektet syftar till att utveckla modell för att förutsäga antalet skott ett lag kommer att försöka under en match och de tillhörande sannolikhet för att uppnå specifika skottresultat. Genom att utnyttja historiska data från den tillhandahållna CSV-filen försöker modellen identifiera betydande mönster och trender som påverkar en av teamets prestationer.

Starta och testa programmet:
Alternativ 1 - 
1. Ladda ner 'fixed_merged_la_liga_results.csv'
2. Köra 'team_model_home.py'

Alternativ 2 -
1. Ladda ner 'la_liga_results_2324.csv' och 'spain-la-liga-matches-2023-to-2024-stats.csv'
2. Köra 'csv_merge.py', då sparas en ny fil kallas 'fixed_merged_la_liga_results.csv'
3. Köra 'team_model_home.py'

Dataanalys och förbearbetning

Datauppsättningen från filen spain-la-liga-matches-2023-to-2024-stats.csv som finns i footystats kan laddas ned .csv fil och la_liga_results_2324.csv' från Kaggle användare som jag mejlade om nyare data matcher från 2023 till 2024. Detta kommer att genomgå utforskande dataanalys för att identifiera nyckelfaktorer som påverkar skottförsök. För Bearbetningsfasen kommer att innefatta data cleaning, handling missing values, och normalisering av variabler för att förbättra modellens träningseffektivitet. Relevanta funktioner som lagstatistik kommer att identifieras för modellinmatning.

Att bygga den prediktiva modell

Modellen kommer att konstrueras för att förutsäga antalet skott som varje lag försöker göra genom att kolla hur många skott Hemma och borta laget skjuts, men samt använda motståndarens antal skott som har skjutit mot laget. Andra mindre viktiga features används för se lagets prestanda vid offensivt eller defensivt spelande.  Modellen för Neural network kommer att tränas med hjälp av en backpropagation-algoritm, med loss function och en adaptive optimizer som testar fram exempelvis Adam. Data Uppsättningen kommer att delas upp i training- och test sets. Random Forest modellen kommer även tränas i en seperat class för att jämföra två modellerna hur de kan hantera projektets insamlingsdata.

Sammanfattningsvis

Detta projekt använder sig av ett neural network och Random forest för att förutsäga skottförsök i fotbollsmatcher och härleda modellbaserad sannolikhet. De prediktiva insikterna som genereras kommer att bidra till bättre strategiskt beslutsfattande för team och mer informerade risk utvärderingar. Flera olika metoder kommer testas tills man får en relevant accuracy för sin modell. Rapporten är dokumenterat för djupare analys inom denna projektet.

Resultat
Neural network: Neural Network- Loss: 17.663623809814453, MAE: 3.2723398208618164, r2: 0.4454943537712097

Predicted and Actual values (first 10 ex):
Predicted:
 [15.633022 16.91614  12.180565 14.209396 16.072697 16.500029 13.074678
 13.025862 12.287777 14.876021]
Actual:
 [14 21  9 10 20 20 12  5 10 15]

Random Forest- MSE: 15.416986047642112
Bästa parametrar: {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 200}
Bästa cross-validation score: 0.4980888886682703
Train Accuracy: 0.912
Test Accuracy (r2): 0.516
Predicted and actual values (first 10 example):
Predicted: 
 [14.73426587 17.83588294 11.28047421 12.99286977 13.59784037 18.55863131
 12.41344282 12.53622421 11.98390079 13.57627381]
Actual: 
 [14 21  9 10 20 20 12  5 10 15]

 Förbättringar
 - Sätter in värden när NaN värden finns med. fillna i median används
 - Försäktra shape är korrekt
 - Transform istället för fit_transform för unvdika data leakage
 - Noder sänkts eftersom data samling är lägre än förväntat
 - Dropout och Batchnormalization och Early stopping används för förbättra accuracy
 - Parameter grid används för hitta bästa parametrar och få bättre accuracy
 - one hot är viktig för features och labels