from django import forms
from .models import Participante


class ParticipanteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        required_fields = ['nome', 'cidade', 'bairro', 'sexo', 'idade']

        for field in required_fields:
            self.fields[field].widget.attrs['required'] = True

    class Meta:
        model = Participante
        fields = '__all__'
        labels = {
            'nome': 'Nome Completo',
            'cidade': 'Cidade',
            'bairro': 'Bairro',
            'sexo': 'Sexo'
        }
