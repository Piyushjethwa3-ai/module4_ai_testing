import pytest
from utils.llm_provider import get_llm_response
from utils.reporter import generate_summary


@pytest.fixture
def llm():
    return get_llm_response

def pytest_sessionfinish(session, exitstatus):
    generate_summary()