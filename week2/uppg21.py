'''Implementera en klass FibonacciIterator som genererar Fibonacci-sekvensen:

    Använd __iter__() och __next__() metoder.
    Låt iteratorn generera sekvensen upp till ett specificerat maxvärde.
    Hantera StopIteration när sekvensen är klar.

Detta introducerar konceptet med iteratorer och generatorer på ett praktiskt sätt.
'''
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ....
class FibonacciIterator:
    def __init__(self, max_value=None):
        self.a = 0
        self.b = 1
        self.max_value = max_value


    def __iter__(self):

        return self
    
    def __next__(self):
        if self.max_value is not None and self.a > self.max_value:
            raise StopIteration
        else:
            fib_number = self.a
            next_value = self.a + self.b
            self.a = self.b
            self.b = next_value
            return fib_number
            
    
    
fibonacciIterator1 = FibonacciIterator(max_value=150)
myiter = iter(fibonacciIterator1)

for i in myiter:
    print(i)


