import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import date

# Vérifier si le token GitHub est bien chargé
github_token = os.getenv("GITHUB_TOKEN")

if github_token:
    st.write("🔐 Accès GitHub sécurisé.")
else:
    st.warning("⚠️ Erreur : Le token GitHub n'est pas disponible.")

# Titre principal
st.title("🎉 heureux anniversaire à la meilleure soeur au monde :) 🎉")

# Page d'accueil
st.header("Je voulais te souhaiter ton anniversaire d'une façon un peu spéciale car t'es une personne très spéciale 🥰 la raison pour laquelle j'ai pris ce retard le temps de mettre ça en place ")

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
    "Mots": ["Généreuse", "Intelligente", "Caring person", "Courageuse", "Inspirante"],
    "Importance": [5, 5, 5, 5, 5]
}

word_df = pd.DataFrame(words)

st.bar_chart(word_df.set_index("Mots"))

# Section 4 : Message final
st.subheader("💌 Mon message pour toi")
st.write("""
**SANA HILWAA LI ARWA3 okht fi l3alam !**  

Je te souhaite tout le bonheur du monde, tu le mérites vraiment !  
Inshallah une longue vie pleine de bonheur, de succès, de santé et beaucoup d'argent 😂  
Inshallah tu réaliseras tous tes projets et tes rêves,  
Que Dieu te protège et te garde pour nous,  
Ton frère qui t'aime plus que tout ❤️❤️❤️  
""")
st.balloons()
