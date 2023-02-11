import streamlit as st

st.set_page_config(page_title="Restaurante & Bar do NEU", page_icon="🍗", layout="centered")

st.title("Restaurante & Bar do NEU 🍗")
st.markdown('### COMANDA')

products = {
    "Água": 2,
    "Água com gás": 3,
    "Almoço": 40,
    "Caçula": 3,
    "Cerveja": 10,
    "Cerveja lata": 5,
    "Coca 2 litros": 15,
    "Coca 600": 8,
    "Coca Ks": 5,
    "Coca lata": 5,
    "Cone": 4,
    "Guaraná 2 litros": 8,
    "Guaraná lata": 5,
    "Pinga copo": 5,
    "Pinga dose": 3,
    "Porção Peixe": 45,
    "Porção Torresmo": 30,
    "Pudim": 3,
    "Suco": 15,
}

total_amount = 0
product_list = []


for product, price in products.items():
    quantity = st.number_input(f"{product.upper()}:", value=0)
    total_amount += quantity * price
    if quantity > 0:
        product_list.append((product, quantity))

if st.button("Calcular Total"):
    st.write(f"**O total da conta é: R$ {total_amount:.2f}**")
    if product_list:
        st.write("Lista de Produtos Consumidos:")
        for product, quantity in product_list:
            st.write(f"- {product}: {quantity}")

    
