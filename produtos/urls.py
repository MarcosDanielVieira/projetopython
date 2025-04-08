from django.urls import path
from . import views

urlpatterns = [
  path('ver-produto/', views.ver_produto, name='ver_produto')
]