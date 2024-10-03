'''Importera och använd functools.reduce() för att:

    Beräkna produkten av alla tal i en lista.
    Hitta det största talet i en lista.
'''

import functools

numbers = [2, 3, 4]
product = functools.reduce (lambda x, y: x * y, [x for x in numbers])
print(product)

biggest = functools.reduce(lambda x, y : x if x > y else y, numbers)

print(biggest)

