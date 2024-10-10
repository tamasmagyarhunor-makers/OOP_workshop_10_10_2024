class Pokemon:
    def __init__(self, name, level):
        self.name = name        # public attribute
        self.level = level      # public attribute
        self.__hp = 100         # private attribute (encapsulated)
    
    def get_hp(self):           # public method to access HP
        return self.__hp
    
    def set_hp(self, new_hp):   # public method to modify HP safely
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
        # Here the move is chosen; details are hidden
        return "Thunderbolt"
    
    def __calculate_power(self, move):
        # Complex logic for calculating power, hidden from the user
        return 90  # base power for Thunderbolt
    
    def __calculate_accuracy(self, move):
        # Complex logic for calculating accuracy, hidden from the user
        return 100  # Thunderbolt has 100% accuracy
    
    def __execute_move(self, move, power, accuracy):
        # Executes the move, combining power and accuracy
        print(f"{self.name} uses {move} with {power} power and {accuracy}% accuracy!")


# Using the class with abstraction
pikachu = Pokemon("Pikachu", 5)
pikachu.use_move()


# Why Abstraction?
# 1. Hides Complex Details: The use_move() method provides a high-level way to use a Pokémon's move, 
# but all the complex details (choosing the move, calculating power and accuracy) are hidden in private methods. 
# The player just needs to call use_move(), and everything else happens behind the scenes.

# 2. Clean and Simple Interface: The user doesn’t need to deal with different steps like choosing a move, 
# calculating stats, or executing it. These details are abstracted away, making the interaction simple and straightforward.

# 3. Modular Code: The private methods (__choose_move(), __calculate_power(), __calculate_accuracy()) are encapsulated within the class, 
# meaning that they can be modified independently without affecting how the use_move() function is called. 
# This keeps the public interface consistent while allowing internal flexibility.