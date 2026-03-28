import pytest
from utils.validator import validate_format
from utils.reporter import save_result

@pytest.mark.parametrize("prompt", [
    "",
    None,
    "123123!!!@@@",
    "DROP TABLE users"
])
def test_negative_inputs(llm, prompt):
    response = llm(str(prompt))

    result = validate_format(response)
    save_result("negative_test", prompt, response, result)

    assert result