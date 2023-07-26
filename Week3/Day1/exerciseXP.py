#Exercise 1: Cats

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# bobby = Cat("Bobby", 3)
# tom = Cat("Tom", 5)
# funky = Cat("Funky", 2)

# cat_list = []
# cat_list.append(Cat("Bobby", 3))
# cat_list.append(Cat("Tom", 5))
# cat_list.append(Cat("Shiro", 2))

# def find_oldest(cat_list):
#     oldest = cat_list[0]
#     for x in cat_list:
#         if x.age > oldest.age:
#             oldest = x
#     return oldest

# oldest = find_oldest(cat_list)

# print (f"The oldest cat is {oldest.name} and is {oldest.age} years old.")

#Exercise 2 : Dogs

# class Dog:
#     def __init__(self, name: str, height: int):
#         self.name = name
#         self.height = height

#     def bark(self):
#         print(f"{self.name} goes Woof!")

#     def jump(self):
#         print(f"{self.name} jumps {self.height *2} cm high!")

# davids_dog = Dog("Rex", 50)
# print(davids_dog.name)
# print(davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20)
# print(sarahs_dog.name)
# print(sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()

# if (davids_dog.height > sarahs_dog.height):
#     print (f"{davids_dog.name} is bigger")
# elif (davids_dog.height < sarahs_dog.height):
#     print (f"{sarahs_dog.name} is bigger")
# else:
#     print (f"{sarahs_dog.name} and {davids_dog.name} are of the same height")

#Exercise 3 : Who’s The Song Producer?

# class Song:
#     def __init__(self, lyrics: list):
#         self.lyrics = lyrics
#     def sing_me_a_song(self):
#         for x in self.lyrics:
#             print(x)

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()

#Exercise 4 : Afternoon At The Zoo

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        self.animals.append(new_animal)
    def get_animals(self):
        print(self.animals)
    def sell_animal(self, animal_sold):
        if (self.animals.count(animal_sold) > 0):
            self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_animal = sorted(self.animals)
        for animal in sorted_animal:
            animal = animal.capitalize()
        current_animal = sorted_animal[0]
        animal_groups = {}
        group = 1
        animal_groups[group] = [current_animal]
        
        for animal in sorted_animal[1:]:
            if current_animal[0] == animal[0]:
                animal_groups[group].append(animal)
            else:
                group += 1
                animal_groups[group] = list(animal.split(" "))
                current_animal = animal
        for key,value in animal_groups.items():
            if len(value) == 1:
                animal_groups[key] = "".join(value)
        return animal_groups
    
    def get_groups(self) :
        print(self.sort_animals())

ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.add_animal("Bobcat")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Ape")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Gibbon")
ramat_gan_safari.add_animal("Antelope")
ramat_gan_safari.add_animal("Alligator")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
