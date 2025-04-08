from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa


def ver_produto(request):
    return render(request, "ver.html", {"nome": "notebook", "preco": 5000.85})


def comprar_produto(request):
    nome = request.POST.get("nomeCompleto")
    idade = request.POST.get("idade")

    pessoa = Pessoa(nome=nome, idade=idade)

    pessoa.save()

    return HttpResponse("Dados cadastrados com sucesso!")
