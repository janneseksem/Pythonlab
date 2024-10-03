'''Skriv ett program som gör följande:

    Skapar en textfil och skriver några rader till den.
    Läser innehållet i filen och skriver ut det.
    Lägger till mer text i slutet av filen.
    Läser filen igen och visar det uppdaterade innehållet.

Använd with-satser för att säkerställa att filen stängs korrekt.
'''

#1. Skapar en textfil och skriver några rader till den.
with open("example.txt", "w") as file:
    file.write("Hej, världen!\n")
    file.write("Detta är en exempelfil.\n")

#2. Läser innehållet i filen och skriver ut det.
with open("example.txt", "r") as file:
    print(file.read())

#3. Lägger till mer text i slutet av filen
with open("example.txt", "a") as file:
    file.write("Detta är ytterligare en rad.\n")

#4. Läser filen igen och visar det uppdaterade innehållet.
with open("example.txt", "r") as file:
    print(file.read())
    