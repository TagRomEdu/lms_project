from django.shortcuts import render
from rest_framework import viewsets

from education_app.models import Course
from education_app.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

