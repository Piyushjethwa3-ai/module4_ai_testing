# Import OS to read environment variables
import os

# Import mock version
from utils.llm_mock import get_llm_response as mock_llm

# Try importing real client (safe import)
try:
    from utils.llm_client import get_llm_response as real_llm
except ImportError:
    real_llm = None


# Decide which LLM to use
def get_llm_response(prompt):

    # Read environment variable (default = mock)
    use_real = os.getenv("USE_REAL_LLM", "false").lower() == "true"

    # If real LLM is enabled AND available
    if use_real and real_llm:
        return real_llm(prompt)

    # Otherwise fallback to mock
    return mock_llm(prompt)