from django.db import models

# Create your models here.

class Empresa(models.Model):
    Empresa = models.CharField(max_length=50)
    Fantasia = models.CharField(max_length=50)
    Responsavel = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.Empresa

class Funcionario(models.Model):
    Empresa = models.CharField(max_length=50)
    Nome = models.CharField(max_length=50)
    Cargo = models.CharField(max_length=20)
    CPF = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.Nome
