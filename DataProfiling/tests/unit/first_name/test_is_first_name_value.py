import pytest
from profilling.first_name import is_first_name_value


@pytest.fixture(scope="function", params=[
    (None, False),
    ("", False),
    ("string", False),
    (None, False),
    ("Андрей", True),
    ("Николай", True),
    ("Конь", False)
])


def param_test(request):
    return request.param

def test_is_first_name_value(param_test):
    (input, expected_output) = param_test
    result = is_first_name_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
