import chromadb
from db.create_vector_db import GeminiEmbeddingFunction

# Initialize the query embedding function
embed_fn = GeminiEmbeddingFunction(document_mode=False)
chroma_client = chromadb.Client()
db = chroma_client.get_collection("my_vector_db")

def retrieve_documents(query):
    # Embed the query using the same embedding function
    query_embedding = embed_fn([query])[0]
    # Perform the query using the embedding
    result = db.query(query_embeddings=[query_embedding], n_results=1)
    # Check if documents are returned
    if result["documents"]:
        # Return the first document
        return result["documents"][0][0]
    else:
        return None
