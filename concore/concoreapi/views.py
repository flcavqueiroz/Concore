from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from concoreapi.serializers import EmpresaSerializer, FuncionarioSerializer
from .models import Empresa, Funcionario

class EmpresaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer