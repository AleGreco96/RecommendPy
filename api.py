import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

df = pd.read_pickle("Data\products_df.pkl")
embeddings = pd.read_pickle("Data\embeddings.pkl")

class CustomerRequest(BaseModel):
    customerId: int


@app.get("/recommend/{customerId}")
def recommend(customerId: int):

    purchased = df[df["CustomerID"] == customerId]
    if purchased.empty:
        return {"products": []}

    emb = model.encode(purchased["description"].tolist()).mean(axis=0)

    sims = cosine_similarity([emb], embeddings)[0]

    temp = df.copy()
    temp["sim"] = sims

    purchased_ids = set(purchased["ProductID"])

    candidates = temp[~temp["ProductID"].isin(purchased_ids)]

    recommendations = (
        candidates.sort_values("sim", ascending=False)
        .drop_duplicates(subset=["ProductID"])
        .head(5)
    )

    return recommendations["ProductID"].tolist()

#uvicorn api:app --host 0.0.0.0 --port 8000