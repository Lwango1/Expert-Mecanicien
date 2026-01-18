import streamlit as st
import pandas as pd
import ollama
import os

# 1. Configuration de l'interface
st.set_page_config(page_title="Expert Méca Moto", page_icon="🏍️")
st.title("🏍️ Diagnostic Moto Certifié")


# 2. Chargement et nettoyage des données
@st.cache_data
def charger_base_pannes():
    fichier = 'pannes_moto.xlsx'
    if os.path.exists(fichier):
        df = pd.read_excel(fichier)
        for col in df.columns:
            df[col] = df[col].astype(str).str.strip()
        return df
    return None


df = charger_base_pannes()

if df is not None:
    st.sidebar.success(f"✅ {len(df)} pannes répertoriées")

    # 3. Saisie utilisateur
    question = st.text_input("Symptôme observé (ex: batterie) :")

    if question:
        question_clean = question.lower().strip()
        mots_saisis = question_clean.split()

        # Recherche de toutes les pannes contenant les mots saisis
        tous_les_matches = df[df['Panne de moto'].apply(lambda x: all(m in str(x).lower() for m in mots_saisis))]

        if not tous_les_matches.empty:
            # SI PLUSIEURS RÉSULTATS : Proposer un choix
            if len(tous_les_matches) > 1:
                st.warning(f"🤔 Plusieurs pannes correspondent à '{question}'. Laquelle choisissez-vous ?")
                options = tous_les_matches['Panne de moto'].tolist()
                choix_final = st.selectbox("Sélectionnez la panne précise :", options)
                res = tous_les_matches[tous_les_matches['Panne de moto'] == choix_final].iloc[0]
            else:
                # SI UN SEUL RÉSULTAT : Affichage direct
                res = tous_les_matches.iloc[0]

            # 4. Affichage des résultats
            st.error(f"### 🛠️ Résultat : {res['Panne de moto']}")

            col1, col2 = st.columns(2)
            with col1:
                st.info(f"**Diagnostic :**\n{res['Diagnostic']}")
            with col2:
                st.warning(f"**Pièce concernée :**\n{res['Pièce concernée']}")

            st.success(f"**Technique de solution :**\n{res['Solution']}")

            # 5. IA Gemma 3
            with st.spinner("Analyse technique..."):
                try:
                    prompt = f"Expert mécanicien. Explique pourquoi '{res['Panne de moto']}' mène au diagnostic '{res['Diagnostic']}'. Sois bref."
                    reponse = ollama.generate(model='gemma3:4b', prompt=prompt)
                    st.markdown("---")
                    st.info(f"**💡 Conseil de l'IA :**\n{reponse['response']}")
                except:
                    st.warning("IA indisponible.")
        else:
            st.warning("⚠️ Aucun cas trouvé pour ce mot.")
else:
    st.error("Fichier 'pannes_moto.xlsx' introuvable.")