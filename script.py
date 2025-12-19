# ==========================================
# CONFIGURAZIONE: Modifica il nome del file qui sotto
# ==========================================
NOME_FILE_INPUT = "pw.csv"
# ==========================================

def leggi_dati(percorso_file):
    """
    Legge un file con formato 'Nome, Password, Nota;'
    e restituisce un array di array.
    """
    matrice_dati = []

    try:
        with open(percorso_file, 'r', encoding='utf-8') as f:
            # Leggiamo tutto e dividiamo per il punto e virgola
            blocchi = f.read().split(';')

            for blocco in blocchi:
                # Puliamo il blocco da spazi e rinvii a capo
                riga_pulita = blocco.strip()

                if riga_pulita:
                    # Dividiamo per virgola e puliamo ogni singolo elemento
                    elementi = [item.strip() for item in riga_pulita.split(',')]
                    matrice_dati.append(elementi)

        return matrice_dati

    except FileNotFoundError:
        print(f"Errore: Il file '{percorso_file}' non esiste nella cartella corrente.")
        return None

def organizza_per_categorie(matrice):
    # Questa sarà la nostra lista di liste finale
    liste_finali = []
    # Qui terremo traccia di quali categorie sono già presenti in ogni lista
    categorie_per_lista = []

    for riga in matrice:
        nome = riga[0]
        # Se la categoria (A, B, ecc.) non esiste, usiamo 'SenzaCategoria'
        categoria = riga[2] if len(riga) > 2 else "SenzaCategoria"

        inserito = False

        # Proviamo a inserire il nome in una delle liste esistenti
        for i in range(len(liste_finali)):
            # Se la categoria non è ancora presente in questa lista
            if categoria not in categorie_per_lista[i]:
                liste_finali[i].append(nome)
                categorie_per_lista[i].add(categoria)
                inserito = True
                break

        # Se non abbiamo trovato nessuna lista valida, ne creiamo una nuova
        if not inserito:
            liste_finali.append([nome])
            # Usiamo un set() per una ricerca più veloce delle categorie
            categorie_per_lista.append({categoria})

    return liste_finali

import random

def mescola_lista(lista):
    """
    Mescola gli elementi della lista direttamente (in-place).
    """
    random.shuffle(lista)
    return lista

def scrivi_html(NOME_FILE, NOME_DONATORE, NOME_RICEVENTE):
    # Aggiunge l'estensione .html al nome fornito
    nome_completo = f"{NOME_FILE}.html"

    PREAMBOLO = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Messaggio per Davide</title>
    <style>
        /* Reset di base e font moderno */
        body {
            margin: 0;
            height: 100vh; /* Occupa tutta l'altezza dello schermo */
            display: flex;
            justify-content: center; /* Centra orizzontalmente */
            align-items: center; /* Centra verticalmente */
            background-color: #f0f2f5; /* Colore di sfondo neutro */
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        /* La "cartolina" che contiene il testo */
        .card {
            background: white;
            padding: 2rem 3rem; /* Spaziatura interna */
            border-radius: 16px; /* Angoli arrotondati */
            box-shadow: 0 4px 12px rgba(0,0,0,0.1); /* Ombra leggera */
            text-align: center;
        }

        /* Stile del testo principale */
        h1 {
            color: #333;
            font-weight: normal;
            font-size: 1.8rem;
            margin: 0;
        }

        /* Stile per l'enfasi su Simone */
        .highlight {
            font-weight: bold;
            color: #007BFF; /* Un bel blu acceso */
            font-style: normal; /* Rimuove il corsivo di default del tag em */
        }
    </style>
</head>
<body>

    <div class="card">
        <h1>Ciao """

    TESTO_IN_MEZZO = """, tu devi fare il regalo a <em class="highlight">"""

    POSTAMBOLO = """</em></h1>
    </div>

</body>
</html>"""

    # Il testo esatto che vuoi scrivere
    testo_da_scrivere = PREAMBOLO + NOME_DONATORE + TESTO_IN_MEZZO + POSTAMBOLO

    # Crea il file e scrive il testo
    with open(nome_completo, "w", encoding="utf-8") as f:
        f.write(testo_da_scrivere)

### ESECUZIONE DEL PROGRAMMA


# Esecuzione della funzione
elenco_persone = leggi_dati(NOME_FILE_INPUT) # Creo l'elenco delle persone
elenco_persone = mescola_lista(elenco_persone) # Randomizzo
smistate = organizza_per_categorie(elenco_persone) # Creo le liste

for lista in smistate:
    randomized = mescola_lista(lista)
    print(randomized)
    for i in range(len(randomized)):
        if ( (i + 1) < len(randomized) ):
            j = i+1
        if ( (i + 1) == len(randomized) ):
            j = 0
        donatore = randomized[i]
        ricevente = randomized[j]
        for persona in elenco_persone:
            if persona[0] = donatore:
                file_da_scrivere = persona[1]
        scrivi_html(file_da_scrivere, donatore, ricevente)
