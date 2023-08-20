from django.shortcuts import render
from .models import Course, Teacher, Facility, Laboratory
from rest_framework import generics
from .serializers import CourseSerializer, TeacherSerializer, FacilitySerializer, LaboratorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self,request, pk=None):
        if pk is not None:
            course = Course.objects.get(id=pk)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherAPIView(APIView):
    def get(self,request):
        queryset = Teacher.objects.all()
        serializer = TeacherSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FacilityAPIView(APIView):
    def get(self,request):
        queryset = Facility.objects.all()
        serializer = FacilitySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FacilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LaboratoryAPIView(APIView):
    def get(self,request):
        queryset = Laboratory.objects.all()
        serializer = LaboratorySerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LaboratorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        