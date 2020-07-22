import pytest
from profilling.rus_passport import is_rus_passport_value


@pytest.fixture(scope="function", params=[
    (None, False),
    ("", False),
    ("string", False),
    (None, False),
    ("0307 739866", True),
    ("03 07 739866", True),
    ("Краснодар", False),
    ("0307739866", False),
])


def param_test(request):
    return request.param

def test_is_rus_passport_value(param_test):
    (input, expected_output) = param_test
    result = is_rus_passport_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
