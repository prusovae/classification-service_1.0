import pytest
from profilling.email import is_email_value


@pytest.fixture(scope="function", params=[
    (None, False),
    ("", False),
    ("string", False),
    (None, False),
    ("ae.prusov@gmail.com", True),
    ("prusov1987@gmail.com", True),
    ("ae.prusovgmail.com", False)
])


def param_test(request):
    return request.param

def test_is_region_value(param_test):
    (input, expected_output) = param_test
    result = is_email_value(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
