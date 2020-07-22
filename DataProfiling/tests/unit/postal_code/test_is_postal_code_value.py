import pytest
from profilling.postal_code import is_postal_code_value


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("123456", False),
    ("350089", True),
    ("108850", True),
    ("108811", True)
])


def param_test(request):
    return request.param


def test_postal_code_value(param_test):
    (input, expected_output) = param_test
    result = is_postal_code_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
