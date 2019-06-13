from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome completo', blank=False, null=True)
    cidade = models.CharField(max_length=255, verbose_name='Cidade', blank=False, null=True)
    bairro = models.CharField(max_length=255, verbose_name='Bairro', blank=False, null=True)
    sexo = models.CharField(max_length=1, verbose_name='Sexo', choices=(('M','Masculino'),
                                                                        ('F', 'Feminino')))
    usuario = models.OneToOneField(User,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome if self.nome is not None else 'Sem nome'


class Emocao(models.Model):
    class Meta:
        unique_together = ('raiva', 'nojo', 'alegria', 'medo', 'tristeza', 'surpresa', 'neutro')
    raiva = models.FloatField(verbose_name='Raiva')
    nojo = models.FloatField(verbose_name='Nojo')
    alegria = models.FloatField(verbose_name='Alegria')
    medo = models.FloatField(verbose_name='Medo')
    tristeza = models.FloatField(verbose_name='Tristeza')
    surpresa = models.FloatField(verbose_name='Surpresa')
    neutro = models.FloatField(verbose_name='Neutro')


class Pagina(models.Model):
    titulo = models.CharField(max_length=128, verbose_name='Titulo', blank=False, null=True)


class Imagem(models.Model):
    arquivo = models.FileField()

    def __str__(self):
        return self.arquivo.instance.name