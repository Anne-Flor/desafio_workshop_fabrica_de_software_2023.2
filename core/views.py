from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import CarroSerializer, ClienteSerializer
from .models import Carro

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer