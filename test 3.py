# print(type("Hello world"))

# print(dir(str))

from typing_extensions import Self


class Character:
    # name = ''
    # power = 0
    # energy = 100
    # hands = 2
    
    
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.backpack = []
        self.hands = hands
      
    def eat(self, food):
        if self.energy < 100:
            self.energy += food
        else:
            print('Not hungry')

    def do_exercise(self, hourse):
        if self.energy > 0:
            self.energy -= hourse * 2
            self.power += hourse *2
        else:
            print('Too tired')

    def chalenge_aliase(self, new_alias):
        print(self)
        self.alias = new_alias

    def beat_up(self, foe):
        if not isinstance(foe, Character):
            return
        if foe.power < self.power:
            foe.status = 'defeated'
            self.statuse = 'winner'
        else:
            print('Retreat!')



peter = Character('Peter Parker', 70)
# peter.name = 'Peter Parker'
# peter.power = 70
peter.alias = 'Spider-Man'
peter.backpack.append('Web-shooter')

bruce = Character('Bruce Wayne', 85)
# bruce.name = 'Bruce Wayne'
# bruce.power = 85
bruce.alias = 'Batman'

# print(peter.name)
# print(peter.power)
# print(peter.energy)
# print(peter.hands)

bruce.chalenge_aliase('Dark Knight')
bruce.do_exercise(10)

# print(bruce.power)
# print(bruce.energy)
# print(bruce.alias)

