import pytest
from utils.validator import validate_length
from utils.reporter import save_result

@pytest.mark.parametrize("prompt", [
    "HELLO!!!!",
    "refund????",
    "   help me   ",
    "asap pls bro"
])
def test_robustness(llm, prompt):
    response = llm(prompt)

    result = validate_length(response)
    save_result("robustness_test", prompt, response, result)

    assert result