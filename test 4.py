# print(type("Hello world"))

# print(dir(str))

class Character:
    name = ''
    power = 0
    energy = 100
    hands = 2

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

    def chalengee_aliase(self, new_alias):
        print(self)
        self.aliase = new_alias


peter = Character()
peter.name = 'Peter Parker'
peter.power = 70
peter.alias = 'Spider-Man'

bruce = Character()
bruce.name = 'Bruce Wayne'
bruce.power = 85
bruce.alias = 'Batman'

# print(peter.name)
# print(peter.power)
# print(peter.energy)
# print(peter.hands)


