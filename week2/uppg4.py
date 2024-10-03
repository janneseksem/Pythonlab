'''Skapa en textfil (i samma mapp som ditt program). 
Skriv in eller kopiera in en text av valfri längd. 
Läs in textfilen och använd ett dictionary för att räkna 
'förekomsten av varje ord. Ignorera skiljetecken och
 konvertera alla ord till lowercase.
'''
import string

with open("example4.txt", "w") as file:
    file.write("Hej världen! Detta är en enkel testtext. Hej, hej igen.")

with open("example4.txt", "r") as file:
    low_letter = file.read().lower()
    #print(low_letter)

    ord_lista = low_letter.translate(str.maketrans('', '', string.punctuation))
    ord_lista = ord_lista.split()
    ord_frekvens = {}

    for i in ord_lista:
        if i in ord_frekvens:
            ord_frekvens[i] +=1
        else:
            ord_frekvens[i] = 1

#expected output: {'hej': 2, 'världen': 1}
print(ord_frekvens)