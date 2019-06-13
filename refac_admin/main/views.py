from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *



class ViewPessoa(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializers

