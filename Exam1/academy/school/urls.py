from django.urls import path
from .views import CourseDetail, TeacherAPIView, FacilityAPIView, LaboratoryAPIView

urlpatterns = [
    path('course/', CourseDetail.as_view(), name='course'),
    path('course/<int:pk>/', CourseDetail.as_view(), name='course'),
    path('teacher/', TeacherAPIView.as_view(), name='teacher'),
    path('facility/', FacilityAPIView.as_view(), name='facility'),
    path('laboratory/', LaboratoryAPIView.as_view(), name='laboratory'),
]