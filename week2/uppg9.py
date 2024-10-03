'''Skapa en hierarki av djurklasser:

    Börja med en basklass Animal med attributen name och sound.
    Skapa subklasser Dog, Cat, och Cow som ärver från Animal.
    Överskugga make_sound() metoden i varje subklass för att returnera djurets specifika ljud.
    Skapa en funktion animal_chorus(animals) som tar en lista av djur och låter alla göra sitt ljud.
'''

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        print(f"{self.name} says {self.sound}")


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name, "Woof")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

class Cow(Animal):

    def __init__(self, name):
        super().__init__(name, "Moo")


dog1 = Dog("Daniel")
cat1 = Cat("Davis")
cow1 = Cow("Bui")

dog1.make_sound()
cat1.make_sound()
cow1.make_sound()



