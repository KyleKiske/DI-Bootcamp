the_string = input("Write a sentence exactly 10 characters long\n")
if len(the_string) > 10:
    print("string too long")
    exit()
if len(the_string) < 10:
    print("string not long enough")
    exit()
if len(the_string) == 10:
    print("perfect string")

print(f"first letter - {the_string[0]}. Last letter - {the_string[-1]}")

for x in range(len(the_string)) :
    print(the_string[:x+1])