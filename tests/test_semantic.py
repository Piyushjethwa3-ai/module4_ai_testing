import pytest

@pytest.mark.parametrize("prompt", [
    "Explain leadership",
    "What is a good leader?"
])
def test_semantic_validation(llm, prompt):

    response = llm(prompt)

    # Log for visibility
    print(f"[SEMANTIC TEST] Prompt: {prompt} | Response: {response}")

    # Pattern 1: flexible keyword validation
    keywords = ["leader", "leadership", "manage", "guide", "inspire"]

    assert any(word in response.lower() for word in keywords), \
        f"Semantic meaning missing: {response}"

    # Pattern 2: ensure meaningful length
    assert len(response.strip()) > 20, "Response too short"