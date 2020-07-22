import pytest
from profilling.org_name import is_org_name_value


@pytest.fixture(scope="function", params=[
    (None, False),
    ("", False),
    ("string", False),
    (None, False),
    ("ЗАО Тандер", True),
    ("АО 'Фирма'", True),
    ("ПАО Сбербанк", True),
    ("Краснодар", False),
    ("Тинькофф Банк", True)
])


def param_test(request):
    return request.param

def test_is_org_name_value(param_test):
    (input, expected_output) = param_test
    result = is_org_name_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
