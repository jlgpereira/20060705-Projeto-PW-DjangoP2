import time

from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.urls import reverse

import base64
from io import BytesIO
from matplotlib import pyplot as plt

from website.forms import ContatoForm, ComentarioForm, QuizForm
from website.models import Contato, Comentario, Aula


def login_page_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('website:contatos'))
        else:
            return render(request, 'website/login.html', {
                'message': 'Credenciais inválidas.'
            })

    context = {
        'titulo_pagina': 'Login'
    }

    return render(request, 'website/login.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'website/login.html', {
        'message': 'Sessão terminada'})


def index_page_view(request):
    context = {
        'titulo_pagina': 'Home'
    }
    return render(request, 'website/index.html', context)


def pesquisa_view_page(request):
    context = {
        'titulo_pagina': 'Pesquisa Músicas'
    }
    return render(request, 'website/pesquisa.html', context)


def introducao_page_view(request):
    context = {
        'titulo_pagina': 'Introdução'
    }
    return render(request, 'website/introducao.html', context)


def nprinc_page_view(request):
    context = {
        'titulo_pagina': 'Noções Principais'
    }
    return render(request, 'website/nprinc.html', context)


def exercicios_page_view(request):
    context = {
        'titulo_pagina': 'Exercícios Preparatórios'
    }
    return render(request, 'website/exercicios.html', context)


def aboutus_page_view(request):
    context = {
        'titulo_pagina': 'About US'
    }
    return render(request, 'website/aboutus.html', context)


def contatos_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('website:login'))

    context = {
        'titulo_pagina': 'Contatos',
        'contatos': sorted(Contato.objects.all(), key=lambda objeto: objeto.criado, reverse=True)
    }

    return render(request, 'website/contatos.html', context)


def inserir_contato_page_view(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:inserir_contato'))

    context = {
        'titulo_pagina': 'Inserir Contato',
        'form': form
    }

    return render(request, 'website/inserir_contato.html', context)


def editar_contato_page_view(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    form = ContatoForm(request.POST or None, instance=contato)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:contatos'))

    context = {
        'titulo_pagina': 'Formulário de Contato',
        'form': form,
        'contato_id': contato_id
    }

    return render(request, 'website/editar_contato.html', context)


def apagar_contato_view(request, contato_id):
    Contato.objects.get(id=contato_id).delete()
    return HttpResponseRedirect(reverse('website:contatos'))


def comentarios_page_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:comentarios'))

    context = {
        'titulo_pagina': 'Comentários',
        'form': form
    }
    return render(request, 'website/comentarios.html', context)


def relatorios_page_view(request):
    plt.style.use('fivethirtyeight')
    print(Comentario.objects.values_list('r1', flat=True))
    dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
    dev_y = [38496, 42000, 46752, 49320, 53200,
             56000, 62316, 64928, 67317, 68748, 73752]
    plt.bar(dev_x, dev_y)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    grafico = base64.b64encode(image_png)
    grafico = grafico.decode('utf-8')

    context = {
        'titulo_pagina': 'Relatórios',
        'grafico': grafico
    }
    return render(request, 'website/relatorios.html', context)


def quiz_page_view(request):
    form = QuizForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:quiz'))

    context = {
        'titulo_pagina': 'Quiz',
        'form': form
    }
    return render(request, 'website/quiz.html', context)


def aulas_page_view(request):
    context = {
        'titulo_pagina': 'Aulas',
        'aulas': Aula.objects.all()
    }
    return render(request, 'website/aulas.html', context)


def aulas_section_view(request, num):
    if num == 1:
        aulas = Aula.objects.all()
        conteudo_json = serializers.serialize('python', aulas)
        return JsonResponse({"conteudo": conteudo_json})
    elif num == 2:
        alunos = Contato.objects.exclude(aulas__isnull=True)
        conteudo_json = serializers.serialize('python', alunos)
        return JsonResponse({"conteudo": conteudo_json})
    else:
        raise Http404("No such section")


def aula_page_view(request, aula_id):
    aula = Aula.objects.get(pk=aula_id)

    context = {
        'titulo_pagina': 'Aulas',
        'aula': aula,
        'contatos': aula.Contatos.all(),
        'nao_contatos': Contato.objects.exclude(aulas=aula),
    }
    return render(request, 'website/aula.html', context)


def adicionar_aluno_view(request, aula_id):
    if request.method == 'POST':
        aula = Aula.objects.get(pk=aula_id)
        contato = Contato.objects.get(pk=int(request.POST["contato"]))
        contato.aulas.add(aula)

        return HttpResponseRedirect(reverse('website:aula', args=(aula.id,)))


def remover_aluno_view(request, aula_id, contato_id):
    aula = Aula.objects.get(id=aula_id)
    aula.Contatos.remove(contato_id)

    return HttpResponseRedirect(reverse('website:aula', args=(aula_id,)))
