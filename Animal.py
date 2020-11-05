
class Animal:

    # initialising class
    def __init__(self):

        # creating attributes
        self.alive = True
        self.spine = True
        self.lungs = True
        self.eyes = True

        # creating behaviours
    def breathe(self):
        return "Breathes to stay alive"

    def move(self):
        return "possesses mobility"

    def eat(self):
        return "eats to stay alive"

    def procreate(self):
        return "seeks mate"

# Instantiate class
# cat = Animal()
# cat inherits everything from parent class Animal
# print(cat.eat())

