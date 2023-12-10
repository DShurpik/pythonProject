class Human:
    greeting = 'Hello'

    def print_info(self):
        print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}")


# Creating a new object by Human class
h1 = Human()
h2 = Human()

# Creating attributes
h1.name = 'John'
h1.surname = 'Doe'
h1.age = 25
h1.print_info()

# Print static attribute through an object
print(h1.greeting)

h2.name = 'Mick'
h2.surname = 'Hox'
h2.age = 76
h2.print_info()
# Print static attribute through an object
print(h2.greeting)

# Print static attribute through Class
print(Human.greeting)