# Base class for all moving entities
class MovingEntity:
    def move(self):
        pass  # This is a placeholder to be overridden by subclasses


# Class representing a Car
class Car(MovingEntity):
    def move(self):
        print("Driving 🚗")

        
# Class representing a Plane
class Plane(MovingEntity):
    def move(self):
        print("Flying ✈️")


# Class representing a Bird
class Bird(MovingEntity):
    def move(self):
        print("Flying like a bird 🐦")


# Class representing a Fish (with swimming)
class Fish(MovingEntity):
    def move(self):
        print("Swimming 🐟")


# Example usage:
def demonstrate_movement(entities):
    for entity in entities:
        entity.move()  # Call the move method of each entity


# Create objects of each class
car = Car()
plane = Plane()
bird = Bird()
fish = Fish()

# Put all objects in a list
entities = [car, plane, bird, fish]

# Demonstrate their movement actions
demonstrate_movement(entities)
