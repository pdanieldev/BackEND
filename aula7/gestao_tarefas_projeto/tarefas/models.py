from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
    ]

    SITUACAO_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('CONCLUIDA', 'Concluída'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE_CHOICES, default='Média')
    data_prevista = models.DateField(blank=True, null=True)
    situacao = models.CharField(max_length=20, choices=SITUACAO_CHOICES, default='PENDENTE')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='tarefas')

    def __str__(self):
        return self.titulo
