# Import OS module to read environment variables
import os

# Import OpenAI client library
from openai import OpenAI

# Create OpenAI client using API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Function that sends prompt to real LLM
def get_llm_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"ERROR: {str(e)}"