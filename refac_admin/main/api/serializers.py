from rest_framework import serializers
from ..models import Participante, Emocao, Arquivo, Pagina


class PessoaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Participante
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
