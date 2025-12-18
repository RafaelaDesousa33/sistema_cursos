"""
Alunos, cursos, módulos, matrículas e progresso. O banco deixa de ser apenas cadastro e passa a contar histórias: quem está aprendendo o quê, quando começou, onde parou.

"""
from tabela_curso import conectar,criar_tabela

#==========
#CLASSE ALUNO
#==========
class Aluno:
    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf
       
    #===========
    #INSERIR ALUNO
    #===========
    def inserir_aluno(self):
        criar_tabela()
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
           """
           INSERT INTO aluno (nome_aluno,cpf_aluno)
           VALUES (?,?)
           """, (self.__nome,self.__cpf)
        )

        conexao.commit()
        conexao.close()

    
    #==============
    #REMOVER ALUNO
    #===========
    def removerAluno(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
           DELETE FROM aluno WHERE cpf_aluno  = ?
            """, (self.__cpf,)
        )
        conexao.commit()
        conexao.close()

    #====================
    #ATUALIZAR ALUNO
    #===============
    def atualizarAluno(self,novo_nome):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
           UPDATE aluno SET nome_aluno = ? WHERE cpf_aluno = ?
            """,
            (novo_nome,self.__cpf)
        )
        conexao.commit()
        conexao.close()

    #============
    #LISTAR ALUNO
    #============
    @staticmethod
    def listarAlunos():
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM aluno")
        dados = cursor.fetchall()
        conexao.close()
        return dados
    
    
    
        
