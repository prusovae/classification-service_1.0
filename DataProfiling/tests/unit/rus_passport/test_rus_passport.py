import pytest
from profilling.rus_passport import rus_passport


@pytest.fixture()
def test_case_rus_passport_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_rus_passport_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_rus_passport_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_rus_passport_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_rus_passport_2_percent():
    data = [str(i) for i in range(98)]
    data.append('0307 739866')
    data.append('03 07 739866')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_rus_passport_3_percent():
    data = [str(i) for i in range(97)]
    data.append('0307 739866')
    data.append('03 07 739866')
    data.append('0101 654456')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_rus_passport_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('паспорт 0307 739866')
    data.append('03 07 739866 паспорт')
    data.append('паспорт клиента 0101 654456 и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestCardNumber:

    def test_rus_passport_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(rus_passport({})) == bool, 'не верный тип'

    def test_rus_passport_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = rus_passport(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_rus_passport_value_all_none(self, test_case_rus_passport_all_none):
        input_data = test_case_rus_passport_all_none
        result = rus_passport(test_case_rus_passport_all_none)
        expected_output = {'dmn': 'DMN_RUS_PASSPORT', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_rus_passport_value_empty(self, test_case_rus_passport_empty):
        input_data = test_case_rus_passport_empty
        result = rus_passport(test_case_rus_passport_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_rus_passport_value_all_empty(self, test_case_rus_passport_all_empty):
        input_data = test_case_rus_passport_all_empty
        result = rus_passport(test_case_rus_passport_all_empty)
        expected_output = {'dmn': 'DMN_RUS_PASSPORT', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_rus_passport_value_0_percent(self, test_case_rus_passport_0_percent):
        input_data = test_case_rus_passport_0_percent
        result = rus_passport(test_case_rus_passport_0_percent)
        expected_output = {'dmn': 'DMN_RUS_PASSPORT', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_rus_passport_value_2_percent(self, test_case_rus_passport_2_percent):
        input_data = test_case_rus_passport_2_percent
        result = rus_passport(test_case_rus_passport_2_percent)
        expected_output = {'dmn': 'DMN_RUS_PASSPORT', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_rus_passport_value_3_percent(self, test_case_rus_passport_3_percent):
        input_data = test_case_rus_passport_3_percent
        result = rus_passport(test_case_rus_passport_3_percent)
        expected_output = {'dmn': 'DMN_RUS_PASSPORT', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_rus_passport_value_3_percent_text(self, test_case_rus_passport_3_percent_text):
        input_data = test_case_rus_passport_3_percent_text
        result = rus_passport(test_case_rus_passport_3_percent_text)
        expected_output = {'dmn': 'DMN_RUS_PASSPORT', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
