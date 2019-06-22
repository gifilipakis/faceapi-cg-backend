from rest_framework import viewsets
from .serializers import *


class ViewPessoa(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = PessoaSerializers


class ViewArquivo(viewsets.ModelViewSet):
    queryset = Arquivo.objects.all()
    serializer_class = ArquivoSerializers


class ViewPagina(viewsets.ModelViewSet):
    queryset = Pagina.objects.all()
    serializer_class = PaginaSerializers


class ViewEmocoesPessoa(viewsets.ModelViewSet):
    queryset = PessoaEmocao.objects.all()
    serializer_class = PessoaEmocaoSerializers
