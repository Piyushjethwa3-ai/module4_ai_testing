import pytest
from utils.validator import validate_format
from utils.reporter import save_result
from utils.logger import log


# Test invalid / edge-case inputs
@pytest.mark.parametrize("prompt", [
    "",
    None,
    "123123!!!@@@",
    "DROP TABLE users"
])
def test_negative_inputs(llm, prompt):

    # Convert None to string to avoid crash
    safe_prompt = str(prompt)

    # Call LLM
    response = llm(safe_prompt)

    # Log execution
    log(f"[NEGATIVE TEST] Prompt: {prompt} | Response: {response}")

    # Validate response format
    format_valid = validate_format(response)

    # Ensure response is not crashing / None
    not_null = response is not None

    # Combine result
    result = format_valid and not_null

    # Save result
    save_result("negative_test", prompt, response, result)

    # Assertions
    assert not_null, "LLM returned None"
    assert format_valid, f"Invalid response format: {response}"

    # Flexible expectation for real LLM
    # Should gracefully handle bad input
    assert len(response.strip()) > 0, "LLM failed to handle invalid input"