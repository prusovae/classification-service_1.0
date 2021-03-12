import pytest
from DataProfiling.profilling.account_number import acct_number


@pytest.fixture()
def test_case_acct_number_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_acct_number_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_acct_number_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_acct_number_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_acct_number_2_percent():
    data = [str(i) for i in range(98)]
    data.append('40817810736824643812')
    data.append('40817810736824643812')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_acct_number_3_percent():
    data = [str(i) for i in range(97)]
    data.append('40817810736824643812')
    data.append('40817810736824643812')
    data.append('40817810736824643812')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_acct_number_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('номер счета 40817810736824643812')
    data.append('40817810736824643812 аккаунт клиента')
    data.append('аккаунт клиента 40817810736824643812 и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestAcctNumber:

    def test_acct_number_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(acct_number({})) == bool, 'не верный тип'

    def test_acct_number_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = acct_number(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_acct_number_value_all_none(self, test_case_acct_number_all_none):
        input_data = test_case_acct_number_all_none
        result = acct_number(test_case_acct_number_all_none)
        expected_output = {'dmn': 'DMN_ACCT_NUMBER', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_acct_number_value_empty(self, test_case_acct_number_empty):
        input_data = test_case_acct_number_empty
        result = acct_number(test_case_acct_number_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_acct_number_value_all_empty(self, test_case_acct_number_all_empty):
        input_data = test_case_acct_number_all_empty
        result = acct_number(test_case_acct_number_all_empty)
        expected_output = {'dmn': 'DMN_ACCT_NUMBER', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_acct_number_value_0_percent(self, test_case_acct_number_0_percent):
        input_data = test_case_acct_number_0_percent
        result = acct_number(test_case_acct_number_0_percent)
        expected_output = {'dmn': 'DMN_ACCT_NUMBER', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_acct_number_value_2_percent(self, test_case_acct_number_2_percent):
        input_data = test_case_acct_number_2_percent
        result = acct_number(test_case_acct_number_2_percent)
        expected_output = {'dmn': 'DMN_ACCT_NUMBER', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_acct_number_value_3_percent(self, test_case_acct_number_3_percent):
        input_data = test_case_acct_number_3_percent
        result = acct_number(test_case_acct_number_3_percent)
        expected_output = {'dmn': 'DMN_ACCT_NUMBER', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_acct_number_value_3_percent_text(self, test_case_acct_number_3_percent_text):
        input_data = test_case_acct_number_3_percent_text
        result = acct_number(test_case_acct_number_3_percent_text)
        expected_output = {'dmn': 'DMN_ACCT_NUMBER', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
