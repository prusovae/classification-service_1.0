import pytest
from profilling.rus_passport import rus_passport_md_pattern


@pytest.fixture(scope="function", params=[
    (None, False),
    ("", False),
    ("string", False),
    ("rus_passport", True),
    ("passport", True),
    ("serial", True),
    ("town", False),
    ("account", False),
    ("acct", False),
    ("locality", False),
    ("settle", False)
])


def param_test(request):
    return request.param


def test_rus_passport_md_pattern(param_test):
    (input, expected_output) = param_test
    result = rus_passport_md_pattern(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
