from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict 

# Create your views here.
FIELDS = {'title', 'author', 'published_date'}

def list_books(request):
    books = Book.objects.all()
    book_result = [model_to_dict(instance=Book, fields=FIELDS) for Book in books]
    return JsonResponse(book_result, safe=False)

def book_detail(request,book_id):
    book = Book.objects.get(id=book_id)
    content = {"title": book.title,
               'author': book.author,
               'published date': book.published_date,
               'description' : book.description
               }
    return JsonResponse(content, safe=False)

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published date')
        description = request.POST.get('description')
        page_count = request.POST.get('page count')
        categories = request.POST.get('categories')
        book = Book.objects.create(title=title, author=author, published_date=published_date, description = description, 
                                   page_count=page_count, categories=categories)
        return JsonResponse({'201': f'Book {book.title} by author {book.author} created.'})
