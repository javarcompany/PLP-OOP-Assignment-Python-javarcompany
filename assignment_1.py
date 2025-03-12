class Superhero:
    def __init__(self, name, powers, health):
        self.name = name
        self.powers = powers
        self.health = health

    # Method to display superhero information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Powers: {', '.join(self.powers)}")
        print(f"Health: {self.health}")
    
    # Method to take damage (reduce health)
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Health is now {self.health}.")
    
    # Method to heal the superhero
    def heal(self, healing_points):
        self.health += healing_points
        print(f"{self.name} healed {healing_points} points. Health is now {self.health}.")
    
    # Polymorphism: A method that can be overridden by subclasses
    def special_ability(self):
        return f"{self.name} uses their powers!"  # Base superhero power

class FlyingSuperhero(Superhero):
    def __init__(self, name, powers, health, flight_speed):
        # Calling the constructor of the base class
        super().__init__(name, powers, health)
        self.flight_speed = flight_speed  # New attribute for flight speed

    # Override the special_ability method to add a flying-related ability
    def special_ability(self):
        return f"{self.name} flies at {self.flight_speed} mph!"
    
    # New method to perform a flying action
    def fly(self):
        print(f"{self.name} is soaring through the skies at {self.flight_speed} mph!")

# Create a basic superhero object
hero1 = Superhero(name="Captain Python", powers=["Super Strength", "Invisibility"], health=100)
hero1.display_info()
hero1.take_damage(20)
hero1.heal(10)
print(hero1.special_ability())  # Polymorphism in action

print("\n----------------------------\n")

# Create a flying superhero object
hero2 = FlyingSuperhero(name="SkySurfer", powers=["Super Speed", "Flight"], health=120, flight_speed=300)
hero2.display_info()
hero2.take_damage(30)
hero2.heal(20)
print(hero2.special_ability())  # Polymorphism: Overridden method
hero2.fly()  # Flying action
