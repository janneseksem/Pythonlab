def generator(num):

        a = 0
        b = 1
        count = 0
        while count < num:
            yield a
            next_number = a + b
            a = b
            b = next_number
            count += 1

#0 1 1 2 3 5 8 13 21 34                                          
for i in generator(10):
      print(i, end=' ')

