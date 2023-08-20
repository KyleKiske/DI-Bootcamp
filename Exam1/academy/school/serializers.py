from rest_framework import serializers
from .models import Course, Teacher, Facility, Laboratory

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
       model = Course
       fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
       model = Teacher
       fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'