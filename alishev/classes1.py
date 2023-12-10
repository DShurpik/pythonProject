# Methods, self - parameter
class Human:
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

h2.name = 'Mick'
h2.surname = 'Hox'
h2.age = 76
h2.print_info()
