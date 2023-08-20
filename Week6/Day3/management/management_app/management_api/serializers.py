from rest_framework import serializers
from .models import Department, Employee, Project, Task

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class DepartmentHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='{deparment}-detail')
    class Meta:
        model = Department
        fields = '__all__'
        
class EmployeeHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='{employee}-detail')
    class Meta:
        model = Employee
        fields = '__all__'
        
class TaskHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='{task}-detail')
    class Meta:
        model = Task
        fields = '__all__'