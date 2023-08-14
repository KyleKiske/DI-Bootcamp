from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    content = []
    for book in books:
        content.append( {"title": book.title,
               'author': book.author,
               'published date': book.published_date
               })
    return JsonResponse(content, safe=False)

def book_detail(request,book_id):
    book = Book.objects.get(id=book_id)
    content = {"title": book.title,
               'author': book.author,
               'published date': book.published_date
               }
    return JsonResponse(content)

def create_book(request):
    pass