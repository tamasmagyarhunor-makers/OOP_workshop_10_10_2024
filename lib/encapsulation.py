class Pokemon:
    def __init__(self, name, level):
        self.name = name        # public attribute
        self.level = level      # public attribute
        self.__hp = 100         # private attribute (encapsulated)

    def get_hp(self):           # method to access HP
        return self.__hp

    def set_hp(self, new_hp):   # method to modify HP safely
        if type(new_hp) != int:
            raise Exception('Only integers can be set for the pokemons hp')
        if new_hp >= 0:
            self.__hp = new_hp
        else:
            print(f"{self.name}'s HP cannot be negative!")

    def attack(self):
        print(f"{self.name} uses a powerful attack!")

# Example of using the encapsulated class
pikachu = Pokemon("Pikachu", 5)
pikachu.attack()              # Can use public methods
print(pikachu.get_hp())       # Access HP through a method, not directly
pikachu.set_hp(80)            # Modify HP through the setter method















# Encapsulation is a core concept in object-oriented programming that involves bundling data (attributes) and 
# methods (functions) that operate on the data within a class, restricting access to some of the object's components. 
# This helps protect the integrity of the data and only allows controlled modifications through specific methods.

# Here’s an example using Pokémon:

# Class Definition and Encapsulation:
# Let’s say we have a class Pokemon that encapsulates attributes like the Pokémon's name, level, and hit points (HP). 
# The class provides methods to access or modify these attributes, but the internal details are hidden from external objects.

# Why Encapsulation?

# Protection: If HP were public, anyone could directly set it to a negative value (e.g., pikachu.hp = -50). 
# Encapsulation prevents this by using setter methods to enforce valid values.

# Controlled Modification: By using methods like set_hp(), we control how the HP value changes (e.g., adding conditions like ensuring it doesn't go negative).

# Data Hiding: The actual internal state of the Pokémon (like HP) is hidden from the external world. 
# This allows changes to how HP is handled internally without affecting the rest of the code.

# In Pokémon, this concept mirrors how certain attributes (like hidden stats or abilities) are not directly visible 
# or modifiable by the player but can only be accessed through specific actions or in-game methods (e.g., leveling up or using specific items).