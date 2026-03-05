import pandas as pd
import numpy as np


# --------------------Generere Data i filen----------------------------------
n_rader = 5000  # <-- Hvor mange rader du ønsker å generere
np.random.seed(42)  # Et tall som bestemmer at vi får samme tilfeldighet hver gang

# --------------------Definere Kolonner-------------------------------------------------------
# Her definerer vi hvilke kolonner vi ønsker å lage, samt hvilke data vi skal få ut i radene
data = {
    "produkt_pris": np.random.uniform(100, 500, n_rader).round(2),
    "kunde_rating": np.random.randint(1, 6, n_rader),
    "frakt_tid_dager": np.random.randint(1, 15, n_rader),
    "rabatt_prosent": np.random.randint(0, 70, n_rader),
    "pakke_skadet": np.random.choice([0, 1], n_rader, p=[0.98, 0.02]),
}

df = pd.DataFrame(data)

# --------------------Beregne Retur Score og Legge til Kolonne for Retur----------------------------------


retur_score = (
    (df["frakt_tid_dager"] * 0.05)
    + (df["pakke_skadet"] * 0.6)
    - (df["kunde_rating"] * 0.1)
)

df["var_retur"] = (retur_score > 0.2).astype(int)

# --------------------Lagre DataFrame til CSV-------------------------------------------------------

df.to_csv("navnet_pa_csv_fil.csv", index=False)

# --------------------Melding i terminal når filen er opprettet-------------------------------------

print("Tada! Her er filen din klar for nye eventyr")
