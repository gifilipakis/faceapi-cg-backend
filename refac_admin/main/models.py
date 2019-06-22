from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Participante(models.Model):

    nome = models.CharField(max_length=255, verbose_name='Nome completo', blank=False, null=True)
    cidade = models.CharField(max_length=255, verbose_name='Cidade', blank=False, null=True)
    bairro = models.CharField(max_length=255, verbose_name='Bairro', blank=False, null=True)
    sexo = models.CharField(max_length=1, verbose_name='Sexo', choices=(('M','Masculino'),
                                                                        ('F', 'Feminino')))
    idade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome if self.nome is not None else 'Sem nome'


class Pagina(models.Model):
    titulo = models.CharField(max_length=128, verbose_name='Titulo', blank=False, null=True)
    arquivos = models.ManyToManyField('Arquivo', through='ArquivoPagina', blank=True)
    video_url = models.CharField(max_length=600, verbose_name='URL Vídeo YouTube', null=True, blank=True)
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo


def diretorio_arquivos(instance, filename):
    return 'refac/arquivos/{}'.format(filename)


class Arquivo(models.Model):
    nome_arquivo = models.CharField(verbose_name='Nome do arquivo', max_length=64, blank=True, null=True)
    imagem = models.FileField('Arquivo', upload_to=diretorio_arquivos,
                                         null=True, blank=True)

    def __str__(self):
        return self.nome_arquivo


class ArquivoPagina(models.Model):
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)
    arquivo = models.ForeignKey(Arquivo, on_delete=models.CASCADE)

    def __str__(self):
        return self.arquivo.nome_arquivo + ' da Página ' + self.pagina.titulo


class PessoaEmocao(models.Model):

    pessoa = models.ForeignKey(Participante, on_delete=models.SET_NULL, null=True, blank=True)
    arquivo = models.ForeignKey(Arquivo, on_delete=models.SET_NULL, null=True, blank=True)
    pagina = models.ForeignKey(Pagina, on_delete=models.SET_NULL, null=True, blank=True)
    raiva = models.FloatField(verbose_name='Raiva')
    nojo = models.FloatField(verbose_name='Nojo')
    alegria = models.FloatField(verbose_name='Alegria')
    medo = models.FloatField(verbose_name='Medo')
    tristeza = models.FloatField(verbose_name='Tristeza')
    surpresa = models.FloatField(verbose_name='Surpresa')
    neutro = models.FloatField(verbose_name='Neutro')

    def __str__(self):
        return 'Emoções: {}, {}, {}, {}, {}, {}, {}.'.format(
            str(self.raiva), str(self.nojo), str(self.alegria),
            str(self.medo), str(self.tristeza), str(self.surpresa), str(self.neutro)
        )
