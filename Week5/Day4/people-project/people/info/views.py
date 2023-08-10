from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

name = 'Bob Smith'
age = 35
country = 'USA'

people = ['bob','martha', 'fabio', 'john']

all_people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def display_person(request):
    return HttpResponse(f'name: {name}, age: {age}, country: {country}')

def display_people(request):
    temp = sorted(people)
    # temp = [x.capitalize() for x in temp]
    result = ""
    for x in temp:
        x = x.capitalize()
        result += x + ", "
    result = result[:-2]
    return HttpResponse(result)

def display_all_people(request):
    return HttpResponse(all_people)