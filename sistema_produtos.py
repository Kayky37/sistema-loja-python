import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('loja.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()


def criar_produto(nome, preco, estoque):
    conexao = sqlite3.connect('loja.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO produtos (nome, preco, estoque)
        VALUES (?, ?, ?)
    ''', (nome, preco, estoque))

    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Produto {nome} adicionado com sucesso!")
    else:
        print(f"Erro ao adicionar o produto {nome}.")

    conexao.close()


def listar_produtos():
    conexao = sqlite3.connect('loja.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if produtos:
        for id, nome, preco, estoque in produtos:
            print(f"ID: {id}, Nome: {nome}, Preço: R${preco:.2f}, Estoque: {estoque}")
    else:
        print("Nenhum produto encontrado.")

    conexao.close()

def atualizar_estoque(id, novo_estoque):
    conexao = sqlite3.connect('loja.db')
    cursor = conexao.cursor()

    cursor.execute('''
        UPDATE produtos 
        SET estoque = ? 
        WHERE id = ?
    ''', (novo_estoque, id))

    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Estoque do produto com ID {id} atualizado para {novo_estoque}.")
    else:
        print(f"Produto com ID {id} não encontrado.")

    conexao.close()

def deletar_produto(id):
    conexao = sqlite3.connect('loja.db')
    cursor = conexao.cursor()

    cursor.execute('''
        DELETE FROM produtos 
        WHERE id = ?
    ''', (id,))

    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Produto com ID {id} deletado com sucesso.")
    else:
        print(f"Produto com ID {id} não encontrado.")

    conexao.close()

def buscar_produto_por_nome(nome):
    conexao = sqlite3.connect('loja.db')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT * FROM produtos 
        WHERE nome LIKE ?
    ''', (f'%{nome}%',))
    produtos = cursor.fetchall()

    if produtos:
        for id, nome, preco, estoque in produtos:
            print(f"ID: {id}, Nome: {nome}, Preço: R${preco:.2f}, Estoque: {estoque}")
    else:
        print(f"Nenhum produto encontrado com o nome '{nome}'.")

    conexao.close()

criar_tabela()

while True:
    print("\n===== MENU =====")
    print("1. Criar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Estoque")
    print("4. Deletar Produto")
    print("5. Buscar Produto por Nome")
    print("6. fazer backup do banco de dados")
    print("0. Sair")     

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        try:
            preco = float(input("Digite o preço do produto: "))
        except ValueError:
            print("Preço inválido. Por favor, insira um número.")
            continue
        estoque = int(input("Digite a quantidade em estoque: "))
        criar_produto(nome, preco, estoque)    
        # pedir nome, preco, estoque
        # chamar criar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        id = int(input("Digite o ID do produto: "))
        novo_estoque = int(input("Digite a nova quantidade em estoque: "))
        atualizar_estoque(id, novo_estoque)
    elif opcao == "4":
        id = int(input("Digite o ID do produto: "))
        deletar_produto(id)
    elif opcao == "5":
        nome = input("Digite o nome do produto para buscar: ")
        buscar_produto_por_nome(nome)
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")

