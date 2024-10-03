squares = [x**2 for x in range(1,11)]
print(squares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

length = "Hello world is a simple code"
list_length = [len(word) for word in length.split()]
print(list_length)