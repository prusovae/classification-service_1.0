import pytest
from profilling.street import street_md_pattern


@pytest.fixture(scope="function", params=[
    (None, False),
    ("district", False),
    ("province", False),
    ("rayon", False),
    ("raion", False),
    ("", False),
    ("string", False),
    ("region", False),
    ("town", False),
    ("account", False),
    ("acct", False),
    ("locality", False),
    ("settle", False),
    ("street", True)
])


def param_test(request):
    return request.param


def test_region_md_pattern(param_test):
    (input, expected_output) = param_test
    result = street_md_pattern(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
