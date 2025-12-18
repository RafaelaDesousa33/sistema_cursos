from tabela_curso import conectar,criar_tabela

#=========
#CLASSE CURSO
#===========
class Cursos:
    def __init__(self,nome,descricao,duracao):
        self.__nome = nome
        self.__descricao = descricao
        self.__duracao = duracao

    #=============
    #INSERIR CURSO
    #===========
    def inserir_cursos(self):
        criar_tabela()
        conexao = conectar()

        cursor = conexao.cursor()
        cursor.execute(
            """
            INSERT INTO cursos_aluno (nome_curso,descricao_curso,duracao_curso)
            VALUES(?,?,?)
            """, (self.__nome, self.__descricao,self.__duracao)
        )
        conexao.commit()
        conexao.close()
        

    #==========
    #REMOVER CURSO
    #===========
    def remover_curso(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
           """
           DELETE FROM cursos_aluno WHERE nome_curso = ?
           """, (self.__nome,)
        )
        conexao.commit()
        conexao.close()


    #============
    #ATUALIZAR CURSO
    #=============
    def atualizarCurso(self,novaDescricao):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
           """
            UPDATE cursos_aluno SET descricao_curso = ? WHERE nome_curso = ?
           """,(novaDescricao,self.__nome)
        )
        conexao.commit()
        conexao.close()



    #================
    #LISTAR CURSO
    #===============
    @staticmethod
    def listarCursos():
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM cursos_aluno")
        dados = cursor.fetchall()
        conexao.close()
        return dados


  


    

