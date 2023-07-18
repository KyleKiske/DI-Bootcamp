#Exercise 1, 2, 3: Birthday Look-Up, Birthdays Advanced, Add Your Own Birthday

birthdays = {
    "Emma" : "2000/02/12",
    "Sitch" : "1993/05/11",
    "Adam" : "1988/08/02",
    "Carl" : "1977/09/30",
    "Ana" : "1990/10/22"
}

person_name = input("Tell us your name - ")
person_bday = input("Tell us your birthday in YYYY/MM/DD format - ")

birthdays[person_name] = person_bday

print("You can look up the birthdays of the people in the list!")

name = input("give me a name of person -> ")

if (birthdays.keys().__contains__(name)):
    print(f"WOAH. {name} was born on {birthdays.get(name)}")
else:
    print(f"Sorry, we don\'t have the birthday information for {name}.")

#Exercise 4: Fruit Shop

# items = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }

# for key,value in items.items():
#     print(f"{key} costs {value}", end=". ")

# items = {
#     "banana": {"price": 4 , "stock":10},
#     "apple": {"price": 2, "stock":5},
#     "orange": {"price": 1.5 , "stock":24},
#     "pear": {"price": 3 , "stock":1}
# }

# total_cost = 0

# for value in items.values():
#     cost = 1
#     for val in value.values():
#         cost *= val
#     total_cost += cost

# print(f"total_cost of all items will be {int(total_cost)}")