import math

class Matte:
    
    def add(self, a, b):
        x = lambda a, b : a + b
        return x(a,b)
    
    def substract(self, a, b):
        x = lambda a, b : a - b
        return x(a,b)
    
    def divide(self, a, b):
        x = lambda a, b : a / b
        return x(a,b)
    
    def multiply(self, a, b):
        x = lambda a, b : a * b
        return x(a,b)
    
    def gcd(self, a, b):
        x = lambda a, b: a if b == 0 else x(b, a % b)
        return x(a,b)
    
    def area_circle(self, r):
        pi = math.pi
        x = lambda r: pi * r**2
        return x(r)
    
    def circumference(self, d): 
        pi = math.pi
        x = lambda d: pi * d
        return x(d)

matte1 = Matte()

print(matte1.add(5,2))
print(matte1.substract(5,2))
print(matte1.divide(5,2))
print(matte1.multiply(5,2))
print(matte1.gcd(38,24))
print(matte1.area_circle(5))
print(matte1.circumference(5))