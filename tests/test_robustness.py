import pytest
from utils.validator import validate_length
from utils.reporter import save_result
from utils.logger import log


# Test messy / real-world user inputs
@pytest.mark.parametrize("prompt", [
    "HELLO!!!!",
    "refund????",
    "   help me   ",
    "asap pls bro"
])
def test_robustness(llm, prompt):

    # Call LLM
    response = llm(prompt)

    # Log response for debugging
    log(f"[ROBUSTNESS TEST] Prompt: {prompt} | Response: {response}")

    # Validate response is meaningful (not empty or too short)
    length_valid = validate_length(response)

    # Additional safety check (real LLM pattern)
    not_empty = len(response.strip()) > 0

    # Combine validations
    result = length_valid and not_empty

    # Save result
    save_result("robustness_test", prompt, response, result)

    # Assertions
    assert not_empty, f"Empty response for input: {prompt}"
    assert length_valid, f"Response too short: {response}"

    # Optional flexible validation
    assert isinstance(response, str), "Response is not a string"