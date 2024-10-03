'''Skriv list comprehensions för att:

    Skapa och skriv ut en lista med alla tal mellan 1 och 100 som är delbara med 3 eller 5.
    Generera och skriv ut en lista med tupler (x, y) för alla x och y där 0 <= x < 5 och 0 <= y < 5.
'''

data1 = [x for x in range(1,101) if x % 3 == 0 and x % 5 == 0]
print(data1)

data2 = [(x, y) for x in range(1,5) for y in range(1,5)]
print(data2)

data3 = []
for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        data3.append(x)

print(data3)

data4 = []
for x in range(1,5):
    for y in range(1,5):
        data4.append((x,y))

print(data4)