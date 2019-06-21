from django.urls import include, path
from .api import urls as api_urls
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'refac_api'

urlpatterns = [
    path('', include(api_urls)),
    path('refac/<id_pagina>', views.pagina_refac_imagem),
    path('participante/refac/<id_pagina>', views.dados_participante, name='dados_participante'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
