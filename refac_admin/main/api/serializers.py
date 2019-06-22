from rest_framework import serializers
from ..models import Participante, Arquivo, Pagina, PessoaEmocao


class PessoaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'


class PaginaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pagina
        fields = '__all__'


class ArquivoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Arquivo
        fields = '__all__'


class PessoaEmocaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PessoaEmocao
        fields = '__all__'