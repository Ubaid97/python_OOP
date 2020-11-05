from Animal import Animal

class Reptile(Animal):
    def __init__(self):

        # Super is used to inherit everything from parent class
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = True
        self.heart_chambers = [3, 4]

    def seek_heat(self):
        return "wants to keep warm"

    def hunt(self):
        return "hunts for food"

    def use_venum(self):
        return "use of deadly poison"

# reptile_object = Reptile()
#
# reptile_object (instance of Reptile class) inherits behaviours and attributes from Parent class Animal
# print(reptile_object.eat())
# print(reptile_object.procreate())
# print(reptile_object.alive)
#
# print(reptile_object.hunt())
# print(reptile_object.tetrapod)