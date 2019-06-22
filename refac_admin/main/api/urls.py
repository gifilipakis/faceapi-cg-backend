from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'pessoas', ViewPessoa)
router.register(r'paginas', ViewArquivo)
router.register(r'arquivos', ViewPagina)
router.register(r'pessoa-emocao', ViewEmocoesPessoa)


urlpatterns = [
    path('api/', include(router.urls)),
]
