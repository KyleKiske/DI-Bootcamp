#Exercise 1 : Pets

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# bengal = Bengal("Bengal", 5)
# chartreux = Chartreux("Chart", 3)
# siamese = Siamese("Siame", 7)
# all_cats = [bengal, chartreux, siamese]
# sara_pets = Pets(all_cats)
# sara_pets.walk()

#Exercise 2 : Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return (f"{self.name} is barking")
    def run_speed(self):
        return ((self.weight / self.age) * 10)
    def fight(self, other_dog):
        value_self = self.run_speed() * self.weight
        value_other = other_dog.run_speed() * other_dog.weight
        if (value_self > value_other):
            return (f"{self.name} won the fight over {other_dog.name}")
        else:
            return (f"{other_dog.name} won the fight over {self.name}")
        
bobby = Dog("Bobby", 5, 25)
big_mac = Dog("Big Mac", 6, 40)
dough = Dog("Dough", 2, 10)

if __name__ == '__main__' :
    print(bobby.bark())
    print(big_mac.fight(bobby))
    print(big_mac.fight(dough))
    print(bobby.fight(dough))

#Exercise 3 : Dogs Domesticated

