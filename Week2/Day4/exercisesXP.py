from random import randint

#Exercise 1 : What Are You Learning ?def 

def display_message():
    return(print("We study the existence of full-stack developer"))  
display_message() 

# #Exercise 2: What’s Your Favorite Book ?

# the_title = "Hitchhiker\'s Guide to the Galaxy"
# def favorite_book(title):
#     return print(f"One of my favorite books is {title}")

# favorite_book(the_title)

# Exercise 3 : Some Geography

# def describe_city(city, country="Israel"):
#     return print(f"{city} is in {country}")

# describe_city("Stockholm", "Sweden")
# describe_city("Jerusalem")

#Exercise 4 : Random

# def give_me_a_number(number):
#     desired = randint(1, 100)
#     if (number == desired):
#         return print("Success message, woohoo!")
#     else:
#         return print(f"Fail. Your number {number}, desired number was {desired}")

# provided = 0

# while provided > 100 or provided < 1:
#     provided = int(input("Give me a number between 1 and 100 - "))

# give_me_a_number(provided)

#Exercise 5 : Let’s Create Some Personalized Shirts !

# def make_shirt(size, text):
#     return print (f"The size of the shirt is {size} and the text is {text}")

# make_shirt("XXXXXL", "Gotta get a grip")

# def make_shirt(size="L", text="I love Python"):
#     return print (f"The size of the shirt is {size} and the text is {text}")

# make_shirt()
# make_shirt("M")
# make_shirt(text="MERICA!!!")

#Exercise 6 : Magicians …

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(magic):
#     for x in magic:
#         print(x)
#     return

# show_magicians(magician_names)

# def make_great(magic):
#     for x in range(len(magic)):
#         magic[x] += " The Great"
#     return magic

# make_great(magician_names)
# show_magicians(magician_names)

#Exercise 7 : Temperature Advice

# def get_random_temp():
#     return (randint(-10, 40))

# def main():
#     temp = get_random_temp()
#     print(f"The temperature now is {temp} degrees Celsius.")
#     if temp < 0 :
#         print("Brrr, that\'s freezing! Wear some extra layers today")
#     elif temp <= 16 :
#         print("Quite chilly! Don\'t forget your coat")
#     elif temp <= 23 :
#         print("Get a pair of Jeans and you're good to go.")
#     elif temp <= 32 :
#         print("Bring your newest t-shirt outside.")
#     else:
#         print("Don't go outside. Hot as hell!")
#     return

# main()

#Exercise 8 : Star Wars Quiz

# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]

# def quiz():
#     answers = 0
#     for x in data:
#         print(x.get("question \n"))
#         user_answer = input("Tell us your answer -> ")
#         if (user_answer == x.get("answer")):
#             answers += 1
#     return print(f"you answered {answers}/{len(data)}")

# quiz()