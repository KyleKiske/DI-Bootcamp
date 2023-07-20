from datetime import datetime, timedelta

#Exercise 1 : When Will I Retire ?

# gender = input("Tell us your gender (either 'M' or 'F')")
# birthdate = input("Tell us your bidrthay in DD.MM.YYYY format ")

# def get_age(year, month, day):
#     time_now = datetime.now()

#     if (time_now.year < year):
#         print("You aren't even born yet.")
#         exit()
#     age = time_now.year - year
#     if (time_now.month < month):
#         age -= 1
#     elif (time_now.month == month):
#         if (time_now.day < day):
#             age -= 1
#     return age

# def can_retire(gender, date_of_birth):
#     date_obj = datetime.strptime(date_of_birth, '%d.%m.%Y').date()
#     year = date_obj.year
#     month = date_obj.month
#     day = date_obj.day
#     age_of_retirement = 0
#     if gender == "M":
#         age_of_retirement = 67
#     else:
#         age_of_retirement = 62
#     age = get_age(year, month, day)
    
#     if age >= age_of_retirement:
#         return True
#     else:
#         return False

# if can_retire(gender, birthdate):
#     print("YES")
# else:
#     print("NO")

#Exercise 2 : Sum

x = int(input("Give me number "))
sum = 0
for i in range(4):
    mult = int("1"*(i+1))
    sum += x*mult

print(sum)

