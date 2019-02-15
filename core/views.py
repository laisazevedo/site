from django.shortcuts import render
from core.forms import Cadastro


def home(request):
    return render(request,'Home.html')

class Formulario():
