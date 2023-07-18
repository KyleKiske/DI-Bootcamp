# Exercise 1

my_fav_numbers = {5, 7, 42}
my_fav_numbers.add(34)
my_fav_numbers.add(75)
my_fav_list = list(my_fav_numbers)
print(f"My fav nums: {my_fav_numbers}")
print(f"My fav list {my_fav_list}")
my_fav_list.pop()
my_fav_numbers.remove(75)
print(f"My fav nums after 75 removal: {my_fav_numbers}")
print(f"My fav list after {my_fav_list}")

friend_fav_numbers = {5, 33, 22}
print(f"Friend fav nums: {friend_fav_numbers}")

combined_set = my_fav_numbers.union(friend_fav_numbers)
print(f"Combined set {combined_set}")

# Exercise 2

#No, because Tulpe is immutable data type.

# Exercise 3 

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

# Exercise  4 

#Float is used to represent real numbers.
# float_list = []
# for x in range(3, 10):
#     float_list.append(x/2)

# print(float_list)

# Exercise 5

# for x in range(1, 21):
#     print(x)

# print("only even index")
# for x in range(1, 21):
#     if x % 2 == 0:
#         print(x)

# Exercise 6

# desired_name = "Dmitri"
# guess = ""
# while guess != desired_name:
#     guess = input("Tell me your name (if your name will match with mine, this loop will stop) > ")

# Exercise 7

# favourite_fruits = input("Tell me your favourite fruits (if you have several, separate them with space): ")

# list_favourite_fruits = favourite_fruits.split()

# chosen_fruit = input("Pick a fruit ")
# if list_favourite_fruits.count(chosen_fruit) > 0:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

# Exercise 8

# total_price = 10
# topping_list = []
# while(True) :
#     topping = input("Add your desired toping for a pizza, or type 'exit' to finish\n")
#     if (topping == "exit") :
#         break
#     else :
#         print(f"you’ll add {topping} to your pizza")
#         total_price += 2.5
#         topping_list.append(topping)

# print("Here are your toppings")
# for x in range(len(topping_list)):
#     print(topping_list[x])
# print(f"Total price will be {total_price}")

# Exercise 9

# total_ticket_price = 0
# price_child = 10
# price_bigger_child = 15
# family_age = input("Tell me ages of people who will be watching (separate them with space): ")
# list_family_age = family_age.split()
# list_family_age = list(map(int, list_family_age))

# for x in list_family_age:
#     if x < 3:
#         continue
#     elif x <= 12:
#         total_ticket_price += price_child
#     else:
#         total_ticket_price += price_bigger_child

# print(f"Total ticket price for a family is {total_ticket_price}\n")

# teenagers_names = input("Tell me names of people who (separate them with space): ")
# list_teenagers_names = teenagers_names.split()
# list_teenagers_ages = []
# for x in range(len(list_teenagers_names)):
#     list_teenagers_ages.append(int(input(f"Tell me age of {list_teenagers_names[x]} :"))) 

# final_list = []
# for x in range(len(list_teenagers_names)):
#     if (21 >= list_teenagers_ages[x] >= 16):
#         final_list.append(list_teenagers_names[x])

# print(f"List of teens who can attend {final_list}")

#Exercise 10

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# while (sandwich_orders.count("Pastrami sandwich") > 0):
#     sandwich_orders.remove("Pastrami sandwich")
# finished_sandwiches = []
# while (sandwich_orders):
#     finished_sandwiches.append(sandwich_orders[0])
#     sandwich_orders.pop(0)
# for x in range(len(finished_sandwiches)):
#     print(f"I finished your {finished_sandwiches[x]}")