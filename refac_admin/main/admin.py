from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass

@admin.register(Imagem)
class ImagemAdmin(admin.ModelAdmin):
    pass


@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    pass


@admin.register(Emocao)
class EmocaoAdmin(admin.ModelAdmin):
    pass