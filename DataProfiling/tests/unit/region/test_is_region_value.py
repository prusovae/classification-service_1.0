import pytest
from profilling.region import is_regions_value


@pytest.fixture(scope="function", params=[
    (None, False),
    ("", False),
    ("string", False),
    (None, False),
    ("Московская область", True),
    ("Ростовская область", True),
    ("Москва", True),
    ("Краснодар", False)
])


def param_test(request):
    return request.param

def test_is_region_value(param_test):
    (input, expected_output) = param_test
    result = is_regions_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
