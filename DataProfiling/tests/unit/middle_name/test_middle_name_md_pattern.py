import pytest
from profilling.middle_name import middle_name_md_pattern


@pytest.fixture(scope="function", params=[
    ("", False),
    ("string", False),
    (None, False),
    ("currency", False),
    ("m_name", True),
    ("mname", True),
    ("middle", True),
    ("mid", True)
])


def param_test(request):
    return request.param

def test_middle_name_md_pattern(param_test):
    (input, expected_output) = param_test
    result = middle_name_md_pattern(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
