import pytest
from profilling.region import region_md_pattern


@pytest.fixture(scope="function", params=[
    (None, False),
    ("district", True),
    ("province", True),
    ("rayon", True),
    ("raion", True),
    ("", False),
    ("string", False),
    ("region", True),
    ("town", False),
    ("account", False),
    ("acct", False),
    ("locality", False),
    ("settle", False)
])


def param_test(request):
    return request.param


def test_region_md_pattern(param_test):
    (input, expected_output) = param_test
    result = region_md_pattern(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
