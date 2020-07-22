import pytest
from profilling.first_name import first_name_md_pattern


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("currency", False),
    ("f_name", True),
    ("fname", True),
    ("fst", True),
    ("first", True),
    ("given", True)
])


def param_test(request):
    return request.param

def test_first_name_md_pattern(param_test):
    (input, expected_output) = param_test
    result = first_name_md_pattern(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
