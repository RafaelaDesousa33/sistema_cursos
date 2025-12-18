from Aluno import Aluno
from Cursos import Cursos
from tabela_curso import conectar,criar_tabela

#===============
#METODO DE ESCOLHAS
#================
def escolha():
    criar_tabela()

    while True:
        print("----Escolhas----")

        print("1-adicionar aluno")
        print("2-adicionar curso")
        print("3-remover aluno")
        print("4-remover curso")
        print("5-atualizar curso")
        print("6-atualizar aluno")
        print("7-listar alunos")
        print("8-listar cursos")
        print("0-sair")

        escolha = input("Digite sua escolha:")

        if escolha == "1" :
            adicionarAluno()
        
        elif escolha == "2" :
            adicionarCurso()

        elif escolha == "3" :
            removerAluno()
        
        elif escolha == "4":
            removerCurso()

        elif escolha == "5" :
            atualizarCurso()

        elif escolha == "6" :
            atualizarAluno()

        elif escolha == "7" :
            listarAlunos()

        elif escolha == "8":
            listarCursos()
        
        elif escolha == "0":
            print("Obrigado!")
            break
        else:
            print("Erro:digite uma escolha valida.")


#================
#ADICIONAR ALUNO
#==============
def adicionarAluno():
     nome_aluno = input("Digite o nome do aluno:")
     cpf_aluno = input("Digite cpf do aluno:")

     novoAluno = Aluno(nome_aluno,cpf_aluno)
     novoAluno.inserir_aluno()
     print("Aluno adicionado com sucesso")
            

#=================
#ADICIONAR CURSO
#==============
def adicionarCurso():
     nome_curso = input("Digite o nome do curso:")
     descricao_curso = input("Digite a descricao do curso:")
     duracao_curso = int(input("Digite a duracao do curso:"))
           
     novo_curso = Cursos(nome_curso,descricao_curso,duracao_curso)
     novo_curso.inserir_cursos()
     print("Curso adicionado com sucesso")

        
#==================
#REMOVER ALUNO
#============
def removerAluno():
     cpf_aluno = input("Digite o cpf do aluno que deseja remover:")
     aluno = Aluno("",cpf_aluno)
     aluno.removerAluno()
     print("Aluno removido com sucesso")


#================
#ATUALIZAR ALUNO
#=============
def atualizarAluno():
    cpf_aluno = input("Digite o cpf do aluno que deseja atualizar:")
    novo_nome_aluno = input("Digite o novo nome que deseja colocar:")
    aluno = Aluno("",cpf_aluno)
    aluno.atualizarAluno(novo_nome_aluno)
    print("Aluno atualizado com sucesso")


#================
#REMOVER CURSO
#=============
def removerCurso():
     nome_curso = input("Digite o nome do curso que deseja remover:")
     curso = Cursos(nome_curso,"","")
     curso.remover_curso()

     print("Curso removido com sucesso!")

#=============
#ATUALIZAR CURSO
#=============
def atualizarCurso():
    nome_curso = input("Digite o nome do curso que deseja atualizar:")
    nova_descricao = input("Digite a nova descricao:")

    curso = Cursos(nome_curso,nova_descricao,"")
    curso.atualizarCurso(nova_descricao)
    print("Curso atualizado com sucesso")

#============
#LISTAR CURSO
#=============
def listarCursos():
   cursos = Cursos.listarCursos()
   for curso in cursos:
       print(curso)

#============
#LISTAR ALUNO
#==============
def listarAlunos():
    alunos = Aluno.listarAlunos()
    for aluno in alunos:
        print(aluno)




escolha()





       






