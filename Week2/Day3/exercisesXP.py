#Exercise 1 : Convert Lists Into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)

#Exercise 2 : Cinemax

# total_ticket_price = 0
# price_child = 10
# price_bigger_child = 15
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# family_payment = dict()
# total_ticket_price = 0

# for key in family:
#     if family[key] < 3:
#         family_payment[key] = 0
#     elif family[key] <= 12:
#         family_payment[key] = price_child
#         total_ticket_price += price_child
#     else:
#         family_payment[key] = price_bigger_child
#         total_ticket_price += price_bigger_child

# print(f"Total:  {total_ticket_price}")
# print(family_payment)

# Exercise 3: Zara

# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": "Amancio Ortega Gaona" ,
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"], 
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue", 
#         "Spain": "red", 
#         "US": ["pink", "green"] 
#         }
# }
# print(f"Brandinfo\n {brand}")
# brand["number_stores"] = 2
# print(f"Core audience - {brand['type_of_clothes']}")
# brand["country_creation"] = 'Spain'

# if "international_competitors" in brand.keys():
#     brand["international_competitors"].append("Desigual")

# del brand["creation_date"]

# print(brand["international_competitors"][-1])
# print(brand["major_color"]["US"])
# print(len(brand))
# print(brand.keys())
# print(brand)

# more_on_zara = { 
#     "creation_date": 1975,
#     "number_stores": 10000
# }

# for key,val in more_on_zara.items():
#     brand[key] = val

# print(brand["number_stores"])

#Number of stores updated value and creation date was added as new thing.

# Exercise 4 : Disney Characters

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# disney_users_A = dict()
# for x in range(len(users)):
#     disney_users_A[users[x]] = x

# disney_users_B = dict()
# for x in range(len(users)):
#     disney_users_B[x] = users[x]

# disney_users_D = dict()
# for x in range(len(users)):
#     if (users[x].__contains__('i')):
#         disney_users_D[users[x]] = x

# disney_users_D2 = dict()
# for x in range(len(users)):
#     if (users[x].find('m'.capitalize()) == 0 or users[x].find('p'.capitalize()) == 0):
#         disney_users_D2[users[x]] = x

# users.sort()

# disney_users_C = dict()
# for x in range(len(users)):
#     disney_users_C[users[x]] = x

# print(disney_users_A)
# print(disney_users_B)
# print(disney_users_C)
# print(disney_users_D)
# print(disney_users_D2)
