# RecommendPy

RecommendPy è un sistema di product recommendation basato su NLP e similarità semantica, esposto tramite FastAPI.  
Il progetto analizza lo storico degli acquisti dei clienti e suggerisce prodotti simili utilizzando Sentence Transformers e cosine similarity.

---

## Funzionalità

- Estrazione dati da SQL Server (schema SalesLT)
- Costruzione di descrizioni prodotto aggregate
- Generazione di embedding semantici
- Calcolo della similarità tra prodotti
- API REST per raccomandazioni personalizzate
- Persistenza degli embedding su file `.pkl`

---

## Tecnologie utilizzate

- Python
- FastAPI
- Pandas
- SQLAlchemy
- pyodbc
- Sentence Transformers
- Scikit-learn
- SQL Server
- Uvicorn

---

## Struttura del progetto

RecommendPy/
│
├── api.py
├── generate_embeddings.py
│
├── Data/
│ ├── products_df.pkl
│ └── embeddings.pkl
│
├── requirements.txt
└── README.md

yaml
Copia codice

---

## Dataset

I dati vengono estratti da SQL Server utilizzando lo schema `SalesLT`:

- Clienti
- Prodotti
- Categorie
- Modelli
- Descrizioni prodotto

Ogni prodotto viene rappresentato come una descrizione testuale combinata:

Product + Category + Model + Description

yaml
Copia codice

---

## Modello NLP

Viene utilizzato il modello pre-addestrato:

sentence-transformers/all-MiniLM-L6-v2

yaml
Copia codice

---

## Setup

### Clonazione repository

git clone https://github.com/tuo-username/RecommendPy.git
cd RecommendPy

shell
Copia codice

### Installazione dipendenze

pip install -r requirements.txt

yaml
Copia codice

---

## Generazione embedding

Configurare la connessione a SQL Server nello script `generate_embeddings.py` e lanciare:

python generate_embeddings.py

yaml
Copia codice

Verranno creati i file:

- `Data/products_df.pkl`
- `Data/embeddings.pkl`

---

## Avvio API

uvicorn api:app --host 0.0.0.0 --port 8000

yaml
Copia codice

Documentazione Swagger disponibile su:

http://localhost:8000/docs

yaml
Copia codice

---

## Endpoint

### GET /recommend/{customerId}

Restituisce una lista di ProductID raccomandati per il cliente indicato.

Esempio risposta:

{
"products": [712, 870, 945, 1021, 1103]
}

yaml
Copia codice

Se il cliente non ha acquisti precedenti, viene restituita una lista vuota.

---

## Logica di raccomandazione

1. Recupero prodotti acquistati dal cliente
2. Calcolo embedding medio delle descrizioni
3. Calcolo similarità con tutti i prodotti
4. Esclusione prodotti già acquistati
5. Selezione dei Top 5 prodotti più simili

---

## Miglioramenti futuri

- Gestione cold start
- Filtri per categoria
- Raccomandazioni ibride
- Cache con Redis
- Persistenza su database
- Ranking avanzato

---

## Autore

Alessandro  
Software Engineer
