import streamlit as st
from crud import inserir_aluno, listar_alunos, atualizar_idade, deletar_aluno
# python -m pip install streamlit

#Rodar o stremlit
# python -m streamlit run app.py

st.set_page_config(page_title="Gerenciamento de alunos", page_icon="🕵️‍♀️")

st.title("Sistema de alunos MySQL")

menu = st.sidebar.radio("Menu",  ["Adicionar aluno", "Listar alunos", "Atualizar idade",
"Deletar aluno"])

if menu == "Adicionar aluno":
    st.subheader("➕ Inserir aluno")
    nome = st.text_input("Nome", placeholder="Digite seu nome")
    idade = st.number_input("Idade", min_value=8, step=1)
    if st.button("Cadastrar"):
        if nome.strip() != "":
            inserir_aluno(nome, idade)
            st.success(f"Aluno {nome} cadastrado com sucesso!")
        else:
            st.warning("O campo nome não pode ser vazio.")

elif menu == "Listar alunos":
    st.subheader("Lista de alunos cadastrado.")
    alunos = listar_alunos()
    if alunos:
        st.dataframe(alunos)
    else:
        st.info("Nenhum aluno cadastrado.")

elif menu == "Atualizar idade":
    st.subheader("Atualizar idade")
    alunos = listar_alunos()
    if alunos:
        id_aluno = st.selectbox("Escolha o id do aluno", [linha[0] for linha in alunos])
        nova_idade = st.number_input("Nova idade", min_value=8, step=1)
        if st.button("Salvar"):
            atualizar_idade(id_aluno, nova_idade)
            st.success("Idade do aluno atualizada com sucesso!")

    else:
        st.info("NEnhum aluno disponivel para atualizar.")

elif menu == "deletar_aluno":
    st.subheader("deletar_aluno")