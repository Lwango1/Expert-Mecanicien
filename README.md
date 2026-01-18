# 🏍️ Mécanico Expert V3 - Diagnostic Moto Certifié

**Mécanico Expert** est une application intelligente d'aide au diagnostic pour les mécaniciens moto. Elle permet d'identifier rapidement une panne à partir de symptômes précis grâce à une base de données locale robuste.

## 🚀 Fonctionnalités Clés
* **Base de Données Performante** : Plus de 145 pannes moto répertoriées avec diagnostics, pièces concernées et solutions techniques.
* **Recherche Intelligente** : Un algorithme de recherche par mots-clés qui évite les confusions (ex: distingue parfaitement la fumée bleue de la fumée noire).
* **Menu de Sélection** : En cas de symptômes similaires, l'application propose un choix pour affiner le diagnostic.
* **Expertise IA (Local)** : Intégration avec Gemma 3 via Ollama pour fournir des explications techniques détaillées.

## 🛠️ Installation et Utilisation Locale
1. Clonez ce dépôt.
2. Installez les dépendances : `pip install -r requirements.txt`.
3. Assurez-vous d'avoir **Ollama** lancé avec le modèle **Gemma 3** pour les conseils IA.
4. Lancez l'application : `streamlit run main.py`.

## 📊 Structure des Données
L'application utilise un fichier `pannes_moto.xlsx` structuré comme suit :
* **Panne de moto** (Symptôme)
* **Diagnostic** (Cause probable)
* **Pièce concernée**
* **Solution** (Procédure technique)

---
*Développé pour simplifier le quotidien des ateliers de réparation moto.*
