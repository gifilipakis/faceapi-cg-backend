from rest_framework import viewsets
from .serializers import *


class ViewPessoa(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializers


class ViewArquivo(viewsets.ModelViewSet):
    queryset = Arquivo.objects.all()
    serializer_class = ArquivoSerializers


class ViewPagina(viewsets.ModelViewSet):
    queryset = Pagina.objects.all()
    serializer_class = PaginaSerializers


class ViewEmocao(viewsets.ModelViewSet):
    queryset = Emocao.objects.all()
    serializer_class = EmocaoSerializers
