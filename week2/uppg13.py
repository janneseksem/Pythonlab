'''Använd map() och filter() för att:

    Skapa en lista med kvadrater av alla jämna tal i en given lista.
    Filtrera ut alla primtal från en lista med tal.
'''

def is_even(x):
    even = x**2
    if even % 2 == 0:
        return even
    

squares = [x for x in range(1, 11)]
squares_even = list(filter(lambda x: x is not None, map(is_even, squares)))
print(squares_even)

def is_prime(x):

    # for i in range(2, x):
    #     if x % i == 0:
    #         return False
    #     else:
    #         return True
    return not any(x % i == 0 for i in range(2,x))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime = list(filter(is_prime, numbers))
print(prime)