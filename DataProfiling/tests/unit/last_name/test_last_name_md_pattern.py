import pytest
from profilling.last_name import last_name_md_pattern


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("currency", False),
    ("l_name", True),
    ("lname", True),
    ("last", True),
    ("sur", True),
    ("family", True)
])


def param_test(request):
    return request.param

def test_last_name_md_pattern(param_test):
    (input, expected_output) = param_test
    result = last_name_md_pattern(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
