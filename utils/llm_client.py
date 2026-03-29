# Import OS module to read environment variables
import os

# Import OpenAI client library
from openai import OpenAI

# Create OpenAI client using API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Function that sends prompt to real LLM
def get_llm_response(prompt):

    # Call OpenAI chat completion API
    response = client.chat.completions.create(
        
        # Model to use (cheap + stable for testing)
        model="gpt-4o-mini",

        # Messages format required by OpenAI
        messages=[
            {"role": "user", "content": prompt}
        ],

        # Set temperature to 0 for deterministic output
        temperature=0
    )

    # Extract text response from API result
    try:
        response = client.chat.completions.create(...)
        return response.choices[0].message.content.strip()

    except Exception:
        return "ERROR: LLM call failed"