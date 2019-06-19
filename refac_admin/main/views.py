from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .models import Pagina


def pagina_refac_imagem(request, id_pagina):
    imagens = Pagina.objects.get(id=id_pagina).arquivos.all()
    context = {'imagens': imagens}
    return render(request, template_name='main/index.html', context=context)
