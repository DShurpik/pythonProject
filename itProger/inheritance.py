class Building:
    age = None
    city = None

    def __init__(self, city, age):
        self.age = age
        self.city = city

    def get_info(self):
        print('City is: ', self.city, 'Age: ', self.age)

class School(Building):
    children = None

# Конструктор, через супер пронаследованный от супер класса с его конструктором
    def __init__(self, children, city, age):
        super(School, self).__init__(city, age)
        self.children = children

# Пример полиморфизма, берем через супер метод родителя, и добавляем необходимую для класса реализацию
    def get_info(self):
        super().get_info()
        print('Children = ', self.children)



school = School(500, 'Minsk', 15)
school.get_info()

house = Building('Gomel', 20)
house.get_info()

shop = Building('Brest', 35)
shop.get_info()