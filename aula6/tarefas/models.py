from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    prioridade = models.CharField(max_length=10, choices=Prioridade.choices)
    situacao = models.CharField(max_length=10, choices=Situacao.choices)


class Prioridade(models.TextChoices):
    BAIXA = "BAIXA", "Baixa"
    MEDIA = "MEDIA", "Média"
    ALTA = "ALTA", "Alta"


class Situacao(models.TextChoices):
    PENDENTE = "PENDENTE", "Pendente"
    CONCLUIDA = "CONCLUIDA", "Concluída"


titulo = models.CharField(max_length=150)
descricao = models.TextField(blank=True)
prioridade = models.CharField(
    max_length=10,
    choices=Prioridade.choices,
    default=Prioridade.MEDIA,
)
data_prevista = models.DateField()
situacao = models.CharField(
    max_length=10,
    choices=Situacao.choices,
    default=Situacao.PENDENTE,
)
categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)


def __str__(self):
    return self.titulo
