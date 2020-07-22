import pytest
from profilling.country import countries_md_pattern


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("country", True),
    ("town", False),
    ("account", False),
    ("acct", False),
    ("locality", False),
    ("settle", False)
])


def param_test(request):
    return request.param


def test_country_md_pattern(param_test):
    (input, expected_output) = param_test
    result = countries_md_pattern(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
