import pytest
from profilling.account_number import is_acct_number_value


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("00000000000000000000", False),
    ("11111111111111111111", False),
    ("22222222222222222222", False),
    ("33333333333333333333", False),
    ("44444444444444444444", False),
    ("55555555555555555555", False),
    ("66666666666666666666", False),
    ("77777777777777777777", False),
    ("88888888888888888888", False),
    ("99999999999999999999", False),
    ("00000000000000000000", False),
    ("10817810793278931873", False),
    ("4051181038362388309", False),
    ("40817810736824643812", True)

])


def param_test(request):
    return request.param


def test_is_acct_number_value(param_test):
    (input, expected_output) = param_test
    result = is_acct_number_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
