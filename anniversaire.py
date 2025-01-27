import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# Titre principal
st.title("🎉 heureux anniversaire à la meilleure soeur au monde :) 🎉")

# Page d'accueil
st.header("Je voulais te souhaiter ton anniversaire d'une façon un peu spéciale car t'es une personne très spéciale 🥰")

st.write("""
Je suis loin, mais mon amour pour toi traverse toutes les frontières ❤️
""")

# Section 2 : Statistiques amusantes
st.subheader("📊 Quelques statistiques sur toi 🥳")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Nombre de sourires générés chez moi", value="100 000+")

with col2:
    st.metric(label="Taux d'amour pour toi ❤️", value="100%")

# Section 3 : Nuage de mots
st.subheader("✨ Les mots qui te décrivent le mieux")
words = {
    "Mots": ["Généreuse", "Intelligente", "caring person", "Courageuse", "Inspirante"],
    "Importance": [5, 5, 5, 5, 5]
}

word_df = pd.DataFrame(words)

st.bar_chart(word_df.set_index("Mots"))

# Section 4 : Message final
st.subheader(" Mon message pour toi")
st.write("""
**SANA HILWAA LI ARWA3 okht fi l3alam !**

Je te souhaite tout le bonheur du monde tu le mérites vraiment ! inshallah une longue vie pleine de bonbeur, de succès, de santé et beaucoup d'argent 😂 inshallah tu réaaliseras tous tes projets et tes rêves, inshallah rabi yeftahlek ga3 biban el khir w iwef9ak fi koul khetwa w yahmik men koul char w sou2 ya rab, que dieu de protège et te garde pour nous, ton frère qui t'aime plus que tout ❤️❤️❤️
""")
st.balloons()
