from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50, blank=False, unique=True )
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

class Carro(models.Model):
    dono = models.ForeignKey(Cliente, on_delete=models.PROTECT, blank=False)
    apelido = models.CharField(max_length=50)
    ano = models.IntegerField()
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    cor = models.CharField(max_length=10)

    def __str__(self):
        return " ".join(self.placa, self.modelo, self.apelido, self.ano, self.cor) 