import sqlite3

def criar_contato(nome, email, telefone):
    conexao = sqlite3.connect('agenda.db')
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO contatos (nome, email, telefone) 
        VALUES (?, ?, ?)
    ''', (nome, email, telefone))

    conexao.commit()
    conexao.close()

    print(f"Contato {nome} adicionado com sucesso!")

criar_contato('kayky', 'kaykyfeio@gmail.com', '123456789')
criar_contato('João', 'joao@gmail.com', '154845178')
criar_contato('Maria', 'maria@gmail.com', '987654421')

def listar_contatos():
    conexao = sqlite3.connect('agenda.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()

    if contatos:
        for id, nome, email, telefone in contatos:
            print(f"ID: {id}, Nome: {nome}, Email: {email}, Telefone: {telefone}")
    else:   
        print("Nenhum contato encontrado.")

    conexao.commit()
    conexao.close()

def atualizar_telefone(id, novo_telefone):
    conexao = sqlite3.connect('agenda.db')
    cursor = conexao.cursor()

    cursor.execute('''
        UPDATE contatos 
        SET telefone = ? 
        WHERE id = ?
    ''', (novo_telefone, id))

    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Telefone do contato com ID {id} atualizado para {novo_telefone}.")
    else:
        print(f"Contato com ID {id} não encontrado.")

    conexao.close()


def deletar_contato(id):
    conexao = sqlite3.connect('agenda.db')
    cursor = conexao.cursor()

    cursor.execute('''
        DELETE FROM contatos
        WHERE id = ?
    ''', (id,))

    conexao.commit()
    if cursor.rowcount > 0:
        print(f"Contato com ID {id} deletado com sucesso.")
    else:
        print(f"Contato com ID {id} não encontrado.")

    conexao.close()