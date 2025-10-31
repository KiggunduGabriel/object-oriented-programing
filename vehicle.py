# Define the parent class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Define the child class
class Car(Vehicle):
    def honk(self):
        print("The car is honking! Beep beep!")

# Create an object of Car
my_car = Car()

# Call methods
my_car.move()   # Inherited from Vehicle
my_car.honk()   # Defined in Car