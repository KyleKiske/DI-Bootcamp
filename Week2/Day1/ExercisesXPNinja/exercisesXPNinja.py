
#Exercise 4 

# my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
#            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#            Ut enim ad minim veniam, quis nostrud exercitation ullamco 
#            laboris nisi ut aliquip ex ea commodo consequat. 
#            Duis aute irure dolor in reprehenderit in voluptate velit 
#            esse cillum dolore eu fugiat nulla pariatur. 
#            Excepteur sint occaecat cupidatat non proident, 
#            sunt in culpa qui officia deserunt mollit anim id est laborum."""

# print(len(my_text))

# Exercise 5

cur_length = 0
while(True) :
    print(f"current longest sentence is {cur_length}")
    print("Type 'exit' to exit the loop")
    sentence = input("Try to type sentence without letter A\n")
    if (sentence.upper().find("A") != -1) :
        print("your sentence have symbol A. Try again")
    elif (sentence == "exit") :
        break
    else :
        if (cur_length < len(sentence)):
            cur_length = len(sentence)
            print(f"New longest sentence is {cur_length}. Well done!")
        else:
            print("Current length is longer. Try again")
print("THE END")