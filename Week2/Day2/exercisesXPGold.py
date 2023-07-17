import random

#Exercise 1: Concatenate Lists

# list_one = [1, 2, 3]
# list_two = [1, 3, 5]
# for x in range(len(list_two)):
#     list_one.append(list_two[x])
# print(list_one)

#Exercise 2: Range Of Numbers

# for x in range(1500, 2501):
#     if (x % 5 == 0 and x % 7 == 0):
#         print(x)

#Exercise 3: Check The Index

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# username = input("Tell us your name > ")

# if (names.count(username) > 0):
#     print(names.index(username))

#Exercise 4: Greatest Number

# list_numbers = []
# for x in range(3):
#     list_numbers.append(int(input(f"Input the №{x+1} number: "))) 

# print(f"The greatest number is: {max(list_numbers)}")

#Exercise 5: The Alphabet

# import string
# print("Alphabet from a-z:")
# for letter in string.ascii_lowercase:
#     print(letter, end =" ")
#     if (letter in ('a', 'e', 'i', 'o', 'u')):
#         print ("Vowel")
#     else:
#         print("Consonant")

#Exercise 6: Words And Letters

# list_words = []
# for x in range(7):
#     list_words.append(input(f"Write me a word {x+1} > ")) 
# letter = input(f"Write me a single letter ")

# for x in range(len(list_words)):
#     if list_words[x].find(letter) >= 0:
#         print(list_words[x].find(letter))
#     else:
#         print(f"{list_words[x]} nope {letter}")

#Exercise 7:

# list_omg = []

# for x in range(1,1000001) :
#     list_omg.append(x)
# print(min(list_omg))
# print(max(list_omg))
# print(sum(list_omg))

#Exercise 8 : List And Tuple

sequence = input("write a sequence of numbers, separated by commas \n")
sequence_list = sequence.split(',')
sequence_tulpe = tuple(sequence_list)

print(sequence_list)
print(sequence_tulpe)

#Exercise 9 : Random Number

# letter = int(input(f"Write me a number from 1 to 9 "))

# guess = random.randint(1, 9)

# if (letter == guess):
#     print("Winner")
# else:
#     print("better luck next time")