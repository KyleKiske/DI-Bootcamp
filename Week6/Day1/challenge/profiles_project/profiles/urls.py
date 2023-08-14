from . import views
from django.urls import path

urlpatterns = [
    path('create_profile/', views.create_profile),
    path('delete_profile/<int:profile_id>/', views.delete_profile),
]