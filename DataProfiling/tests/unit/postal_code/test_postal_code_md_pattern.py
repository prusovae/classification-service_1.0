import pytest
from profilling.postal_code import postal_code_md_pattern

@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("credit_card", False),
    ("postal", True),
    ("zip", True),
    ("indeks", True),
    ("index", True)
])


def param_test(request):
    return request.param


def test_postal_code_md_pattern(param_test):
    (input, expected_output) = param_test
    result = postal_code_md_pattern(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
