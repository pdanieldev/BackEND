# Sistema Web de Gestão de Tarefas

Este repositório contém a entrega unificada das atividades Hands-on das **Semanas 06 e 07** da disciplina de Laboratório de Programação Back-End (Django).

---

## 📁 Estrutura de Pastas e Arquivos

```text
gestao_tarefas/
│
├── manage.py                   # Script principal do Django
├── README.md                   # Documentação do projeto
├── gestao_tarefas/             # Configurações globais do projeto
│   ├── __init__.py
│   ├── settings.py             # Configurações (INSTALLED_APPS, Banco de Dados, etc)
│   ├── urls.py                 # Rotas globais
│   ├── wsgi.py
│   └── asgi.py
│
└── tarefas/                    # Aplicação Django 'tarefas'
    ├── __init__.py
    ├── admin.py                # Registro dos models Categoria e Tarefa no Admin
    ├── apps.py
    ├── models.py               # Definição dos models Categoria e Tarefa
    ├── urls.py                 # Rotas da aplicação (/ e /tarefas/)
    ├── views.py                # Lógica das views (inicio e lista_tarefas com ORM)
    ├── migrations/
    │   └── __init__.py
    └── templates/
        └── tarefas/
            ├── inicio.html     # Página inicial com link para listagem
            └── lista.html      # Página de listagem dinâmica com ORM
```

---

## 🛠️ O que foi feito e como foi feito

### Semana 06: Interface Web Inicial
1. **Criação da Aplicação e Configuração de URLs:**
   - A aplicação `tarefas` foi criada e registrada em `INSTALLED_APPS` no `settings.py`.
   - Foram configuradas as rotas no arquivo `tarefas/urls.py` e incluídas no arquivo `gestao_tarefas/urls.py`:
     - `/`: chama a view `inicio`
     - `/tarefas/`: chama a view `lista_tarefas`
2. **Implementação de Views e Templates:**
   - A view `inicio` renderiza o template `inicio.html` com mensagem de boas-vindas e link para a lista.
   - A view `lista_tarefas` renderiza o template `lista.html` que itera sobre a lista de tarefas e exibe cada uma com condicional `{% if %}` para lista vazia.

### Semana 07: Persistência com Models, ORM e Admin
1. **Modelagem de Dados (`models.py`):**
   - **`Categoria`**: possui o campo `nome`.
   - **`Tarefa`**: possui os campos `titulo`, `descricao`, `prioridade`, `data_prevista`, `situacao` e o relacionamento `ForeignKey` com `Categoria`.
   - Métodos `__str__` implementados em ambos os models.
2. **Registro no Admin (`admin.py`):**
   - Os modelos `Categoria` e `Tarefa` foram registrados para permitir cadastro via Django Admin.
3. **Consulta ORM:**
   - A view `lista_tarefas` em `views.py` foi integrada ao banco utilizando `Tarefa.objects.all()`.

---

## 🚀 Como executar o projeto

1. **Criar e ativar o ambiente virtual (opcional, porém recomendado):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/macOS:
   source venv/bin/activate
   ```

2. **Instalar o Django:**
   ```bash
   pip install django
   ```

3. **Gerar e aplicar as migrações do banco de dados:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Criar um superusuário para acessar o Django Admin:**
   ```bash
   python manage.py createsuperuser
   ```

5. **Iniciar o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

6. **Testar no navegador:**
   - **Página inicial:** `http://127.0.0.1:8000/`
   - **Listagem de tarefas:** `http://127.0.0.1:8000/tarefas/`
   - **Painel Administrativo:** `http://127.0.0.1:8000/admin/`

---

## 📝 Registro do Commit

Exemplo de comando utilizado para versionamento Git:
```bash
git add .
git commit -m "Implementa interface web e persistência de tarefas e categorias com Django"
```

## ❓ Registro de Dificuldade Encontrada e Solução
- **Dificuldade:** Ao integrar os dados do ORM com os templates HTML, tarefas pendentes cadastradas no admin utilizavam códigos internos como `PENDENTE`.
- **Solução:** Utilizou-se o método auxiliar do Django `get_situacao_display` na template tag para exibir a versão legível para o usuário final, mantendo o código limpo e desacoplado.
