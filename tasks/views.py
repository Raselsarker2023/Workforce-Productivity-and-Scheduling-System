from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.filters import SearchFilter


# Create your views here.

class TaskModelViewset(viewsets.ModelViewSet):
    queryset = models.TaskModel.objects.all()
    serializer_class = serializers.TaskModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'priority', 'status', 'Cancel_reason']
    
    
   