from django.shortcuts import render
from django.http import HttpResponse

def ver_produto(request):
  return render(request,'ver.html',{'nome': 'notebook', 'preco': 5000.85})
