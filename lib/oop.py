# A bstraction
# P olymorphism
# I nheritance
# E ncapsulation

class Pokemon():
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.level = 0

    def attack():
        # choses its main attack, focuses and attacks
        # "Pikachu attacks"
        if self.name == 'Pikachu':
            return "Pikachu attacks with electricity"
        elif self.name == 'Charmander':
            return "Charmander attacks with fire"
        ### we have another 50 pokemons
        elif self.name == 'Bulbasaur':
            return "Bulbasaur attacks with nature skills"

    def use_move():
        if self.name == 'Pikachu':
            return 'some movement specific to Pikachu'
        elif self.name == 'Charmander':
            return "some movevement specific to Charmander"
        ### we have another 50 pokemons
        elif self.name == 'Bulbasaur':
            return "Bulbasaur attacks with nature skills"




pikachu = Pokemon('Pikachu')
pikachu.attack()

bulbasaur = Pokemon('Bulbasaur')
bulbasaur.attack()