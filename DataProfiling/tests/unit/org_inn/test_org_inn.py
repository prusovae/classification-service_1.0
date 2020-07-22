import pytest
from profilling.org_inn import org_inn


@pytest.fixture()
def test_case_org_inn_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_org_inn_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_org_inn_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_org_inn_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_org_inn_2_percent():
    data = [str(i) for i in range(98)]
    data.append('5047125766')
    data.append('1315000052')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_org_inn_3_percent():
    data = [str(i) for i in range(97)]
    data.append('5047125766')
    data.append('1315000052')
    data.append('5047155633')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_org_inn_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('инн клиента 5047125766')
    data.append('1315000052 инн клиента')
    data.append('инн клиента 5047155633 и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestAcctNumber:

    def test_org_inn_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(org_inn({})) == bool, 'не верный тип'

    def test_org_inn_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = org_inn(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_inn_value_all_none(self, test_case_org_inn_all_none):
        input_data = test_case_org_inn_all_none
        result = org_inn(test_case_org_inn_all_none)
        expected_output = {'dmn': 'DMN_ORG_INN', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_inn_value_empty(self, test_case_org_inn_empty):
        input_data = test_case_org_inn_empty
        result = org_inn(test_case_org_inn_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_inn_value_all_empty(self, test_case_org_inn_all_empty):
        input_data = test_case_org_inn_all_empty
        result = org_inn(test_case_org_inn_all_empty)
        expected_output = {'dmn': 'DMN_ORG_INN', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_inn_value_0_percent(self, test_case_org_inn_0_percent):
        input_data = test_case_org_inn_0_percent
        result = org_inn(test_case_org_inn_0_percent)
        expected_output = {'dmn': 'DMN_ORG_INN', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_inn_value_2_percent(self, test_case_org_inn_2_percent):
        input_data = test_case_org_inn_2_percent
        result = org_inn(test_case_org_inn_2_percent)
        expected_output = {'dmn': 'DMN_ORG_INN', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_inn_value_3_percent(self, test_case_org_inn_3_percent):
        input_data = test_case_org_inn_3_percent
        result = org_inn(test_case_org_inn_3_percent)
        expected_output = {'dmn': 'DMN_ORG_INN', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_inn_value_3_percent_text(self, test_case_org_inn_3_percent_text):
        input_data = test_case_org_inn_3_percent_text
        result = org_inn(test_case_org_inn_3_percent_text)
        expected_output = {'dmn': 'DMN_ORG_INN', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
