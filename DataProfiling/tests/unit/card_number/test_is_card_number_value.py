import pytest
from profilling.card_number import is_card_number_value


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("0000000000000000", False),
    ("1111111111111111", False),
    ("2222222222222222", False),
    ("3333333333333333", False),
    ("4444444444444444", False),
    ("5555555555555555", False),
    ("6666666666666666", False),
    ("7777777777777777", False),
    ("8888888888888888", False),
    ("9999999999999999", False),
    ("0000000000000000", False),
    ("521324774146355", False),
    ("52132477414635571", False),
    ("5213247741463557", True),
    ("0213247741463557", False)

])


def param_test(request):
    return request.param


def test_is_card_number_value(param_test):
    (input, expected_output) = param_test
    result = is_card_number_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
