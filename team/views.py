from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.filters import SearchFilter

# Create your views here.

class TeamModelViewset(viewsets.ModelViewSet):
    queryset = models.TeamModel.objects.all()
    serializer_class = serializers.TeamModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'description']

