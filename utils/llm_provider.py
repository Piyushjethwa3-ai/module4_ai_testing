# Import OS to read environment variables
import os

# Import mock version
from utils.llm_mock import get_llm_response as mock_llm

from utils.llm_client import get_llm_response as real_llm


# Decide which LLM to use
def get_llm_response(prompt):

    use_real = os.getenv("USE_REAL_LLM", "false").lower() == "true"

    if use_real:
        print("Using REAL LLM")

        if real_llm is None:
            raise RuntimeError("Real LLM not available. Check llm_client import or dependencies.")

        return real_llm(prompt)

    print("Using MOCK LLM")
    return mock_llm(prompt)