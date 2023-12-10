# Create class and describe it
class Cat:

    # Function, for creating a class constructor
    def __init__(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    # Default constructor
    #def __init__(self):
    #    pass
    # Для переопределения методов, к полю добавлять просто = None
    def say_meow(self, name):
        print(name, 'meow')
# Create the instances class Cat

cat1 = Cat('Barsik', 10, True)
#name = cat1.name = 'Barsik'
#age = cat1.age = 10
#isHappy = cat1.isHappy = True
cat1.say_meow(cat1.name)

cat2 = Cat('Marsik', 5, True)
#cat2.name = "Marsik"
#cat2.age = 5
#cat2.isHappy = True
cat2.say_meow(cat2.name)
print(cat1.name, cat1.age, cat1.isHappy, '\n', cat2.name, cat2.age, cat2.isHappy)
