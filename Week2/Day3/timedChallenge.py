#Timed 1

# sentence = input('your input\n')
# list_word = sentence.split()
# list_word.reverse()
# sentence =" ".join(list_word)
# print(sentence)

#Timed 2

number = int(input("Enter a number "))

bcd = number // 2
sum_of_divisors = 0
for x in range(bcd, 0, -1):
    if (number % x == 0):
        sum_of_divisors += x

print(sum_of_divisors)
if (number == sum_of_divisors):
    print(True)
else:
    print(False)