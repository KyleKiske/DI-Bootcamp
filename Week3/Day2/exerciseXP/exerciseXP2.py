from exerciseXP import Dog
from random import choice

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained
    def train(self):
        self.trained = True
        print(self.bark())
    def play(self, *Dogs):
        output = self.name
        for dog in Dogs:
            output += ", "
            output += dog.name
        output += " all play together"
        print(output)
    def do_a_trick(self):
        tricks = ["does a barrel roll",
                    "stands on his back legs",
                    "shakes your hand",
                    "plays dead"]
        if self.trained:
            trick = choice(tricks)
            print(f"{self.name} {trick}")


chloe = PetDog("Chloe", 2, 8)
timmy = PetDog("Timmy", 3, 10)
rex = PetDog("Rex", 6, 22)
chloe.play(timmy, rex)
rex.do_a_trick()
rex.train()
rex.do_a_trick()
rex.do_a_trick()
rex.do_a_trick()