# Controle de Tarefas

Este projeto consiste na refatoração inicial de um protótipo procedural de controle de tarefas para uma versão estruturada orientada a objetos (paradigma POO), preparando a base de código para futuras integrações com frameworks web.

## Como Executar o Programa

Certifique-se de ter o Python 3 instalado no seu ambiente de terminal local.

1. Abra o terminal na pasta raiz do projeto (`controle_tarefas/`).
2. Execute o seguinte comando:

```bash
python main.py
```

##  Organização e Responsabilidade dos Arquivos

O projeto foi modularizado para garantir a separação de conceitos e responsabilidades:

- `tarefa.py`: Contém a classe principal `Tarefa`, mapeando seus atributos (`titulo`, `descricao`, `prioridade`, `situacao`) e métodos comportamentais (`concluir` e `exibir_resumo`).
- `servicos.py`: Centraliza as funções lógicas e regras operacionais do sistema, como as rotinas de cadastro, listagem geral e filtros analíticos por situação.
- `main.py`: Funciona como o script orquestrador (ponto de entrada) encarregado de rodar a demonstração prática da aplicação.

## Funcionalidades Demonstradas

Ao executar o arquivo principal, a aplicação valida e executa o seguinte fluxo em memória:
1. Instanciação e cadastro automático de 3 tarefas com diferentes níveis de prioridade.
2. Modificação de estado interno de um objeto (mudança da situação de "Pendente" para "Concluída").
3. Listagem completa no terminal de todas as tarefas cadastradas.
4. Aplicação de filtro lógico para exibir isoladamente apenas os itens concluídos.
