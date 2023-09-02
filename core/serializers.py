from rest_framework import serializers
from .models import Cliente
from .models import Carro

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'idade', 'endereco']

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['id', 'dono', 'apelido', 'ano', 'modelo', 'placa', 'cor',]