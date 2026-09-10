from django.shortcuts import render


def inicio(request):
    return render(request, "tarefas/inicio.html")


def lista_tarefas(request):
    tarefas = [
        {
            "titulo": "Estudar URLs no Django",
            "prioridade": "Alta",
            "situacao": "Pendente",
        },
        {
            "titulo": "Criar template de listagem",
            "prioridade": "Média",
            "situacao": "Concluída",
        },
    ]
    return render(request, "tarefas/lista.html", {"tarefas": tarefas})
