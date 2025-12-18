from Cursos import Cursos
from Aluno import Aluno
import streamlit as st


st.set_page_config(page_title="Sistema de Cursos", layout="centered")

st.title("Sistema de Cursos")

# ================================
# INSERIR ALUNO
# ================================
st.header("Inserir aluno")

nome_aluno = st.text_input("Nome do aluno:", key="nome_aluno")
cpf_aluno = st.text_input("CPF (11 dígitos):", key="cpf_aluno")

if st.button("Inserir aluno", key="btn_inserir_aluno"):
    if nome_aluno and cpf_aluno:
        aluno = Aluno(nome_aluno, cpf_aluno)
        aluno.inserir_aluno()
        st.success("Aluno inserido com sucesso")
    else:
        st.error("Preencha todos os campos")


# ================================
# INSERIR CURSO
# ================================
st.header("Inserir curso")

nome_curso = st.text_input("Nome do curso:", key="nome_curso")
descricao_curso = st.text_input("Descrição do curso:", key="descricao_curso")
duracao_curso = st.number_input(
    "Duração (horas):",
    min_value=1,
    step=1,
    key="duracao_curso"
)

if st.button("Inserir curso", key="btn_inserir_curso"):
    if nome_curso and descricao_curso:
        curso = Cursos(nome_curso, descricao_curso, duracao_curso)
        curso.inserir_cursos()
        st.success("Curso inserido com sucesso")
    else:
        st.error("Preencha todos os campos")


# ================================
# REMOVER ALUNO
# ================================
st.header("Remover aluno")

cpf_remover = st.text_input("CPF do aluno:", key="cpf_remover")

if st.button("Remover aluno", key="btn_remover_aluno"):
    if cpf_remover:
        aluno = Aluno("", cpf_remover)
        aluno.removerAluno()
        st.success("Aluno removido com sucesso")
    else:
        st.error("Preencha o CPF")


# ================================
# REMOVER CURSO
# ================================
st.header("Remover curso")

nome_remover_curso = st.text_input("Nome do curso:", key="nome_remover_curso")

if st.button("Remover curso", key="btn_remover_curso"):
    if nome_remover_curso:
        curso = Cursos(nome_remover_curso, "", "")
        curso.remover_curso()
        st.success("Curso removido com sucesso")
    else:
        st.error("Preencha o nome do curso")


# ================================
# ATUALIZAR ALUNO
# ================================
st.header("Atualizar aluno")

cpf_update = st.text_input("CPF do aluno:", key="cpf_update")
novo_nome_aluno = st.text_input("Novo nome do aluno:", key="novo_nome_aluno")

if st.button("Atualizar aluno", key="btn_atualizar_aluno"):
    if cpf_update and novo_nome_aluno:
        aluno = Aluno("", cpf_update)
        aluno.atualizarAluno(novo_nome_aluno)
        st.success("Aluno atualizado com sucesso")
    else:
        st.error("Preencha todos os campos")


# ================================
# ATUALIZAR CURSO
# ================================
st.header("Atualizar curso")

nome_update_curso = st.text_input("Nome do curso:", key="nome_update_curso")
nova_descricao = st.text_input("Nova descrição do curso:", key="nova_descricao")

if st.button("Atualizar curso", key="btn_atualizar_curso"):
    if nome_update_curso and nova_descricao:
        curso = Cursos(nome_update_curso, "", "")
        curso.atualizarCurso(nova_descricao)
        st.success("Curso atualizado com sucesso")
    else:
        st.error("Preencha todos os campos")


#===========================
#LISTAR COMPONENTES
#======================

st.header("Listar componentes")

if st.button("Listar componentes", key="btn_listar_componentes"):
    dados_cursos = cursos = Cursos.listarCursos()
    dados_alunos = alunos = Aluno.listarAlunos()

    st.table(dados_cursos)
    st.table(dados_alunos)




#Key é o como o RG do componente. assim o Streamlit nao se confude