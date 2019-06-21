from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views.generic import FormView

from main.forms import ParticipanteForm
from .models import Pagina, Participante


def pagina_refac_imagem(request, id_pagina):
    imagens = Pagina.objects.get(id=id_pagina).arquivos.all()
    imagem_ativa = imagens[0].imagem.url
    context = {'imagens': imagens[1:], 'img_ativa': imagem_ativa}
    return render(request, template_name='main/index.html', context=context)


def dados_participante(request, id_pagina):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ParticipanteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            nome = form.cleaned_data['nome']
            idade = form.cleaned_data['nome']
            nome = form.cleaned_data['nome']
            # redirect to a new URL:
            return HttpResponseRedirect('/refac/'+id_pagina)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ParticipanteForm()
    pagina = Pagina.objects.get(id=id_pagina)
    return render(request, 'main/cadastro_pessoa.html', {'form': form, 'pagina': id_pagina, 'titulo': pagina.titulo})
