import pytest
from profilling.region import region


@pytest.fixture()
def test_case_region_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_region_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_region_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_region_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_region_2_percent():
    data = [str(i) for i in range(98)]
    data.append('московская область')
    data.append('мурманская область')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_region_3_percent():
    data = [str(i) for i in range(97)]
    data.append('московская область')
    data.append('мурманская область')
    data.append('ростовская область')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_region_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('Карты московская область')
    data.append('мурманская область карта')
    data.append('карта клиента ростовская область и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestCardNumber:

    def test_region_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(region({})) == bool, 'не верный тип'

    def test_region_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = region(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_region_value_all_none(self, test_case_region_all_none):
        input_data = test_case_region_all_none
        result = region(test_case_region_all_none)
        expected_output = {'dmn': 'DMN_REGION', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_region_value_empty(self, test_case_region_empty):
        input_data = test_case_region_empty
        result = region(test_case_region_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_region_value_all_empty(self, test_case_region_all_empty):
        input_data = test_case_region_all_empty
        result = region(test_case_region_all_empty)
        expected_output = {'dmn': 'DMN_REGION', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_region_value_0_percent(self, test_case_region_0_percent):
        input_data = test_case_region_0_percent
        result = region(test_case_region_0_percent)
        expected_output = {'dmn': 'DMN_REGION', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_region_value_2_percent(self, test_case_region_2_percent):
        input_data = test_case_region_2_percent
        result = region(test_case_region_2_percent)
        expected_output = {'dmn': 'DMN_REGION', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_region_value_3_percent(self, test_case_region_3_percent):
        input_data = test_case_region_3_percent
        result = region(test_case_region_3_percent)
        expected_output = {'dmn': 'DMN_REGION', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_region_value_3_percent_text(self, test_case_region_3_percent_text):
        input_data = test_case_region_3_percent_text
        result = region(test_case_region_3_percent_text)
        expected_output = {'dmn': 'DMN_REGION', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
