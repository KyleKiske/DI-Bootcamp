from math import pi, pow
from random import randint

#Exercise 1 : Geometry

# class Circle:
#     def __init__(self, radius = 1.0):
#         self.radius = radius

#     def calc_perimeter(self):
#         perimeter = 2 * self.radius * pi
#         return perimeter
    
#     def calc_area(self):
#         area = pow(self.radius, 2)  * pi
#         return area
    
# cirlce = Circle()
# print(f"Perimeter = {cirlce.calc_perimeter()}")
# print(f"Area = {cirlce.calc_area()}")

# print("same for radius 3")
# cirlce3 = Circle(3)
# print(f"Perimeter = {cirlce3.calc_perimeter()}")
# print(f"Area = {cirlce3.calc_area()}")

#Exercise 2 : Custom List Class

# class MyList:
#     def __init__(self, letters: list()):
#         self.letters = letters
#     def reversed(self):
#         result = self.letters
#         result.reverse()
#         return result
#     def sorted(self):
#         result = self.letters
#         result.sort()
#         return result
#     def numbers(self):
#         numbers = []
#         for letter in self.letters:
#             numbers.append(randint(0, 9))
#         return numbers

# the_list = MyList(['a','s','f','b','l'])
# print(the_list.letters)
# print(the_list.reversed())
# print(the_list.sorted())
# print(the_list.numbers())

#Exercise 3 : Restaurant Menu Manager

class MenuManager:
    def __init__(self, menu: list = []):
        self.menu = menu

    def add_item(self, name, price, spice, gluten):
        item = {"name" : name,
                "price": price,
                "spice": spice,
                "gluten": gluten}
        for i in range(len(self.menu)):
            if self.menu[i]["name"] == name:
                print("This dish is already in menu")
                return
        self.menu.append(item)

    def update_item(self, name, price, spice, gluten):
        changed = False
        item = {"name" : name,
                "price": price,
                "spice": spice,
                "gluten": gluten}
        for i in range(len(self.menu)):
            if self.menu[i]["name"] == name:
                self.menu[i] = item
                changed = True
                break
        if not changed:
            print(f"The dish \"{name}\" is not in the menu.")

    def display_menu(self):
        for x in self.menu:
            print(x)
        
    def remove_item(self, name):
        deleted = False
        for i in range(len(self.menu)):
            if self.menu[i]["name"] == name:
                del self.menu[i]
                deleted = True
                break
        if not deleted:
            print(f"The dish \"{name}\" was not in the menu.")
        else:
            print(f"Menu after removal of {name}:")
            print(self.menu)

menu = MenuManager()
menu.add_item("A", 1, "A", True)
menu.add_item("B", 2, "A", False)
menu.add_item("B", 2, "A", False)
menu.add_item("C", 3, "C", True)
menu.remove_item("C")
menu.remove_item("C")
menu.update_item("A", 1000, "A", True)
menu.update_item("C", 1000, "A", True)
menu.display_menu()