# Base class Pokemon with Abstraction
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


    # Public method to use a move (Abstraction + Polymorphism)
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
    def __choose_move(self):
        return "Thunderbolt"

# Charmander subclass
class Charmander(Pokemon):
    def __choose_move(self):
        return "Flamethrower"

# Squirtle subclass
class Squirtle(Pokemon):
    def __choose_move(self):
        return "Water Gun"

# Using the classes with Inheritance, Polymorphism, and Abstraction
pokemon_team = [Pikachu("Pikachu", 5), Charmander("Charmander", 7), Squirtle("Squirtle", 6)]
for pokemon in pokemon_team:
    pokemon.use_move()   # Same method, different outcomes (Polymorphism)










# Why Polymorphism?

# 1. Uniform Interface with Different Behaviors: The use_move() method is the same across all Pokémon,
#  but each subclass (Pikachu, Charmander, Squirtle) implements its own unique move by overriding __choose_move().
#  This allows a uniform interface while having different underlying behaviors. 
# You don't need to know what specific Pokémon it is—just call use_move() and it will do the right thing.

# 2. Easier Code Management: The code for handling Pokémon is simplified 
# because you don’t need to write separate methods for each Pokémon’s moves. 
# Instead, you can treat all Pokémon uniformly by calling the same method (use_move()), 
# making the code easier to manage and extend when adding more Pokémon in the future.

# 3. Extensibility with Flexible Functionality: As new Pokémon are added, you can simply extend 
# the base class and implement the specific move choice. The polymorphic behavior ensures that the use_move() 
# method will call the correct move for each new Pokémon, without modifying the core structure of the Pokemon class or the overall interface.