# RecommendPy

RecommendPy is a product recommendation system based on NLP and semantic similarity, exposed through FastAPI.  
The project analyzes customers’ purchase history and suggests similar products using Sentence Transformers and cosine similarity.

---

## Features

- Data extraction from SQL Server (SalesLT schema)
- Aggregated product description building
- Semantic embedding generation
- Product similarity computation
- REST API for personalized recommendations
- Embedding persistence using `.pkl` files

---

## Technologies Used

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

## Project Structure

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

Data is extracted from SQL Server using the `SalesLT` schema, including:

- Customers
- Products
- Categories
- Models
- Product descriptions

Each product is represented as a combined textual description:

Product + Category + Model + Description

yaml
Copia codice

---

## NLP Model

The project uses the pre-trained model:

sentence-transformers/all-MiniLM-L6-v2

yaml
Copia codice

---

## Setup

### Clone the repository

git clone https://github.com/your-username/RecommendPy.git
cd RecommendPy

shell
Copia codice

### Install dependencies

pip install -r requirements.txt

yaml
Copia codice

---

## Embedding Generation

Configure the SQL Server connection inside `generate_embeddings.py` and run:

python generate_embeddings.py

yaml
Copia codice

This will generate:

- `Data/products_df.pkl`
- `Data/embeddings.pkl`

---

## Running the API

uvicorn api:app --host 0.0.0.0 --port 8000

arduino
Copia codice

Swagger documentation is available at:

http://localhost:8000/docs

yaml
Copia codice

---

## Endpoints

### GET /recommend/{customerId}

Returns a list of recommended ProductIDs for the specified customer.

Example response:

{
"products": [712, 870, 945, 1021, 1103]
}

yaml
Copia codice

If the customer has no previous purchases, an empty list is returned.

---

## Recommendation Logic

1. Retrieve products purchased by the customer
2. Compute the average embedding of purchased product descriptions
3. Calculate similarity against all products
4. Exclude already purchased products
5. Return the Top 5 most similar products

---

## Future Improvements

- Cold start handling
- Category-based filtering
- Hybrid recommendations
- Redis caching
- Database persistence
- Advanced ranking strategies

---

## Author

Alessandro  
Software Engineer
