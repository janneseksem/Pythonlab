'''Läs på lite om map() och filter(), gör sedan följande uppgifter:

    Skriv en funktion double(x) som returnerar det dubbla värdet av x.
    Använd map() för att applicera double på en lista av tal, d.v.s. varje tal i listan ska dubblas.
    Skriv en funktion is_even(x) som returnerar True om x är jämnt, annars False.
    Använd filter() för att filtrera ut jämna tal från en lista.
'''

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled = list(map(double, numbers))
print(doubled)

def is_even(x):
    return x % 2 == 0

even = list(filter(is_even, numbers))
print(even)