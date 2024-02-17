
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.filters import SearchFilter

# Create your views here.

class ScheduleModelViewset(viewsets.ModelViewSet):
    queryset = models.ScheduleModel.objects.all()
    serializer_class = serializers.ScheduleModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'status', 'cancel_reason']
 
 
