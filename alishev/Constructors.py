# __init__ method is a class constructor
class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_info(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}")

h1 = Human('John', 'Doe', 25)
h1.print_info()

h2 = Human("Max", 'Katc', 33)
h2.print_info()