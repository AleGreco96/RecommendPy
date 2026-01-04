import pyodbc
import pickle
import urllib
import pandas as pd
from sqlalchemy import create_engine
from sentence_transformers import SentenceTransformer

server = r'localhost\SQLEXPRESS'
database = 'SellinProduction'
driver = '{ODBC Driver 17 for SQL Server}'

params = urllib.parse.quote_plus(
    f"DRIVER={driver};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"Trusted_Connection=yes;"
    f"TrustServerCertificate=yes;"
)

connection_string = f"mssql+pyodbc:///?odbc_connect={params}"

engine = create_engine(connection_string)

query = """
SELECT CustomerID, 
       SalesLT.[Product].ProductID, 
       SalesLT.[Product].[Name] AS [Product], 
       SalesLT.ProductCategory.[Name] AS Category,
       SalesLT.ProductModel.[Name] AS Model,
       SalesLT.ProductDescription.[Description] AS Description
FROM SalesLT.SalesOrderHeader
RIGHT JOIN SalesLT.SalesOrderDetail ON SalesLT.SalesOrderHeader.SalesOrderID = SalesLT.SalesOrderDetail.SalesOrderID
RIGHT JOIN SalesLT.[Product] ON SalesLT.SalesOrderDetail.ProductID = SalesLT.[Product].ProductID
LEFT JOIN SalesLT.ProductCategory ON SalesLT.[Product].ProductCategoryID = SalesLT.ProductCategory.ProductCategoryID
LEFT JOIN SalesLT.ProductModel ON SalesLT.[Product].ProductModelID = SalesLT.ProductModel.ProductModelID
LEFT JOIN SalesLT.ProductModelProductDescription ON SalesLT.ProductModel.ProductModelID = SalesLT.ProductModelProductDescription.ProductModelID
LEFT JOIN SalesLT.ProductDescription ON SalesLT.ProductModelProductDescription.ProductDescriptionID = SalesLT.ProductDescription.ProductDescriptionID
"""

df = pd.read_sql(query, engine)

df = df.dropna()
df['description'] = df['Product'] + " " + df['Category'] + " " + df['Model'] + " " + df['Description']

print("Loading Model...")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

print("Generating Embeddings...")
embeddings = model.encode(df['description'].tolist())

print("Saving products_df.pkl ...")
df.to_pickle("Data\products_df.pkl")

print("Saving embeddings.pkl ...")
with open("Data\embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)

print("Done")
