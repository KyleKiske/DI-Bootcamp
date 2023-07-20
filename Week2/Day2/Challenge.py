#Challenge 1

# number = int(input("Please enter a number > "))
# length = int(input("Please enter length > "))
# multiples = []
# for x in range(length):
#     multiples.append(number*(x+1))
# print(f"number {number} - length {length} -> {multiples}")

#Challenge 2

user_word = (input("Please write a word > "))
new_word = ""
for x in range(len(user_word)-1):
    if user_word[x] == user_word[x+1]:
        continue
    else:
        new_word += user_word[x]
new_word += user_word[-1]
print(new_word)
