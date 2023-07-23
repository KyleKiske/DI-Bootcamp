#Old MacDonald’s Farm

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}
    def add_animal(self, name, count = 1):
        if name in self.animals:
            self.animals[name] += count
        else:
            self.animals[name] = count
    def get_info(self):
        print(f"{self.name}'s farm\n")
        for key,value in self.animals.items():
            print(f"{key} : {value}")
        print("\n\t E-I-E-I-O! ")
    
    
    def get_animal_types(self):
        animal_list = []
        for key in self.animals:
            animal_list.append(key)
        return sorted(animal_list)
    
    def get_short_info(self):
        list_animal = self.get_animal_types()
        result_string = f"{self.name}'s farm has "
        for x in range(len(list_animal)):
            result_string += list_animal[x]
            if (self.animals[list_animal[x]] > 1):
                result_string += "s"
            if (x == len(list_animal)-1):
                result_string += "."
            elif (x == len(list_animal)-2):
                result_string += " and "    
            else :
                result_string += ", "
        return result_string

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)   
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()

print(macdonald.get_animal_types())

print(macdonald.get_short_info())