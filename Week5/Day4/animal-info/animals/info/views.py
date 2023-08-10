from django.shortcuts import render
from . import data
from django.http import HttpResponse


def display_all_animals(request):
    return HttpResponse(data.animals)

def display_all_families(request):
    return HttpResponse(data.families)

def display_one_animal(request, animal_id):
    response = None
    for animal in data.animals:
        if animal['id'] == animal_id:
            response = animal
            break
    result = str(response)
    return HttpResponse(result)

def display_animal_per_family(request, family_id):
    results = []
    for animal in data.animals:
        if animal['family'] == family_id:
            results.append(animal)
    return HttpResponse(results)
    