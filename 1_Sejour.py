import streamlit as st
from PIL import Image

st.set_page_config(page_title="Séjour", page_icon="🎿")

st.title("🏔️ Semaine de ski mars 2026 !")

st.header("📅 Dates")
st.write(" **Du samedi 21 mars 2026 au samedi 28 mars 2026**")

st.header("📍 Destination")
st.subheader("La Toussuire (Les Sybelles)")
st.write("""
Nous partons cette année à **La Toussuire**, une station située à **1 750 m d'altitude**, au cœur du domaine skiable **Les Sybelles** dans les Alpes.  
Avec ses **310 km de pistes** variées, elle est idéale pour profiter d'une semaine de ski et se mettre des caisses.
""")

carte_sybelles = "https://raw.githubusercontent.com/jeanuguili/ski_five_stars_march_2026/main/images/screenshot_emplacement_sybelles.png"
st.image(carte_sybelles, caption="Les Sybelles", use_container_width=True)

st.header("La résidence")
st.subheader("Résidence CGH L'Alpaga ⭐⭐⭐⭐⭐")
st.write("""
Comme tous les ans, c'est sur **Sunweb** que nous réservons notre séjour tout compris. Et cette année, c'est le thème **GRAND LUXE** qui est à l'honneur en cette semaine peu fréquentée. 
Nous avons donc jeté notre dévolu sur cette résidence 5 étoiles qui nous accueillera tous dans un grand appartement 10 couchages.
""")

st.image("https://www.cgh-residences.com/photos/residences/sliders/lalpaga-exterieur-2-%C2%A9estelle-daviere-1920x1080_2173.webp", caption="", use_container_width=True)
st.markdown('<a href="https://www.sunweb.fr/ski/france/les-sybelles/la-toussuire/residence-lalpaga?Participants%5B0%5D%5B0%5D=1995-11-29&Participants%5B0%5D%5B1%5D=1995-11-29&Participants%5B0%5D%5B2%5D=1995-11-29&Participants%5B0%5D%5B3%5D=1995-11-29&Participants%5B0%5D%5B4%5D=1995-11-29&Participants%5B0%5D%5B5%5D=1995-11-29&Duration%5B0%5D=8&DurationsRanges=8-8&Mealplan=LG&Month=2026-03-01&TransportType=SelfDrive" target="_blank">Lien Sunweb de la résidence</a>', unsafe_allow_html=True)

st.subheader("L'emplacement 📍")
st.write("""
Située à 300m du centre ville, 50m de la piste débutants "Grands Lutins" et 300m de la piste bleue Comborcière, l'emplacement offre un parfait équilibre entre tranquillité et proximité de l'animation.
""")
carte_alpage = "https://raw.githubusercontent.com/jeanuguili/ski_five_stars_march_2026/main/images/screenshot_emplacement_residence.png"
st.image(carte_alpage, caption="", use_container_width=True)
carte_alpage_large = "https://raw.githubusercontent.com/jeanuguili/ski_five_stars_march_2026/main/images/screenshot_emplacement_residence_large.png"
st.image(carte_alpage_large, caption="", use_container_width=True)
st.markdown('<a href="https://skimap.org/skiareas/view/765" target="_blank">Plan des pistes</a>', unsafe_allow_html=True)


st.subheader("Les équipements 🏊‍♂️")
st.write("""
- Piscine 🏊‍♂️
- Sauna ♨️
- Hammam 🧖‍♀️
- Wifi dans les chambres 📶
- Réception 🛎️  
  - Samedi : 07:30 - 20:00  
  - Dimanche à vendredi : 08:00 - 11:00 et 16:00 - 20:00
""")
st.image("https://www.cgh-residences.com/photos/residences/sliders/cgh-lalpaga_espaceludique%C2%A9foudimages-21_2220.webp", caption="", use_container_width=True)

st.subheader("L'appartement 🛋️")
st.write("""
- Superficie : environ 95 m²
- Balcon ou terrasse
- Cuisine équipée :
  - Plaques de cuisson
  - Combiné four/micro-ondes
  - Cafetière
  - Grille-pain
  - Lave-vaisselle
- Télévision (TV par satellite)
- Salle de séjour : 2 lits (1 x canapé-lit 2 personnes)
- Chambres à coucher : 4
  - Chambre 1 : 2 lits (1 x lit double)
  - Chambre 2 : 2 lits (1 x lit double)
  - Chambre 3 : 2 lits (2 x lits simples)
  - Chambre 4 : 2 lits (2 x lits simples)
- WC séparés
- Salles de bain : 3
  - Salle de bain 1 : baignoire, toilettes
  - Salle de bain 2 : douche, sèche-cheveux
  - Salle de bain 3 : douche
- **Linge de lit inclus** 🤯🤯🤯
- **Linge de toilette inclus** 🤯🤯🤯
""")
st.image("https://static.sunweb.fr/products/Images/Original/39200000/44000/39244829-Original.jpg?mode=crop&scale=both&width=1280&height=960", caption="", use_container_width=True)
st.image("https://static.sunweb.fr/products/Images/Original/39200000/44000/39244828-Original.jpg?mode=crop&scale=both&width=1280&height=960", caption="", use_container_width=True)
st.image("https://static.sunweb.fr/products/Images/Original/39200000/44000/39244827-Original.jpg?mode=crop&scale=both&width=1280&height=960", caption="", use_container_width=True)

