import random
import streamlit as st

# 1. Il tuo database di gruppi musicali
DATABASE_GRUPPI = [
    {"nome": "Coldplay", "genere": "pop", "umore": "rilassato"},
    {"nome": "Imagine Dragons", "genere": "pop", "umore": "energico"},
    {"nome": "Radiohead", "genere": "rock", "umore": "malinconico"},
    {"nome": "AC/DC", "genere": "rock", "umore": "energico"},
    {"nome": "Daft Punk", "genere": "elettronica", "umore": "energico"},
    {"nome": "Massive Attack", "genere": "elettronica", "umore": "malinconico"},
    {"nome": "Pink Floyd", "genere": "rock", "umore": "rilassato"},
]

# Titolo e descrizione della pagina web
st.title("🎵 Il mio Raccomandatore Musicale")
st.write(
    "Seleziona il genere musicale e il tuo umore attuale: l'app ti consiglierà"
    " un gruppo perfetto per te!"
)

# Estraiamo i generi e gli umori disponibili dal database per i menu a tendina
generi_disponibili = sorted(list(set(g["genere"] for g in DATABASE_GRUPPI)))
umori_disponibili = sorted(list(set(g["umore"] for g in DATABASE_GRUPPI)))

# Creazione dei menu a tendina nella pagina
genere_scelto = st.selectbox("Scegli il genere:", generi_disponibili)
umore_scelto = st.selectbox("Come ti senti?", umori_disponibili)

# Pulsante per generare la raccomandazione
if st.button("Consigliami un gruppo!"):
  # Ricerca nel database
  risultati = [
      gruppo["nome"]
      for gruppo in DATABASE_GRUPPI
      if gruppo["genere"] == genere_scelto and gruppo["umore"] == umore_scelto
  ]

  # Mostriamo il risultato con un effetto grafico carino
  if risultati:
    scelta = random.choice(risultati)
    st.success(f"Ti consiglio di ascoltare: **{scelta}**! 🎸")
  else:
    st.warning(
        "Mi dispiace, non ho trovato nessun gruppo per questa combinazione di"
        " genere e umore."
    )