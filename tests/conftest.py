import pytest
from utils.llm_mock import get_llm_response

@pytest.fixture
def llm():
    return get_llm_response