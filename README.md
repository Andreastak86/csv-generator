# CSV DataGenerator 

**Er du sånn som meg, liker store datasett og fiktive data å leke med?**

Her er verktøyet du trenger. Bare bytt ut antall rader, navn på kolonnene og kjør scriptet. Da har du en ferdig csv-fil på bare et øyeblikk.

---

## Hvorfor bruke denne generatoren?

Når man lærer seg maskinlæring eller datavitenskap, er tilgang på gode data ofte den største flaskehalsen. Ekte data kan være sensitive eller rotete. Med dette verktøyet kan du:

* **Lage store datasett:** Generer tusenvis av rader på under ett sekund.
* **Definere egne regler:** Lag skjulte mønstre i dataene som AI-modeller kan lære av.
* **Reproduserbare resultater:** Ved bruk av `seed` får du de samme tilfeldige tallene hver gang, noe som er kritisk for feilsøking.

---

## Slik fungerer skriptet

Skriptet er bygget opp i logiske moduler for å være mest mulig brukervennlig:

1. **Konfigurasjon:** Her bestemmer du volumet (antall rader).
2. **Definisjon:** Du navngir kolonnene (f.eks. `pris`, `rating`) og velger datatype (desimaler, heltall eller kategorier).
3. **Logikk (The Secret Sauce):** Her legger du inn en matematisk formel som bestemmer "fasiten" (f.eks. om en vare blir returnert eller ikke).
4. **Eksport:** En lynrask lagring til en standard `.csv`-fil.

---

## Koden (`app.py`)

```python
import pandas as pd
import numpy as np

# -------------------- Generere Data --------------------
n_rader = 5000  # <-- Her velger du hvor stor verdenen din skal være
np.random.seed(42)  # Sikrer at vi får de samme tallene hver gang

# -------------------- Definere Kolonner --------------------
data = {
    "produkt_pris": np.random.uniform(100, 500, n_rader).round(2),
    "kunde_rating": np.random.randint(1, 6, n_rader),
    "frakt_tid_dager": np.random.randint(1, 15, n_rader),
    "rabatt_prosent": np.random.randint(0, 70, n_rader),
    "pakke_skadet": np.random.choice([0, 1], n_rader, p=[0.98, 0.02]),
}

df = pd.DataFrame(data)

# -------------------- Legge til Logikk (Fasit) --------------------
retur_score = (
    (df["frakt_tid_dager"] * 0.05)
    + (df["pakke_skadet"] * 0.6)
    - (df["kunde_rating"] * 0.1)
)

df["var_retur"] = (retur_score > 0.2).astype(int)

# -------------------- Eksport --------------------
df.to_csv("mitt_datasett.csv", index=False)

print("Tada! Her er filen din klar for nye eventyr")

