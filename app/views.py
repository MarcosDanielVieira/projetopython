from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def mysite(request):
    return render(request, "index.html")

@login_required
def home(request):
    return HttpResponse(f"Usuário logado: {request.user}")