import pytest
from profilling.city import city


@pytest.fixture()
def test_case_city_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_city_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_city_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_city_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_city_2_percent():
    data = [str(i) for i in range(98)]
    data.append('Москва')
    data.append('Краснодар')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_city_3_percent():
    data = [str(i) for i in range(97)]
    data.append('Москва')
    data.append('Краснодар')
    data.append('Волгоград')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_city_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('номер карты Москва')
    data.append('Краснодар карта клиента')
    data.append('карта клиента Волгоград и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestCardNumber:

    def test_city_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(city({})) == bool, 'не верный тип'

    def test_city_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = city(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_city_value_all_none(self, test_case_city_all_none):
        input_data = test_case_city_all_none
        result = city(test_case_city_all_none)
        expected_output = {'dmn': 'DMN_CITY', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_city_value_empty(self, test_case_city_empty):
        input_data = test_case_city_empty
        result = city(test_case_city_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_city_value_all_empty(self, test_case_city_all_empty):
        input_data = test_case_city_all_empty
        result = city(test_case_city_all_empty)
        expected_output = {'dmn': 'DMN_CITY', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_city_value_0_percent(self, test_case_city_0_percent):
        input_data = test_case_city_0_percent
        result = city(test_case_city_0_percent)
        expected_output = {'dmn': 'DMN_CITY', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_city_value_2_percent(self, test_case_city_2_percent):
        input_data = test_case_city_2_percent
        result = city(test_case_city_2_percent)
        expected_output = {'dmn': 'DMN_CITY', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_city_value_3_percent(self, test_case_city_3_percent):
        input_data = test_case_city_3_percent
        result = city(test_case_city_3_percent)
        expected_output = {'dmn': 'DMN_CITY', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_city_value_3_percent_text(self, test_case_city_3_percent_text):
        input_data = test_case_city_3_percent_text
        result = city(test_case_city_3_percent_text)
        expected_output = {'dmn': 'DMN_CITY', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
