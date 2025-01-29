from langchain_community.document_loaders import DataFrameLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import sqlite3
import pandas as pd

def load_and_vectorize_data():
    """Load data from the database and vectorize it."""
    
    # Load data from SQLite
    conn = sqlite3.connect('hospital.db')
    df_physicians = pd.read_sql_query("SELECT * FROM Physicians", conn)
    df_schedules = pd.read_sql_query("SELECT * FROM Schedules", conn)
    df_specialities = pd.read_sql_query("SELECT * FROM Specialities", conn)
    df_pricelist = pd.read_sql_query("SELECT * FROM Pricelist", conn)
    conn.close()

    # Combine data into a single DataFrame
    combined_data = pd.concat([df_physicians, df_schedules, df_specialities, df_pricelist], axis=0)

    # Check the columns to identify the text column
    print(combined_data.columns)

    # Ensure that the 'Definition' column exists or specify the correct column with text data
    text_column = "Definition"  # Adjust if needed
    
    # Check if the column exists in the dataframe
    if text_column not in combined_data.columns:
        raise ValueError(f"Column '{text_column}' not found in the DataFrame")
    
    # Vectorize the data
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(
        DataFrameLoader(combined_data, page_content_column=text_column).load(), 
        embeddings
    )
    
    # Save the vector store locally
    vector_store.save_local("vector_store")

    print("Data vectorized and saved successfully!")
if __name__ == '__main__':
    load_and_vectorize_data()
