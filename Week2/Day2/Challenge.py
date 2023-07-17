#Challenge 1

number = int(input("Please enter a number > "))
length = int(input("Please enter length > "))
multiples = []
for x in range(length):
    multiples.append(number*(x+1))
print(f"number {number} - length {length} -> {multiples}")

#Challenge 2

# user_word = (input("Please write a word > "))
# letters_to_delete = []
# for x in range(len(user_word)-1, 0, -1):
#     if user_word[x] == user_word[x-1]:
#         letters_to_delete.append(x)
# for x in range(len(letters_to_delete)):
#     user_word = user_word[0:letters_to_delete[x]:] + user_word[letters_to_delete[x]+1: : ]

# print(user_word)
