class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"{self.name} says Hello!")

h1 = Person('John', 33)
h1.say_hello()

class Student(Person):
    # ПЕРЕОПРЕДЕЛЕНИЕ МЕТОДОВ
    def __init__(self, name, age, grade):
        # Через супер наследуем конструктор из родителя, с полями родителя и добавляем свои поля для реализации

        # Либо вызвать конструктор через имя класса
        #  Person.__init__(name, age)

        super().__init__(name, age)
        self.grade = grade

    def say_hello(self):
        print(f"{self.name} is a student and says Hello!")

class Teacher(Person):
    pass

s1 = Student('John', 22, 100)
s1.say_hello()

t1 = Teacher('Bob', 56)
t1.say_hello()