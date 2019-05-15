from django.shortcuts import render
from .models import area
from rest_framework import viewsets
from .serializers import AreaSerializer

class lahanviewset(viewsets.ModelViewSet):
    queryset = area.objects.all()
    serializer_class = AreaSerializer

