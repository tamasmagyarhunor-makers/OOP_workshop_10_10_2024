class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.__hp = 100

    def get_hp(self):          
        return self.__hp

    def set_hp(self, new_hp):  
        if new_hp >= 0:
            self.__hp = new_hp
        else:
            print(f"{self.name}'s HP cannot be negative!")
    
    # Public method to use a move (Abstraction)
    def use_move(self):
        move = self.__choose_move()
        power = self.__calculate_power(move)
        accuracy = self.__calculate_accuracy(move)
        self.__execute_move(move, power, accuracy)
    
    # Private methods (details hidden from the user)
    def __choose_move(self):
        raise NotImplementedError("Subclass must implement move choice")
    
    def __calculate_power(self, move):
        # Logic to calculate power based on move and Pokémon specifics
        return 90  # Default base power
    
    def __calculate_accuracy(self, move):
        return 100  # Default accuracy for all moves
    
    def __execute_move(self, move, power, accuracy):
        print(f"{self.name} uses {move} with {power} power and {accuracy}% accuracy!")

# Pikachu subclass
class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(name, level)
        self.__hp = 50

    def __choose_move(self):
        return "Thunderbolt"
    
    def elecrify():
        #attack with elecricity
        pass

class Raichu(Pikachu):
    def __init__(self):
        super().__init__()
        self.__hp = 75

# Charmander subclass
class Charmander(Pokemon):
    def __choose_move(self):
        return "Flamethrower"

# Using the classes with Inheritance and Abstraction
pikachu = Pikachu("Pikachu", 5)
charmander = Charmander("Charmander", 7)

pikachu.use_move()              # Pikachu uses Thunderbolt
charmander.use_move()           # Charmander uses Flamethrower


# Why Inheritance?

# 1. Reusability: The Pokemon class provides a common structure (like HP management and the use_move() method) 
# that is reused in all Pokémon subclasses. This prevents code duplication and makes it easier 
# to manage shared features like power calculation or move execution logic.

# 2. Specialization: Each Pokémon subclass (e.g., Pikachu, Charmander) can specialize certain behaviors, 
# like the choice of moves, by overriding the private method __choose_move(). 
# This allows each Pokémon to behave according to its specific type while still inheriting the general structure from the base class.

# 3. Extensibility: New Pokémon can be added easily by creating new subclasses that inherit from the Pokemon base class. 
# They only need to implement the private method __choose_move(), while the rest of the functionality (HP, move execution) remains consistent. 
# This makes it easy to extend the program to support new Pokémon with minimal code changes.