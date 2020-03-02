from django.db import models

# Create your models here.

class Empresa(models.Model):
    Social = models.CharField(max_length=50)
    Fantasia = models.CharField(max_length=50)
    Responsável = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.Social

class Funcionario(models.Model):
    Empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=50)
    Cargo = models.CharField(max_length=20)
    CPF = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.Empresa
