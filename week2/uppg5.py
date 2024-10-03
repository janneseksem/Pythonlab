'''Implementera en klass ContactBook som använder ett 
dictionary för att lagra kontakter. 
Inkludera metoder för att lägga till, ta bort, 
uppdatera och visa kontakter.'''

class ContactBook:
    def __init__(self):
        
        self.data = {}
    
    def add(self, name, phone):
        if name in self.data:
            print(f"Contact {name} already exists in the book")
        else:
            self.data[name] = {'phone': phone}
            print(f"Contact {name} has been added")
    
    def remove(self, name):
        if name in self.data:
            del self.data[name]
            print(f"The name {name} as been deleted in the book")
        else:
            print(f"The name {name} doesn't exists in the book")
        
    def update(self, name, phone):
        if name in self.data:
            if phone:
                self.data[name]['phone'] = phone
            else:
                print("Invalid update")

    def display(self):
        if not self.data:
            print("No contacts")
        else:
            for name, info in self.data.items():
                print(f"Name: {name}, Phone number: {info['phone']}")

contactbook1 = ContactBook()

print(contactbook1.add("Daniel", "0708981883"))
print(contactbook1.display())

print(contactbook1.add("David", "0733145909"))
print(contactbook1.display())

print(contactbook1.remove("David"))
print(contactbook1.display())

print(contactbook1.update("Daniel", "07355593"))
print(contactbook1.display())