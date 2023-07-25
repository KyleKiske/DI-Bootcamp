from func import addition 
import random
import string
from datetime import datetime, timedelta
from faker import Faker
#Exercise 1: Currencies

# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __int__(self):
#         return(self.amount)
#     def __str__(self):
#         if (self.amount > 1):
#             return(f"{self.amount} {self.currency}s")
#         else:
#             return(f"{self.amount} {self.currency}")
#     def __repr__(self) -> str:
#         return(self.__str__())
#     def __add__(self, other):
#         if (type(other) == int):
#             return (self.amount + other)
#         elif (type(other) == Currency):
#             if (other.currency != self.currency):
#                 raise Exception("Cannot add between Currency type " + self.currency +" and " + other.currency)
#             else:
#                 self.amount += other.amount
#                 return (self)
#     def __iadd__(self, value):
#         self.amount += value
#         return (self)
    
# c1 = Currency("dollar", 5)
# c2 = Currency("dollar", 10)
# cEuro = Currency("Euro", 7)

# print("str")
# print(str(c1))
# print("int")
# print(int(c1))
# print("repr(c1)")
# print(repr(c1))
# print("c1")
# print(c1)
# print("c1 + 5")
# print(c1 + 5)
# c1 += 10
# print('c1 after += 10')
# print(c1)
# print("c1 + c2")
# print(c1 + c2)
# c1 + cEuro

#Exercise 2: Import

# addition(2, 87)

#Exercise 3: Random Module

# def get_rand(number):
#     if number > 100 or number < 1:
#         print ("Your number should be between 1 and 100")
#         return
#     result = randint(1,100)
#     if (result == number):
#         print("Wow, that was very lucky!")
#         return
#     else:
#         print("Nope")

# get_rand(22)

#Exercise 4: String Module

# result_str = ''.join(random.choice(string.ascii_letters) for i in range(5))
# print(result_str)

#Exercise 5 : Current Date

# print(datetime.now().date())

#Exercise 6 : Amount Of Time Left Until January 1st

# def timeleft():
#     now = datetime.now()
#     january_st = datetime(datetime.now().year+1, 1,1)
#     delta = january_st - now
#     days = delta.days


#     print(f"The 1st of January in {delta.days} days and {delta.seconds//3600}:{(delta.seconds//60)%60}:{(delta.seconds - delta.seconds // 3600 * 3600) - ((delta.seconds//60)%60)*60} hours")

# timeleft()  

#Exercise 7 : Birthday And Minutes

# def lifespan(birthdate):
#     the_date = datetime.strptime(birthdate, "%d.%m.%Y")
#     delta = datetime.now() - the_date
#     print (f"You've lived {delta.days*24*60 + delta.seconds//60} minutes thus far.")

# birthdate = input("Please provide us your birthdate in format dd.MM.YYYY ")

# lifespan(birthdate)

#Exercise 8 : Faker Module

users = list()

print(users)
def add_fake_data(users):
    fake = Faker()
    name = fake.name()
    address = fake.address()
    code = fake.language_code()
    my_dict = {"name" : name ,"address": address,"code": code}
    users.append(my_dict)
    return users
    
add_fake_data(users)
add_fake_data(users)
for x in users:
    print(x)