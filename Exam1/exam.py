# Python Basics

# Data Types

# Which of the following is not a mutable data type in Python?
# a) List
# b) Dictionary
# c) Tuple
# d) Set

# Immutable type is Tuple

# Lists and Loops

# Using a list comprehension, generate a list of the squares of numbers from 1 to 10, but only include squares of even numbers.

number_list = [x*x for x in range(1, 11) if x % 2 == 0]
print(number_list)

# Using the range function, create a list of numbers from 1 to 10, then print numbers that are divisible by both 2 and 3.
numbers = []
for i in range(10):
    numbers.append(i+1)
print(numbers)

print ('divisible by both 2 and 3')
for i in numbers:
    if (i % 2 == 0 and i % 3 == 0 ):
        print(i)


# Loop through the provided list of dictionaries and print the names and ages:

student_list = [
    {
    "name": "John", 
    "age": 24
    }, 
    {
    "name": "Anna", 
    "age": 22
    }, 
    {
    "name": "Mike", 
    "age": 25
    }
]

for i in student_list:
    print(i['name'])

#Function Behavior with *args and **kwargs

# Write a function combine_words that accepts any number of positional arguments and key-value arguments. The function should return a single sentence combining all the words provided.
def combine_words(*args, **kwargs):
    result_string = ""
    for a in args:
        result_string += (a+" ")
    for kwa in sorted(kwargs):
        # if (kwa == 'second'):
            result_string += (kwargs[kwa] + " ")

    return result_string    

print(combine_words("Hello", "world", second="is", third="great!", first="Python"))

# Object-Oriented Programming (OOP)
# Create a class Vehicle with string attributes type, brand, and integer attribute year. 
# Ensure instances of the vehicle cannot be created if any of these attributes are missing and include a method to display the vehicle’s info. Use dunder method.

class Vehiche:
    def __init__(self, type, brand, year: int) -> None:
        self.type = type
        self.brand = brand
        self.year = year

    def __str__(self) -> str:
        return (f'type = {self.type}, brand = {self.brand}, year = {str(self.year)}')

toyota = Vehiche("sports", 'Toyota', 1992)
honda = Vehiche("Sports-prototype", 'Honda', 1996)

print(honda)
print(toyota)

# OOP Inheritance and Decorators

# Create a class Car with string attributes brand, model, and integer attribute mileage. Implement a method to return the car’s details.
class Car:
    def __init__(self, brand, model, mileage : int) -> None:
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def get_details(self):
        result = {
            "brand" : self.brand,
            "model" : self.model,
            "mileage" : self.mileage
        }
        return result

skoda = Car("Skoda", 'Rapid', 100000)
print(skoda.get_details())

# Create a subclass ElectricCar inheriting from Car with an additional float private attribute __battery_capacity. Override the car’s details method to include the battery capacity.
# Use the @property decorator to get the battery_capacity value and @battery_capacity.setter to modify the battery capacity only if the new value is positive.

class ElectricCar(Car):
    def __init__(self, brand, model, mileage: int, battery_capacity: float) -> None:
        super().__init__(brand, model, mileage)
        self.__battery_capacity = battery_capacity

    def get_details(self):
        result = {
            "brand" : self.brand,
            "model" : self.model,
            "mileage" : self.mileage,
            "battery capacity" : self.battery_capacity()
        }
        return result

    @property
    def battery_capacity(self):
        return self.__battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, new_capacity):
        if new_capacity > 0:
            self.__battery_capacity = float(new_capacity)
        else :
            print('Battery capacity should be positive.')

tesla = ElectricCar("Tesla", "SV", 1000, 800.0)

print(tesla.battery_capacity)
tesla.battery_capacity = 500

print(tesla.battery_capacity)
tesla.battery_capacity = -500

# Create a BankAccount class with private float attribute _balance and private string attribute _account_holder. 
# Implement methods to deposit, withdraw, and view the balance.
# Include a class method to track accounts created and a static method for a bank policy message. Ensure the balance is non-negative.
class BankAccount:
    def __init__(self, balance: float, account_holder: str) -> None:
        self._balance = balance
        self._account_holder = account_holder

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if (self._balance < amount):
            print('amount to withdraw is too big.')
        else:
            self._balance -= amount

    @property
    def balance(self):
        return self._balance
