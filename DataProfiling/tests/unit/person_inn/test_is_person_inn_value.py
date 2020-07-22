import pytest
from profilling.person_inn import is_person_inn_value


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("123123123123", False),
    ("399522182210", True),
    ("838112750737", True),
    ("878862122545", True)
])


def param_test(request):
    return request.param


def test_person_inn_value(param_test):
    (input, expected_output) = param_test
    result = is_person_inn_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
