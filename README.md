Retrieval-Augmented Generation (RAG) Project
This project implements a Retrieval-Augmented Generation (RAG) architecture using a local vector database with ChromaDB and Google’s Gemini API for document retrieval and natural language generation. It allows users to add documents to a vector database, perform queries, and get natural language answers based on retrieved documents.

Project Structure

## Prerequisites

- Python 3.8 or higher
- Google API Key for Generative AI (set as GOOGLE_API_KEY in environment variables)
- ChromaDB and Google Gemini API libraries
- Install Required Packages
- Install the required packages from requirements.txt:

`pip install -r requirements.txt`

Required Environment Variables

- Set Google API Key: In your terminal or .zshrc (or .bashrc) file, set your Google API Key as an environment variable:

Verify Environment Setup: Check that the API key is accessible by running:

`echo $GOOGLE_API_KEY`

## Project Components

1. data/documents.txt: Document Data
   Add documents in documents.txt using the following structure:

```
----Document 1

Title: Introduction to Retrieval-Augmented Generation (RAG)

Content:
Retrieval-Augmented Generation (RAG) combines document retrieval with language generation. A RAG system retrieves relevant documents from a database in response to a query, then passes the information to a language model to generate coherent answers...

----Document 2

Title: Setting Up a Local Vector Database for Document Retrieval

Content:
To create a vector database...

----Document 3

Title: Using Gemini Google AI Models for RAG

Content:
Gemini models offer advanced capabilities for both embedding generation and language generation...
```

2. db/create_vector_db.py: Database Creation

This script loads documents from data/documents.txt, generates embeddings using Google Gemini, and populates a local vector database with ChromaDB.

Usage:

`python db/create_vector_db.py`

This command will read documents.txt, generate embeddings, and add them to the vector database.

3. agent/agent.py: Document Retrieval Agent
   Defines the retrieve_documents function, which uses the same embedding function for document and query embeddings. It sets document_mode=False during querying to ensure the correct embedding type.

4. scripts/query_agent.py: Query the Agent
   query_agent.py lets you input a question for the RAG model, which retrieves relevant documents from the vector database and generates a natural language answer based on the retrieved information.

## Usage:

Queries run in the terminal

`python scripts/query_agent.py "How do you create a vector db?"`

Or, run without a question to enter one interactively:

`python scripts/query_agent.py`
