import pytest
from profilling.first_name_eng import is_first_name_eng_value


@pytest.fixture(scope="function", params=[
    (None, False),
    ("", False),
    ("string", False),
    (None, False),
    ("Andrey", True),
    ("Andrey,", True),
    ("Andrey.", True),
    ("anton", True),
    ("Armenia", False)
])


def param_test(request):
    return request.param

def test_is_first_name_eng_value(param_test):
    (input, expected_output) = param_test
    result = is_first_name_eng_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
