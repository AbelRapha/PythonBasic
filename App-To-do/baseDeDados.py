import sqlite3 as lite
from sqlite3.dbapi2 import Cursor

#Criando o banco de dados
conexao = lite.connect("Lista de Tarefas.db")
#Funcao para criar tabela
def criarTabela():
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")


def inserir(i):
    with conexao:
        cursor = conexao.cursor()
        query = " INSERT INTO tarefa(nome) VALUES(?)"
        cursor.execute(query,i) 

def selecionar():
    lista_de_tarefas = []
    with conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM tarefa")
        row = cursor.fetchall()
        for query in row:
            lista_de_tarefas.append(query)
    return lista_de_tarefas

def deletar(i):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM tarefa WHERE id=?"
        cursor.execute(query, i)


def renomear(i):
    with conexao:
        cursor = conexao.cursor()
        query = "UPDATE tarefa SET nome = 'Comer' WHERE id=?"
        cursor.execute(query,i)

   
