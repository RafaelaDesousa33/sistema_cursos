import sqlite3

#=========
#CONEXAO
#=========
def conectar():
    conexao = sqlite3.connect("curso.db")
  
    return conexao

#==========
#CRIACAO DE TABELAS
#=============
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
       """
       CREATE TABLE IF NOT EXISTS cursos_aluno(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome_curso TEXT NOT NULL UNIQUE,
       descricao_curso TEXT NOT NULL,
       duracao_curso INTEGER NOT NULL
       )
       """

    )
    conexao.commit()
   

    cursor.execute(
       """
       CREATE TABLE IF NOT EXISTS aluno(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nome_aluno TEXT NOT NULL,
       cpf_aluno TEXT NOT NULL UNIQUE
       )
       """
    )
    
    conexao.commit()
    conexao.close()

