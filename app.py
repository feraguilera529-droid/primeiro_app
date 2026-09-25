import streamlit as st

# Configuração da página (título da aba do navegador e layout)
st.set_page_config(page_title="Calculadora Vibe", page_icon="🧮", layout="centered")

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora Interativa")
st.caption("Desenvolvida com Python e Streamlit")

st.divider()

# Formulário de entradas para organizar visualmente
with st.container():
    # 2. Dois campos de entrada numérica
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Primeiro número", value=0.0, step=1.0, format="%.2f")

    with col2:
        num2 = st.number_input("Segundo número", value=0.0, step=1.0, format="%.2f")

    # 3. Componente de seleção da operação
    operacao = st.radio(
        "Escolha a operação desejada:",
        options=["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"],
        horizontal=True,
    )

    st.write("")  # Espaçamento simples

    # 4. Botão de ação
    if st.button("Calcular", type="primary", use_container_width=True):
        # 5. Lógica de cálculo executada ao clicar no botão
        if operacao == "Soma (+)":
            resultado = num1 + num2
            st.metric(label="Resultado da Soma", value=f"{resultado:.2f}")
            st.success("Cálculo realizado com sucesso!")

        elif operacao == "Subtração (-)":
            resultado = num1 - num2
            st.metric(label="Resultado da Subtração", value=f"{resultado:.2f}")
            st.success("Cálculo realizado com sucesso!")

        elif operacao == "Multiplicação (*)":
            resultado = num1 * num2
            st.metric(label="Resultado da Multiplicação", value=f"{resultado:.2f}")
            st.success("Cálculo realizado com sucesso!")

        elif operacao == "Divisão (/)":
            # Tratamento da divisão por zero
            if num2 == 0:
                st.error(
                    "⚠️ Operação inválida: Não é possível dividir um número por zero!"
                )
            else:
                resultado = num1 / num2
                st.metric(label="Resultado da Divisão", value=f"{resultado:.2f}")
                st.success("Cálculo realizado com sucesso!")