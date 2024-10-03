'''Skriv en klass FileManager med följande metoder:

    read_file(filename): Läser innehållet i en fil och returnerar det som en sträng.
    write_file(filename, content): Skriver innehållet till en fil.
    append_file(filename, content): Lägger till innehåll i slutet av en befintlig fil.
    delete_file(filename): Raderar en fil.
'''
import os

# with open('example.txt', 'w') as file:
#     file.write("This is a test \n")
#     file.write("Hello world \n")
#     file.write("This is another test \n")

class FileManager:
    
    def read_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"File {filename} is not found")

        except Exception as e:
            print(f"An error was found while reading the user")

    def write_file(self, filename, content):
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

        print(f"The string has been written in {filename}.")
    
    def append_file(self, filename, content):
         
        with open(filename, 'a', encoding='utf-8') as file:
              file.write(content)

        print(f"file has been appended at {filename}.")

    def delete_file(self, filename):

            if os.path.exists(filename):
                os.remove(filename)
                print(f"File named {filename} has been removed")
            else:
                print(f"file name {filename} is not found")
                   
    

filemanager1 = FileManager()

#print(filemanager1.read_file('example.txt'))

filemanager1.write_file('example.txt', 'This is a test \n')
print(filemanager1.read_file('example.txt'))

filemanager1.append_file('example.txt', 'This is another test \n')
print(filemanager1.read_file('example.txt'))

# filemanager1.delete_file('example.txt')
# print(filemanager1.read_file('example.txt')) 





