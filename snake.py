from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = True
        self.limbs = False

    def use_tongue_to_smell(self):
        return "smell using tongue"

# snake_object = Snake()

# attribute from animal class
# print(snake_object.lungs)

# function from reptile class
# print(snake_object.seek_heat())

# attribute from snake class
# print(snake_object.forked_tongue)
