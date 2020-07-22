import pytest
from profilling.org_name import org_name


@pytest.fixture()
def test_case_org_name_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_org_name_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_org_name_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_org_name_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_org_name_2_percent():
    data = [str(i) for i in range(98)]
    data.append('ЗАО Тандер')
    data.append('ПАО Сбербанк')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_org_name_3_percent():
    data = [str(i) for i in range(97)]
    data.append('ЗАО Тандер')
    data.append('ПАО Сбербанк')
    data.append('Тинькофф Банк')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_org_name_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('Компания ЗАО Тандер ололо')
    data.append('ПАО Сбербанк карта')
    data.append('карта клиента в Тинькофф Банк и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestCardNumber:

    def test_org_name_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(org_name({})) == bool, 'не верный тип'

    def test_org_name_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = org_name(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_name_value_all_none(self, test_case_org_name_all_none):
        input_data = test_case_org_name_all_none
        result = org_name(test_case_org_name_all_none)
        expected_output = {'dmn': 'DMN_ORG_NAME', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_name_value_empty(self, test_case_org_name_empty):
        input_data = test_case_org_name_empty
        result = org_name(test_case_org_name_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_name_value_all_empty(self, test_case_org_name_all_empty):
        input_data = test_case_org_name_all_empty
        result = org_name(test_case_org_name_all_empty)
        expected_output = {'dmn': 'DMN_ORG_NAME', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_name_value_0_percent(self, test_case_org_name_0_percent):
        input_data = test_case_org_name_0_percent
        result = org_name(test_case_org_name_0_percent)
        expected_output = {'dmn': 'DMN_ORG_NAME', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_name_value_2_percent(self, test_case_org_name_2_percent):
        input_data = test_case_org_name_2_percent
        result = org_name(test_case_org_name_2_percent)
        expected_output = {'dmn': 'DMN_ORG_NAME', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_name_value_3_percent(self, test_case_org_name_3_percent):
        input_data = test_case_org_name_3_percent
        result = org_name(test_case_org_name_3_percent)
        expected_output = {'dmn': 'DMN_ORG_NAME', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_org_name_value_3_percent_text(self, test_case_org_name_3_percent_text):
        input_data = test_case_org_name_3_percent_text
        result = org_name(test_case_org_name_3_percent_text)
        expected_output = {'dmn': 'DMN_ORG_NAME', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
