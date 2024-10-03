'''Uppgift 10: Arvs och polyformism: 
Klass och subklasser för geometriska former 
(med kod-skelett/scaffolding)
Här är en början på en klass för geometriska former. 
Komplettera klassen med metoder och funktionalitet 
enligt kommentarerna:'''

class GeometricShape:
    def __init__(self, name):
        self.name = name

    def area(self):
        # Implementera en metod som returnerar formens area
        pass

    def perimeter(self):
        pass
        

    def __str__(self):
        # Returnera en sträng som beskriver formen
        return f"Formel: {self.name}"
        

class Rectangle(GeometricShape):
    def __init__(self, width, height):
        # Implementera konstruktorn
        super().__init__("Rectangle")        
        self.width = width
        self.height = height
        
        #lambda for area och parametrar
        self.area_func = lambda : self.width * self.height
        self.para_func = lambda : 2 * self.width + 2 * self.height
    

    # Implementera area() och perimeter() för Rectangle
    def area(self):
        return self.area_func()

    def perimeter(self):
        return self.para_func()
    
class Circle(GeometricShape):
    def __init__(self, radius):

        super().__init__("Circle")
        self.radius = radius
        
        self.area_func = lambda : self.radius * self.radius * 3.14
        self.para_func = lambda : 2 * self.radius * 3.14

    # Implementera area() och perimeter() för Circle
    def area(self):
        return self.area_func()
    
    def perimeter(self):
        return self.para_func()

    

# Skapa några instanser av Rectangle och Circle och testa dina metoder

# geometricshape1 = GeometricShape()
circle1 = Circle(3)
rectangle1 = Rectangle(4,2)

print(f"Area: {rectangle1.area()}")
print(f"Parameter: {rectangle1.perimeter()}")

print(f"Area: {circle1.area()}")
print(f"Parameter: {circle1.perimeter()}")

