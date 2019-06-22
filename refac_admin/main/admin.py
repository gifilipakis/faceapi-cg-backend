from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Participante)
class PessoaAdmin(admin.ModelAdmin):
    pass


@admin.register(Arquivo)
class ArquivoAdmin(admin.ModelAdmin):
    pass


class ArquivoPaginaInline(admin.TabularInline):
    model = ArquivoPagina
    extra = 1

    def get_queryset(self, request):
        qs = Arquivo.objects.filter(id__in=ArquivoPagina.objects.filter(
            pagina__responsavel=request.user).values_list('id'))
        return qs


@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    inlines = (ArquivoPaginaInline,)
    exclude = ('responsavel',)

    def save_model(self, request, obj, form, change):
        obj.responsavel = request.user
        super().save_model(request, obj, form, change)


@admin.register(ArquivoPagina)
class ArquivoPaginaAdmin(admin.ModelAdmin):
    pass
