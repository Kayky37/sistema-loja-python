from database import (
    criar_tabela,
    criar_produto,
    listar_produtos,
    atualizar_estoque,
    deletar_produto,
    buscar_produto_por_nome,
    fazer_backup
)

criar_tabela()

while True:
    print("\n===== MENU =====")
    print("1. Criar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Estoque")
    print("4. Deletar Produto")
    print("5. Buscar Produto por Nome")
    print("6. Fazer Backup")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        try:
            preco = float(
                input("Preço: ")
                .replace('.', '')   # remove ponto de milhar
                .replace(',', '.')) # troca vírgula por ponto decimal
            estoque = int(
                input("Estoque: "))
        except ValueError:
            print("Valor inválido!")
            continue
        criar_produto(nome, preco, estoque)

    elif opcao == "2":
        listar_produtos()

    elif opcao == "3":
        try:
            id = int(input("ID do produto: "))
            novo_estoque = int(input("Novo estoque: "))
        except ValueError:
            print("Valor inválido!")
            continue
        atualizar_estoque(id, novo_estoque)

    elif opcao == "4":
        try:
            id = int(input("ID do produto: "))
        except ValueError:
            print("ID inválido!")
            continue
        deletar_produto(id)

    elif opcao == "5":
        nome = input("Nome para buscar: ")
        buscar_produto_por_nome(nome)
    elif opcao == "6":
        fazer_backup()

    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")