import pytest
from profilling.account_number import acct_number_md_pattern


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("credit_card", False),
    ("acc", True),
    ("account", True),
    ("acct", True)
])




def param_test(request):
    return request.param


def test_acct_number_md_pattern(param_test):
    (input, expected_output) = param_test
    result = acct_number_md_pattern(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
