class CadastrarTarefas():
    def __init__(self):
        self.tarefas = []

    def cadastrar(self):
        print("\n--- Novo Cadastro ---")
        id_tarefa = input("Digite o ID: ")
        titulo = input("Título: ")
        prioridade = input("Prioridade (Baixa/Média/Alta): ").strip()
        situacao = input("Situação (Aberto/Em Andamento/Concluído): ").strip()
        categoria = input("Categoria (Estudos/Trabalho/Pessoal/etc): ").strip()

        nova_tarefa = {
            "id": id_tarefa,
            "titulo": titulo,
            "prioridade": prioridade,
            "situacao": situacao,
            "categoria": categoria
        }

        self.tarefas.append(nova_tarefa)
        print("Tarefa cadastrada com sucesso!")

    def listar(self):
        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada!")
            return
        
        print("\n=== Lista de Tarefas ===")
        for tarefa in self.tarefas:
            print(f"ID: {tarefa['id']} | Título: {tarefa['titulo']} | Prioridade: {tarefa['prioridade']} | Situação: {tarefa['situacao']} | Categoria: {tarefa['categoria']}")

    def filtrar_por_situacao(self):
        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada para filtrar!")
            return
        
        busca = input("Qual situação deseja buscar? (ex: Aberto, Em Andamento, Concluído): ").strip()

        if not encontradas:
            print(f"Nenhuma tarefa encontrada com a situação '{busca}'.")
        else:
            print(f"\n=== Tarefas com situação: {busca} ===")
            for tarefa in encontradas:
                print(f"ID: {tarefa['id']} | Título: {tarefa['titulo']} | Prioridade: {tarefa['prioridade']} | Categoria: {tarefa['categoria']}")

    def atualizar_situacao(self):
        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada para atualizar!")
            return

        id_busca = input("Digite o ID da tarefa que deseja atualizar: ")
        for tarefa in self.tarefas:
            if tarefa['id'] == id_busca:
                nova_situacao = input(f"Nova situação para a tarefa '{tarefa['titulo']}': ").strip()
                tarefa['situacao'] = nova_situacao
                print("Situação atualizada com sucesso!")
                return
        
        print("ID não encontrado!")

    def mostrar_categorias(self):
        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada!")
            return

        print("\n=== Resumo por Categoria ===")
        categorias = set(t['categoria'] for t in self.tarefas)
        for cat in categorias:
            qtd = sum(1 for t in self.tarefas if t['categoria'] == cat)
            print(f"- {cat}: {qtd} tarefa(s)")



sistema = CadastrarTarefas()

while True:
    print("\n========== MENU ==========")
    print("1. Cadastrar tarefa")
    print("2. Listar todas as tarefas")
    print("3. Filtrar por situação")
    print("4. Atualizar situação")
    print("5. Mostrar resumo por categoria")
    print("0. Encerrar")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        sistema.cadastrar()
    elif opcao == "2":
        sistema.listar()
    elif opcao == "3":
        sistema.filtrar_por_situacao()
    elif opcao == "4":
        sistema.atualizar_situacao()
    elif opcao == "5":
        sistema.mostrar_categorias()
    elif opcao == "0":
        print("\nPrograma encerrado. Até mais!")
        break
    else:
        print("Opção inválida! Tente novamente.")