from django.shortcuts import render
from .models import Tarefa

def inicio(request):
    return render(request, "tarefas/inicio.html")

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, "tarefas/lista.html", {"tarefas": tarefas})
