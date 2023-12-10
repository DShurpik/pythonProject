class Circle:

    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius * 2 * Circle.PI

    def get_perimetr(self):
        return self.radius ** 2 * Circle.PI

c1 = Circle(3)
print(c1.get_area())
print(c1.get_perimetr())