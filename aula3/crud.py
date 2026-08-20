lista_tarefa = {}


def cadastrar():
    titulo = input("Insira o titulo da tarefa: ")
    prioridade = input("Insira a prioridade da tarefa(1 a 3): ")

    lista_tarefa[titulo] = prioridade
    print(f"Tarefa '{titulo}' cadastrada com sucesso!!")


def listar():
    if not lista_tarefa:
        print("Sem tarefas cadastradas.")
        return

    print("\n=== Lista de Tarefas ===")
    for titulo, prioridade in lista_tarefa.items():
        print(f"- {titulo} (Prioridade: {prioridade})")


def atualizar():
    if not lista_tarefa:
        print("Sem tarefas para atualizar.")
        return

    titulo = input("Digite o titulo da tarefa que deseja atualizar: ")

    if titulo in lista_tarefa:
        nova_prioridade = input("Insira a nova prioridade (1 a 3): ")
        lista_tarefa[titulo] = nova_prioridade
        print(f"Tarefa '{titulo}' atualizada com sucesso!!")
    else:
        print("Tarefa não encontrada.")


def encerrar():
    print("Encerrando programa...")
    exit()


while True:
    print("\n======== Menu =========")
    print("1 - Cadastrar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Atualizar Tarefa")
    print("4 - Encerrar sistema")

    try:
        opcao = int(input("Selecione uma das opções: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        atualizar()
    elif opcao == 4:
        encerrar()
    else:
        print("Opção inválida! Tente novamente.")