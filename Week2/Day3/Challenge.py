#Challenge 1

word = input("Please enter a word > ")
letter_dictionary = dict()

for x in range(len(word)):
    if (letter_dictionary.get(word[x]) == None):
        letter_dictionary[word[x]] = []
    letter_dictionary[word[x]].append(x)

print(letter_dictionary)

#Challenge 2

# items_purchase = {
#   "Water": 1,
#   "Bread": 3,
#   "TV": 1000,
#   "Fertilizer": 20
# }

# wallet = (int(input("Tell uo how much money do you have - ")))

# result = []

# for key,value in items_purchase.items():
#     if value < wallet:
#         result.append(key)
# result.sort()
# if len(result) != 0:
#     print(result)
# else:
#     print("Nothing")