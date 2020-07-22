import pytest
from profilling.country import is_countries_value


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("Россия", True),
    ("Пакистан", True),
    ("Москва", False),
    ("Краснодар", False)
])


def param_test(request):
    return request.param


def test_is_country_value(param_test):
    (input, expected_output) = param_test
    result = is_countries_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
