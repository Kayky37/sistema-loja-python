import sqlite3
import shutil # Serve para copiar arquivos
import os     # Serve para verificar se o arquivo existe
from datetime import datetime

def conectar():
    return sqlite3.connect('loja.db')

def criar_tabela():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL,
                estoque INTEGER NOT NULL
            )
        ''')

def criar_produto(nome, preco, estoque):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (?, ?, ?)
        ''', (nome, preco, estoque))
        if cursor.rowcount > 0:
            print(f"Produto '{nome}' adicionado com sucesso!")
        else:
            print(f"Erro ao adicionar o produto '{nome}'.")

def listar_produtos():
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()
        if produtos:
            for id, nome, preco, estoque in produtos:
                print(f"ID: {id} | Nome: {nome} | Preço: R${preco:.2f} | Estoque: {estoque}")
        else:
            print("Nenhum produto encontrado.")

def atualizar_estoque(id, novo_estoque):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE produtos SET estoque = ? WHERE id = ?
        ''', (novo_estoque, id))
        if cursor.rowcount > 0:
            print(f"Estoque do ID {id} atualizado para {novo_estoque}.")
        else:
            print(f"Produto com ID {id} não encontrado.")

def deletar_produto(id):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM produtos WHERE id = ?', (id,))
        if cursor.rowcount > 0:
            print(f"Produto com ID {id} deletado com sucesso.")
        else:
            print(f"Produto com ID {id} não encontrado.")

def buscar_produto_por_nome(nome):
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            SELECT * FROM produtos WHERE nome LIKE ?
        ''', (f'%{nome}%',))
        produtos = cursor.fetchall()
        if produtos:
            for id, nome, preco, estoque in produtos:
                print(f"ID: {id} | Nome: {nome} | Preço: R${preco:.2f} | Estoque: {estoque}")
        else:
            print(f"Nenhum produto encontrado com '{nome}'.")


def fazer_backup():
    try:
        if os.path.exists('loja.db'):
            # Gera uma data/hora atual formatada: 20231027_143005
            data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            nome_backup = f"loja_backup_{data_hora}.db"
            
            shutil.copy2('loja.db', nome_backup)
            print(f"Backup realizado: {nome_backup}")
        else:
            print("Banco de dados não encontrado.")
    except Exception as e:
        print(f"Erro no backup: {e}")