import streamlit as st
from PIL import Image

st.set_page_config(page_title="Transport", page_icon="🚆")

st.title("🚆 Transport et accès à la station")

st.header("🎯 Gare d'arrivée")
st.subheader("👉 **Saint-Jean-de-Maurienne - Vallée de l’Arvan**")

st.header("🚂 Si vous voulez prendre le train avec nous")

st.subheader("Aller : 11H34 (Direct) - 61€ (30/11/2025)")
billet_aller = Image.open("images\\billet_aller_sybelles.png")
st.image(billet_aller, caption="", use_container_width=True)

st.subheader("Retour : 15h54 (Direct) - 53€ (30/11/2025)")
billet_retour = Image.open("images\\billet_retour_sybelles.png")
st.image(billet_retour, caption="", use_container_width=True)

st.markdown(
    "- **Réserver 👉** : https://www.sncf-connect.com/"
)

st.header("🚌 Navette Gare - Station")
st.write("""
- Arrêt de départ : **SAINT JEAN DE MAURIENNE Gare routiere**
- Arrêt d'arrivée : **LA TOUSSUIRE Office de tourisme**
""")
st.subheader("🕒 Horaires (attention à vos trains)")
horaires_altibus = Image.open("images\horaires_altibus_toussuire.png")
st.image(horaires_altibus, caption="", use_container_width=True)

st.subheader("💵 Tarifs")
st.write("""
Aller-retour :
- **18.90€ (adulte)**
- **13.50€ (-25 ans cc Colette)**
""")
st.markdown(
    "- **Réserver 👉** : https://www.altibus.com/"
)
