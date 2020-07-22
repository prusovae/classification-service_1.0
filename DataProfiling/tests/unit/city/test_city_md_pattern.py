import pytest
from profilling.city import city_md_pattern


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("city", True),
    ("town", True),
    ("account", False),
    ("acct", False),
    ("locality", True),
    ("settle", True)
])



def param_test(request):
    return request.param


def test_city_md_pattern(param_test):
    (input, expected_output) = param_test
    result = city_md_pattern(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
