class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"


# Demonstrating polymorphism
def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        print(vehicle.move())


# Create instances of each vehicle
car = Car()
plane = Plane()
boat = Boat()

# List of vehicles
vehicles = [car, plane, boat]

# Demonstrate movement
demonstrate_movement(vehicles)