from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views.generic import FormView
from main.forms import ParticipanteForm
from .models import Pagina, Participante


def pagina_refac_imagem(request, id_pagina, id_pessoa):
    imagens = Pagina.objects.get(id=id_pagina).arquivos.all()
    imagem_ativa = imagens[0].imagem.url
    context = {'imagens': imagens[1:], 'img_ativa': imagem_ativa, 'pagina': id_pagina, 'pessoa': id_pessoa}
    return render(request, template_name='main/index.html', context=context)


def dados_participante(request, id_pagina):

    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            idade = form.cleaned_data['idade']
            sexo = form.cleaned_data['sexo']
            bairro = form.cleaned_data['bairro']
            cidade = form.cleaned_data['cidade']
            pessoa = Participante(
                nome=nome,
                idade=idade,
                sexo=sexo,
                bairro=bairro,
                cidade=cidade
            )
            pessoa.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/refac/'+id_pagina+'/'+str(pessoa.id))

    else:
        form = ParticipanteForm()
    pagina = Pagina.objects.get(id=id_pagina)
    return render(request, 'main/cadastro_pessoa.html', {'form': form, 'pagina': id_pagina, 'titulo': pagina.titulo})
