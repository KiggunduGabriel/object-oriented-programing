# Define the parent class
class Shape:
    def area(self):
        print("This is the area of a generic shape.")

# Define the child class that overrides the area method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Override the area method
    def area(self):
        area_value = self.width * self.height
        print(f"The area of the rectangle is: {area_value}")

# Create an object of Rectangle
rect = Rectangle(5, 10)

# Call the overridden method
rect.area()
