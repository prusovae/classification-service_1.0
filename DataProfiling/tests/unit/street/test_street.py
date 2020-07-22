import pytest
from profilling.street import street


@pytest.fixture()
def test_case_street_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_street_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_street_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_street_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_street_2_percent():
    data = [str(i) for i in range(98)]
    data.append('ул. московская')
    data.append('улица мурманская')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_street_3_percent():
    data = [str(i) for i in range(97)]
    data.append('ул. московская')
    data.append('улица мурманская')
    data.append('ул мурманская')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_street_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('Карты ул. московская область')
    data.append('улица мурманская область карта')
    data.append('карта клиента ул ростовская область и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestCardNumber:

    def test_street_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(street({})) == bool, 'не верный тип'

    def test_street_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = street(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_street_value_all_none(self, test_case_street_all_none):
        input_data = test_case_street_all_none
        result = street(test_case_street_all_none)
        expected_output = {'dmn': 'DMN_STREET', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_street_value_empty(self, test_case_street_empty):
        input_data = test_case_street_empty
        result = street(test_case_street_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_street_value_all_empty(self, test_case_street_all_empty):
        input_data = test_case_street_all_empty
        result = street(test_case_street_all_empty)
        expected_output = {'dmn': 'DMN_STREET', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_street_value_0_percent(self, test_case_street_0_percent):
        input_data = test_case_street_0_percent
        result = street(test_case_street_0_percent)
        expected_output = {'dmn': 'DMN_STREET', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_street_value_2_percent(self, test_case_street_2_percent):
        input_data = test_case_street_2_percent
        result = street(test_case_street_2_percent)
        expected_output = {'dmn': 'DMN_STREET', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_street_value_3_percent(self, test_case_street_3_percent):
        input_data = test_case_street_3_percent
        result = street(test_case_street_3_percent)
        expected_output = {'dmn': 'DMN_STREET', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_street_value_3_percent_text(self, test_case_street_3_percent_text):
        input_data = test_case_street_3_percent_text
        result = street(test_case_street_3_percent_text)
        expected_output = {'dmn': 'DMN_STREET', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
