import argparse
from agent.agent import retrieve_documents
import google.generativeai as genai
from config.secrets import get_google_api_key

# Initialize API Key
genai.configure(api_key=get_google_api_key())

def query_agent(question):
    passage = retrieve_documents(question)
    if not passage:
        return "No relevant information found."

    prompt = f"""
    You are a helpful bot answering questions based on the passage below:
    
    QUESTION: {question}
    PASSAGE: {passage.replace("\n", " ")}
    """

    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query the agent with a specific question.")
    parser.add_argument("question", nargs="?", help="The question to ask the agent")
    args = parser.parse_args()

    # If no question is provided as an argument, prompt for it interactively
    question = args.question if args.question else input("Enter your question: ")

    answer = query_agent(question)
    print(f"Answer: {answer}")
