import pytest
from profilling.city import is_city_value


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("Россия", False),
    ("Пакистан", False),
    ("Москва", True),
    ("Краснодар", True)
])


def param_test(request):
    return request.param


def test_is_city_value(param_test):
    (input, expected_output) = param_test
    result = is_city_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
