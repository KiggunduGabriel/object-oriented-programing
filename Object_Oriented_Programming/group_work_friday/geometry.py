import math

# Class for a Point in 2D space
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Calculate distance between this point and another
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    # Find the midpoint between this point and another
    def midpoint(self, other):
        mid_x = (self.x + other.x) / 2
        mid_y = (self.y + other.y) / 2
        return Point(mid_x, mid_y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


# Class for a Circle
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    # Calculate area of the circle
    def area(self):
        return math.pi * (self.radius ** 2)

    # Check if a point lies inside the circle
    def contains(self, point):
        return self.center.distance_to(point) <= self.radius

    # (Stretch) Check if two circles intersect / overlap
    def intersects(self, other_circle):
        distance_between_centers = self.center.distance_to(other_circle.center)
        return distance_between_centers <= (self.radius + other_circle.radius)

    def __str__(self):
        return f"Circle(center={self.center}, radius={self.radius})"


#  TESTING THE CLASSES  

# Step 1: Create a circle and some points
circle = Circle(Point(0, 0), 5)   # Circle centered at (0,0) with radius 5
points = [
    Point(1, 2),
    Point(5, 0),
    Point(6, 1),
    Point(-3, -4)
]

# Step 2: Check which points lie inside the circle
for p in points:
    print(f"{p} is inside circle: {circle.contains(p)}")

# Midpoint and distance example
p1 = Point(0, 0)
p2 = Point(4, 4)
print(f"Distance between {p1} and {p2}: {p1.distance_to(p2)}")
print(f"Midpoint: {p1.midpoint(p2)}")

# Stretch: Check if two circles intersect
circle2 = Circle(Point(8, 0), 4)
print(f"Do circles intersect? {circle.intersects(circle2)}")
