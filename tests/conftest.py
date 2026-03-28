import pytest
from MODULE4_AI_TESTING.utils.llm_mock import get_llm_response

@pytest.fixture
def llm():
    return get_llm_response