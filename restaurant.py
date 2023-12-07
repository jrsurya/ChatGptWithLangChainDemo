import streamlit as st
import langchain_helper as lh

st.title("MenuMaestro Bot")
st.latex("A Restaurant Name and Menu Generator")
cuisine = st.sidebar.selectbox("Pick a cuisine", ["Indian", "Mexican", "Italian"])


if cuisine:
    response = lh.generateRestaurant(cuisine)
    st.header(response["restaurant_name"])
    menu_items = response["menu_items"].strip().split(",")
    st.write("****Menu Items***")
    for item in menu_items:
        st.write("-", item)
