from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=50, blank=False)
    published_date = models.DateField(blank=False)
    description = models.TextField(blank=False)
    page_count = models.IntegerField()
    categories = models.CharField(max_length=50, blank=False)
    thumbnail_url = models.URLField()

    def clean(self):
        if self.page_count < 1:
            raise ValidationError('Page count should be a positive value')
        
    
    # category_set/categories (ManyToMany with Category

class BookReview(models.Model):
    linked_book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()

    def clean(self):
        if self.rating > 5 or self.rating < 1:
            raise ValidationError('Ratign should be between 1 and 5.')
        if len(self.review_text) < 10:
            raise ValidationError('Review text should be at least 10 characters long.')