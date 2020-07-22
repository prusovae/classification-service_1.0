import pytest
from profilling.middle_name import is_middle_name_value


@pytest.fixture(scope="function", params=[
    (None, False),
    ("", False),
    ("string", False),
    (None, False),
    ("Евгениевич", True),
    ("Сергеевич", True),
    ("Конь", False)
])


def param_test(request):
    return request.param

def test_is_middle_name_value(param_test):
    (input, expected_output) = param_test
    result = is_middle_name_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
