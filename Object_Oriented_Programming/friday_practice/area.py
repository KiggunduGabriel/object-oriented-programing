class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c1 = Circle(7)
c2 = Circle(6.9)

print(c1.area())
print("The area of circle 2 is:", c2.area())