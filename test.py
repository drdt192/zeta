import httpx
from dotenv import load_dotenv
import os

load_dotenv()

def generate(input):
    
    response = httpx.post(
        url="https://api.groq.com/openai/v1/chat/completions", #endpoint, remember that the server expects specific data
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv("GROQ_API_KEY")}"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [{ "role": "user", "content": input}]
        }
    )

    data = response.json()
    return data["choices"][0]["message"]["content"]

print(generate("wassup"))