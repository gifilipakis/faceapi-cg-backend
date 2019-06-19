from rest_framework import serializers
from ..models import Pessoa, Emocao, Arquivo, Pagina


class PessoaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class PaginaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pagina
        fields = '__all__'


class EmocaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Emocao
        fields = '__all__'


class ArquivoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Arquivo
        fields = '__all__'
