from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass


@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    pass


class ArquivoPaginaInline(admin.TabularInline):
    model = ArquivoPagina
    extra = 1


@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    inlines = (ArquivoPaginaInline,)


@admin.register(Emocao)
class EmocaoAdmin(admin.ModelAdmin):
    pass


@admin.register(ArquivoPagina)
class ArquivoPaginaAdmin(admin.ModelAdmin):
    pass
