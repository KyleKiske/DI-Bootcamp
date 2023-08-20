from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50, unique=True)

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)

class Facility(models.Model):
    facility_name = models.CharField(max_length=50)
    usage_purpose = models.TextField()

class Laboratory(Facility):
    equipment_list = models.TextField()