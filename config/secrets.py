import os

# To set the GOOGLE_API_KEY in your environment:
# export GOOGLE_API_KEY="your_google_api_key"

def get_google_api_key():
    return os.getenv("GOOGLE_API_KEY")
