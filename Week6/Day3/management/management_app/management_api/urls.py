from django.urls import path
from .views import DepartmentAPIView, ProjectAPIView, EmployeeAPIView, TaskAPIView

urlpatterns = [
    path('dept/', DepartmentAPIView.as_view(), name='department'),
    path('dept/<int:pk>/', DepartmentAPIView.as_view(), name='department'),
    path('empl/', EmployeeAPIView.as_view(), name='employee'),
    path('empl/<int:pk>/', EmployeeAPIView.as_view(), name='employee'),
    path('proj/', ProjectAPIView.as_view(), name='project'),
    path('proj/<int:pk>/', ProjectAPIView.as_view(), name='project'),
    path('task/', TaskAPIView.as_view(), name='task'),
    path('task/<int:pk>/', TaskAPIView.as_view(), name='task'),
]