'''Vi villa bygga våra program så att kan hantera olika situationer, till exempel när vi får fel typ av input från användaren. Låt säga att du har ett program som tar in två heltal från användaren och utför en division på dessa två tal, då måste du se till att ditt program kan hantera när täljaren är 0. Vi vill aldrig ha division med 0. Vi hanterar dessa undantagsfall, Exceptions med try- och except-satser i vår kod. I andra programmeringsspråk ser man catch istället för try. Det finns olika typer av Exceptions, så som TypeError, ValueError, IndexError, KeyError. Ibland använder vi alla typer av errors som en generell Exception istället för specifik typ av Error. Detta ger oss dock eventuellt mindre detaljerad information om vad som gått fel.

Skriv ett program som demonstrerar grundläggande undantagshantering:

    Be användaren mata in två tal.
    Försök (try) att dividera det första talet med det andra.
    Hantera ZeroDivisionError om användaren försöker dividera med noll. (except)
    Hantera ValueError om användaren matar in något som inte är ett tal. (except)
'''



try:
    data1 = int(input("Mata in första talet: "))
    data2 = int(input("Mata in andra talet: "))
    print(data1 / data2)
    
except ZeroDivisionError:
    print("Error: cant be divided by zero")

try:
    data3 = int(input("Mata in något som är inte ett tal: "))
    print(data3)

except ValueError:
    print("Error non value")