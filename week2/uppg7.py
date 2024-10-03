'''Skapa en klass Stack som implementerar en stack (sista in, första ut) datastruktur med metoderna:

    push(item): Lägger till ett element överst i stacken.
    pop(): Tar bort och returnerar det översta elementet i stacken.
    peek(): Returnerar det översta elementet utan att ta bort det.
    is_empty(): Returnerar True om stacken är tom, annars False.
'''

class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        stack = self.list
        return stack.append(item)
    
    def pop(self):
        stack = self.list
        if not self.is_empty():
            return stack.pop()
        else:
            return None    
    def peek(self):
        stack = self.list
        length = len(stack)
        if not self.is_empty():
            return stack[length - 1]
        else:
            return None 
        
    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
        
    
        
stack1 = Stack()

stack1.push(1)
stack1.push(2)
stack1.push(3)
print(f"Stack: {stack1.list}")

stack1.pop()
print(f"Stack: {stack1.list}")

print(stack1.pop())

print(stack1.is_empty())

stack1.pop()

print(stack1.is_empty())
print(f"Stack: {stack1.list}")



