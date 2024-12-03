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

Dataanalys och förbearbetning

Datauppsättningen från filen spain-la-liga-matches-2023-to-2024-stats.csv som finns i footystats kan laddas ned .csv fil och la_liga_results_2324.csv' från Kaggle användare som jag mejlade om nyare data matcher från 2023 till 2024. Detta kommer att genomgå utforskande dataanalys för att identifiera nyckelfaktorer som påverkar skottförsök. För Bearbetningsfasen kommer att innefatta data cleaning, handling missing values, och normalisering av variabler för att förbättra modellens träningseffektivitet. Relevanta funktioner som lagstatistik kommer att identifieras för modellinmatning.

Att bygga den prediktiva modell

Modellen kommer att konstrueras för att förutsäga antalet skott som varje lag försöker göra genom att kolla hur många skott Hemma och borta laget skjuts, men samt använda motståndarens antal skott som har skjutit mot laget. Andra mindre viktiga features används för se lagets prestanda vid offensivt eller defensivt spelande.  Modellen för Neural network kommer att tränas med hjälp av en backpropagation-algoritm, med loss function och en adaptive optimizer som testar fram exempelvis Adam. Data Uppsättningen kommer att delas upp i training- och test sets. Random Forest modellen kommer även tränas i en seperat class för att jämföra två modellerna hur de kan hantera projektets insamlingsdata.

Sammanfattningsvis

Detta projekt använder sig av ett neural network och Random forest för att förutsäga skottförsök i fotbollsmatcher och härleda modellbaserad sannolikhet. De prediktiva insikterna som genereras kommer att bidra till bättre strategiskt beslutsfattande för team och mer informerade risk utvärderingar. Flera olika metoder kommer testas tills man får en relevant accuracy för sin modell.
