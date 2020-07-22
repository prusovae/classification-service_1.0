import pytest
from profilling.postal_code import postal_code


@pytest.fixture()
def test_case_postal_code_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_postal_code_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_postal_code_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_postal_code_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_postal_code_2_percent():
    data = [str(i) for i in range(98)]
    data.append('350089')
    data.append('108850')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_postal_code_3_percent():
    data = [str(i) for i in range(97)]
    data.append('350089')
    data.append('108850')
    data.append('108811')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_postal_code_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('индекс клиента 350089')
    data.append('108811 индекс клиента')
    data.append('индекс клиента 108850 и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestAcctNumber:

    def test_postal_code_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(postal_code({})) == bool, 'не верный тип'

    def test_postal_code_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = postal_code(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_postal_code_value_all_none(self, test_case_postal_code_all_none):
        input_data = test_case_postal_code_all_none
        result = postal_code(test_case_postal_code_all_none)
        expected_output = {'dmn': 'DMN_POSTAL_CODE', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_postal_code_value_empty(self, test_case_postal_code_empty):
        input_data = test_case_postal_code_empty
        result = postal_code(test_case_postal_code_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_postal_code_value_all_empty(self, test_case_postal_code_all_empty):
        input_data = test_case_postal_code_all_empty
        result = postal_code(test_case_postal_code_all_empty)
        expected_output = {'dmn': 'DMN_POSTAL_CODE', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_postal_code_value_0_percent(self, test_case_postal_code_0_percent):
        input_data = test_case_postal_code_0_percent
        result = postal_code(test_case_postal_code_0_percent)
        expected_output = {'dmn': 'DMN_POSTAL_CODE', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_postal_code_value_2_percent(self, test_case_postal_code_2_percent):
        input_data = test_case_postal_code_2_percent
        result = postal_code(test_case_postal_code_2_percent)
        expected_output = {'dmn': 'DMN_POSTAL_CODE', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_postal_code_value_3_percent(self, test_case_postal_code_3_percent):
        input_data = test_case_postal_code_3_percent
        result = postal_code(test_case_postal_code_3_percent)
        expected_output = {'dmn': 'DMN_POSTAL_CODE', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_postal_code_value_3_percent_text(self, test_case_postal_code_3_percent_text):
        input_data = test_case_postal_code_3_percent_text
        result = postal_code(test_case_postal_code_3_percent_text)
        expected_output = {'dmn': 'DMN_POSTAL_CODE', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
