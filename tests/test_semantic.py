import pytest

@pytest.mark.parametrize("prompt", [
    "Explain leadership",
    "What is a good leader?"
])
def test_semantic_validation(llm, prompt):

    response = llm(prompt)

    # Pattern 1: keyword validation
    assert any(word in response.lower() for word in ["leader", "leadership"])

    # Pattern 2: length validation
    assert len(response.strip()) > 20