from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Empresa, Funcionario


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'Empresa', 'Fantasia', 'Responsavel', 'email']


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'Empresa', 'Nome', 'Cargo', 'CPF', 'email' ]