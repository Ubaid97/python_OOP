from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "can digest large prey"

    def climb(self):
        return "can climb surfaces"

    def shed_skin(self):
        return "sheds skin"

# python_object = python()

# from animal class
# print(python_object.alive)
#
# from reptile class
# print(python_object.hunt())
#
# from snake class
# print(python_object.limbs)
#
# from python class
# print(python_object.shed_skin())
