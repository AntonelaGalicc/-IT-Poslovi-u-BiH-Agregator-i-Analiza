import streamlit as st
import pandas as pd
import sqlite3

# Postavke stranice
st.set_page_config(page_title="IT Poslovi BiH Analytics", layout="wide")

st.title("📊 IT Poslovi u BiH – Agregator i Analiza")
st.write("Pregled najtraženijih tehnologija i lokacija na IT sceni u Bosni i Hercegovini.")

# Učitavanje podataka iz SQLite baze
@st.cache_data
def ucitaj_podatke():
    conn = sqlite3.connect('it_poslovi.db')
    df = pd.read_sql("SELECT * FROM oglasi", conn)
    conn.close()
    return df

df = ucitaj_podatke()

# Prikaz osnovnih metrika na vrhu
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Ukupno pronađeno oglasa", value=len(df))
with col2:
    st.metric(label="Broj Remote pozicija", value=len(df[df['lokacija'] == 'Remote']))

st.markdown("---")

# Vizualizacija po lokacijama
st.subheader("📍 Poslovi po lokacijama")
lokacije_counts = df['lokacija'].value_counts()
st.bar_chart(lokacije_counts)

# Vizualizacija po tehnologijama
st.subheader("💻 Najtraženije tehnologije")
# Rastavljamo string tehnologija natrag u pojedinačne stavke za graf
sve_tehnologije = []
for tech_str in df['tehnologije'].dropna():
    if tech_str:
        sve_tehnologije.extend([t.strip() for t in tech_str.split(',') if t.strip()])

if sve_tehnologije:
    tech_df = pd.Series(sve_tehnologije).value_counts()
    st.bar_chart(tech_df)
else:
    st.write("Nema zabilježenih tehnologija u bazi.")

# Prikaz sirovih podataka na dnu
st.subheader("📋 Pregled svih oglasa u bazi")
st.dataframe(df[['naslov_i_opis', 'tehnologije', 'lokacija', 'link']])