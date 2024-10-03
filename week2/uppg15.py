'''Vi introducerar lambda-funktioner, så kallade "anonyma funktioner" med några enkla exempel:

    Skriv en lambda-funktion som returnerar kvadraten av ett tal.
    Använd sorted() med en lambda-funktion för att sortera en lista av tupler baserat på det andra elementet.
    Använd filter() med en lambda-funktion för att filtrera ut negativa tal från en lista.

Ta reda på och förklara hur lambda-funktioner skiljer sig från vanliga funktioner och när de är användbara.'''

def square(x):
    sq = lambda x : x**2
    return sq(x)

print(square(4))


#sort by tupels second element
data = [(1, 3), (2, 1), (3, 2)]

tupels = sorted(data, key=lambda x: x[1], reverse=False)
print(tupels)

#filter by taking out negative numbers from the list
numbers = [-1, 2, -3, 5]

non_neg = list(filter(lambda x : x > 0, numbers))

print(non_neg)