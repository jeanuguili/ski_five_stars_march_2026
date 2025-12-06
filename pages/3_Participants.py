import streamlit as st
import gspread
import pandas as pd
import json
from oauth2client.service_account import ServiceAccountCredentials

st.set_page_config(page_title="Participants", page_icon="👥")

st.title("👥 Participants")

st.subheader("Tableau des participants")

st.write("(peut prendre quelques secondes à charger)")

# --- Google Sheets setup ---
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

gsheet_json = dict(st.secrets["GSHEET"])
#gsheet_json = json.loads(st.secrets["GSHEET_JSON"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(gsheet_json, scope)

#creds = ServiceAccountCredentials.from_json_keyfile_name("service_account_key.json", scope)

client = gspread.authorize(creds)

# Ouvre ton Google Sheet par son URL
sheet_url = "https://docs.google.com/spreadsheets/d/1Uat2jSCo446hajDoc_bR8u1ZOWAqvabao1l0i0s_7W0/edit?gid=0#gid=0"
sheet = client.open_by_url(sheet_url).sheet1

# Lecture
data = sheet.get_all_records()
df = pd.DataFrame(data)

# --- Affichage ---
st.dataframe(df,hide_index=True, use_container_width=True)
st.write("Remboursement via virement ou Wero")

st.subheader("Explication des prix et frais additionnels")
st.write("""
- Coût logement par personne : 109.64€
- Coût forfait 6 jours : 173€
- Coût skis 6 jours : 63€
- Coût Snowboard 6 jours 94.75€
- Si 8 participants, le coût de logement de la 9ème place est divisée en 8 soit 109.64/8 = 13.7€
- Taxe de séjour : 2,53€ par personne par jour, soit 17,71€ par personne
- Caution : environ 400€ pour l'appartement
""")

