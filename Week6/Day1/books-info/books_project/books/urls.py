from django.urls import path
from .views import list_books, book_detail

urlpatterns = [
    path('books/', list_books, name='all books'),
    path('book/<int:book_id>/', book_detail, name='specific book'), # str, int
]