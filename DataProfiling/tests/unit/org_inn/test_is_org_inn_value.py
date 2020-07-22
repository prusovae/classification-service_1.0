import pytest
from profilling.org_inn import is_org_inn_value


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("1231231231", False),
    ("5047155633", True),
    ("1315000052", True),
    ("5047125766", True)
])


def param_test(request):
    return request.param


def test_org_inn_value(param_test):
    (input, expected_output) = param_test
    result = is_org_inn_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
