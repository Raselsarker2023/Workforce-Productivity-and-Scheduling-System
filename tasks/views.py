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
    
    
class ManagerViewset(viewsets.ModelViewSet):
    queryset = models.Manager.objects.all()
    serializer_class = serializers.ManagerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'email', 'phone_no']
    
    
    
class RoleViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    
    
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'email', 'phone_no']
    
    
class EmployeeAssignViewset(viewsets.ModelViewSet):
    queryset = models.EmployeeAssign.objects.all()
    serializer_class = serializers.EmployeeAssignSerializer
    filter_backends = [SearchFilter]
    search_fields = ['assigned_date']
    
   