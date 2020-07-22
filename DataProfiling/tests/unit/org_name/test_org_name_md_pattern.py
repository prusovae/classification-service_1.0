import pytest
from profilling.org_name import org_name_md_pattern


@pytest.fixture(scope="function", params=[
    (None, False),
    ("", False),
    ("string", False),
    ("investor", True),
    ("bank", True),
    ("authority", True),
    ("issuer", True),
    ("payer", True),
    ("institut", True),
    ("creditor", True),
    ("agency", True),
    ("emp_nam", True),
    ("depon", True),
    ("emitent", True),
    ("employ", True),
    ("party", True),
    ("comp", True),
    ("org", True),
    ("issue", True),
    ("who", True),
    ("legal", True),
    ("firm", True),
    ("benef", True),
    ("customer", True),
    ("where", True),
    ("custn", True),
    ("fssp_nam", True),
    ("corp_nam", True),
    ("org_name", True),
    ("town", False),
    ("account", False),
    ("acct", False),
    ("locality", False),
    ("settle", False)
])


def param_test(request):
    return request.param

def test_org_name_md_pattern(param_test):
    (input, expected_output) = param_test
    result = org_name_md_pattern(input)
    print("input: {0}, output: {1}, expected: {2}".format(input, result, expected_output))
    assert result == expected_output
