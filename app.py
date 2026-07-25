import streamlit as st

st.title("Mon Application de Chiffrement")
st.write("Projet de Cryptographie - César et Vigenère")

# Choix de l'algorithme
choix = st.selectbox("Choisis la méthode :", ["Chiffre de César", "Chiffre de Vigenère"])

# Action : Chiffrer ou déchiffrer
action = st.radio("Que veux-tu faire ?", ["Chiffrer", "Déchiffrer"])

# Saisie du texte
message = st.text_area("Entre ton message ici :")

# Paramètres selon le choix
if choix == "Chiffre de César":
    decalage = st.number_input("Valeur du décalage (ex: 3)", min_value=1, max_value=25, value=3)
else:
    cle = st.text_input("Entre la clé (un mot) :")

# Bouton pour lancer
if st.button("Calculer"):
    if message == "":
        st.warning("Il faut entrer un message !")
    else:
        res = ""
        
        # --- PARTIE CESAR ---
        if choix == "Chiffre de César":
            # Si on déchiffre, on inverse le décalage
            dec = decalage if action == "Chiffrer" else -decalage
            
            for c in message:
                if c.isalpha():
                    if c.isupper():
                        base = ord('A')
                    else:
                        base = ord('a')
                    # Application de la formule de César
                    code = (ord(c) - base + dec) % 26 + base
                    res += chr(code)
                else:
                    res += c

        # --- PARTIE VIGENERE ---
        else:
            if cle == "":
                st.error("Il faut mettre une clé !")
                res = None
            else:
                cle = cle.upper()
                i = 0
                for c in message:
                    if c.isalpha():
                        if c.isupper():
                            base = ord('A')
                        else:
                            base = ord('a')
                        
                        # Récupère le décalage de la lettre de la clé
                        dec = ord(cle[i % len(cle)]) - ord('A')
                        if action == "Déchiffrer":
                            dec = -dec
                            
                        code = (ord(c) - base + dec) % 26 + base
                        res += chr(code)
                        i += 1
                    else:
                        res += c

        # Affichage du résultat
        if res:
            st.success("Résultat :")
            st.write(res)
