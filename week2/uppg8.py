'''Implementera en klass TodoList med metoder för att:

    Lägga till uppgifter
    Markera uppgifter som slutförda
    Visa alla uppgifter
    Visa endast oavslutade uppgifter

'''

class TodoList:
    def __init__(self):
        self.list = []

    def add(self, item):
        self.list.append({"Task": item, "Completed": False})
        print(f"Task {item} has been added")

    def mark(self, task):
        for i in self.list:
            if i['Task'] == task:
                i['Completed'] = True
                print(f"Task {task} has been marked")
                return
        print(f"{task} has not been found")

    def showAll(self):
        if not self.list:
            print("No tasks has been found")

        else:
            for i in self.list:
                print(f"Task {i['Task']}, Status: {i['Completed']}")

    def showCompleted(self):
        for i in self.list:
            if i['Completed'] == True:
                print(f"Task {i['Task']}, Status: {i['Completed']}")


todolist1 = TodoList()

todolist1.add("Handla mat")
todolist1.add("Städa huset")
todolist1.add("Gå till möte")

todolist1.showAll()

todolist1.mark("Handla mat")
todolist1.showAll()

print("\n visas klara uppgifter")
todolist1.showCompleted()