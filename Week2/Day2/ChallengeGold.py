from datetime import datetime, timedelta

birthdate = input("Tell us your bidrthay in DD.MM.YYYY format ")
print(birthdate)
date_obj = datetime.strptime(birthdate, '%d.%m.%Y').date()
print(date_obj)

time_difference = datetime.now().date() - date_obj
time_now = datetime.now()

if (time_now.year < date_obj.year):
    print("You aren't even born yet.")
    exit()
age = time_now.year - date_obj.year
if (time_now.month < date_obj.month):
    age -= 1
elif (time_now.month == date_obj.month):
    if (time_now.day < date_obj.day):
        age -= 1


needed_age = age % 10
print(needed_age)

top = "       ______"
top2 = "      |:H:a:p:p:y:|"
top3 = "    __|___________|__"
bottom1 = "   |^^^^^^^^^^^^^^^^^|"
bottom2 = "   |:B:i:r:t:h:d:a:y:|"
bottom3 = "   |                 |"
bottom4 = "   ~~~~~~~~~~~~~~~~~~~"

if (needed_age < 5):
    top = top[:(10+((5-needed_age)//2))] + "i"*needed_age + "_"*(5-needed_age) + top[(10+((5-needed_age)//2)):]
elif(needed_age == 5):
    top = top[:10] + "i"*needed_age + "_"*(5-needed_age) + top[10:]
else :
    top = top[:(10-((needed_age-5)// 2))] + "i"*needed_age + top[(10-((needed_age-5)// 2)):-(needed_age-5)]

print(top)
print(top2)
print(top3)
print(bottom1)
print(bottom2)
print(bottom3)
print(bottom4)
