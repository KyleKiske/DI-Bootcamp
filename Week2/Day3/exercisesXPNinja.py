cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet, Cadillac, Renault"

list_cars = cars.split(',')

print(f"There are {len(list_cars)} manufacturers in the list")

list_cars.sort(reverse=True)
print(list_cars)

man_with_o = 0
man_without_i = 0
for x in range(len(list_cars)):
    if (list_cars[x].upper().__contains__('O')):
        man_with_o += 1
    if not list_cars[x].upper().__contains__('I'):
        man_without_i += 1

print(man_with_o)
print(man_without_i)

list2 = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

set_list2 = set(list2)
result = ""
for x in set_list2:
    result += x + ","

print(result[:-1])

list_cars.sort()

for x in range(len(list_cars)):
    list_cars[x] = list_cars[x].strip()
    list_cars[x] = sorted(list_cars[x])
    list_cars[x].reverse()
    list_cars[x] = ''.join(list_cars[x])
print(list_cars)