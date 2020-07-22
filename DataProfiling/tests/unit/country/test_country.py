import pytest
from profilling.country import country


@pytest.fixture()
def test_case_country_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_country_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_country_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_country_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_country_2_percent():
    data = [str(i) for i in range(98)]
    data.append('Россия')
    data.append('Румыния')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_country_3_percent():
    data = [str(i) for i in range(97)]
    data.append('Россия')
    data.append('Румыния')
    data.append('Сербия')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_country_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('Карты Россия')
    data.append('Румыния карта')
    data.append('карта клиента Сербия и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestCardNumber:

    def test_country_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(country({})) == bool, 'не верный тип'

    def test_country_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = country(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_country_value_all_none(self, test_case_country_all_none):
        input_data = test_case_country_all_none
        result = country(test_case_country_all_none)
        expected_output = {'dmn': 'DMN_COUNTRY', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_country_value_empty(self, test_case_country_empty):
        input_data = test_case_country_empty
        result = country(test_case_country_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_country_value_all_empty(self, test_case_country_all_empty):
        input_data = test_case_country_all_empty
        result = country(test_case_country_all_empty)
        expected_output = {'dmn': 'DMN_COUNTRY', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_country_value_0_percent(self, test_case_country_0_percent):
        input_data = test_case_country_0_percent
        result = country(test_case_country_0_percent)
        expected_output = {'dmn': 'DMN_COUNTRY', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_country_value_2_percent(self, test_case_country_2_percent):
        input_data = test_case_country_2_percent
        result = country(test_case_country_2_percent)
        expected_output = {'dmn': 'DMN_COUNTRY', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_country_value_3_percent(self, test_case_country_3_percent):
        input_data = test_case_country_3_percent
        result = country(test_case_country_3_percent)
        expected_output = {'dmn': 'DMN_COUNTRY', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_country_value_3_percent_text(self, test_case_country_3_percent_text):
        input_data = test_case_country_3_percent_text
        result = country(test_case_country_3_percent_text)
        expected_output = {'dmn': 'DMN_COUNTRY', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
