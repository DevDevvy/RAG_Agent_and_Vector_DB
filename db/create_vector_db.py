import chromadb
from chromadb import Documents
from config.secrets import get_google_api_key
import google.generativeai as genai
import re

# Configure API Key
genai.configure(api_key=get_google_api_key())

# Define an embedding function using Gemini
class GeminiEmbeddingFunction(chromadb.EmbeddingFunction):
    def __init__(self, document_mode=True):
        self.document_mode = document_mode

    def __call__(self, input: Documents):
        task_type = "retrieval_document" if self.document_mode else "retrieval_query"
        response = genai.embed_content(
            model="models/text-embedding-004",
            content=input,
            task_type=task_type,
        )
        return response["embedding"]

# Parse the documents.txt file
def load_documents(file_path):
    documents = []
    with open(file_path, 'r') as file:
        content = file.read()
        # Split by each document section using regex
        raw_docs = re.split(r'----Document \d+', content)
        for raw_doc in raw_docs:
            if raw_doc.strip():  # Skip empty sections
                # Extract title and content
                title_match = re.search(r"Title:\s*(.*)", raw_doc)
                content_match = re.search(r"Content:\s*(.*)", raw_doc, re.DOTALL)
                if title_match and content_match:
                    title = title_match.group(1).strip()
                    content = content_match.group(1).strip()
                    # Combine title and content for embedding
                    full_text = f"{title}\n{content}"
                    documents.append(full_text)
    return documents

# Load and embed documents from the file
file_path = "data/documents.txt"
documents = load_documents(file_path)

# Initialize the embedding function and database
embed_fn = GeminiEmbeddingFunction(document_mode=True)
chroma_client = chromadb.Client()
db = chroma_client.get_or_create_collection(name="my_vector_db", embedding_function=embed_fn)

# Populate the database
db.add(documents=documents, ids=[str(i) for i in range(len(documents))])
print(f"Document count in DB: {db.count()}")
