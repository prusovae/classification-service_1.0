import pytest
from profilling.card_number import card_number


@pytest.fixture()
def test_case_card_number_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_card_number_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_card_number_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_card_number_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_card_number_2_percent():
    data = [str(i) for i in range(98)]
    data.append('5213247744536318')
    data.append('5213247744536318')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_card_number_3_percent():
    data = [str(i) for i in range(97)]
    data.append('5213247744536318')
    data.append('5213247744536318')
    data.append('5213247744536318')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_card_number_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('номер карты 5213247744536318')
    data.append('5213247744536318 карта клиента')
    data.append('карта клиента 5213247744536318 и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestAcctNumber:

    def test_card_number_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(card_number({})) == bool, 'не верный тип'

    def test_card_number_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = card_number(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_card_number_value_all_none(self, test_case_card_number_all_none):
        input_data = test_case_card_number_all_none
        result = card_number(test_case_card_number_all_none)
        expected_output = {'dmn': 'DMN_CARD_NUMBER', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_card_number_value_empty(self, test_case_card_number_empty):
        input_data = test_case_card_number_empty
        result = card_number(test_case_card_number_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_card_number_value_all_empty(self, test_case_card_number_all_empty):
        input_data = test_case_card_number_all_empty
        result = card_number(test_case_card_number_all_empty)
        expected_output = {'dmn': 'DMN_CARD_NUMBER', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_card_number_value_0_percent(self, test_case_card_number_0_percent):
        input_data = test_case_card_number_0_percent
        result = card_number(test_case_card_number_0_percent)
        expected_output = {'dmn': 'DMN_CARD_NUMBER', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_card_number_value_2_percent(self, test_case_card_number_2_percent):
        input_data = test_case_card_number_2_percent
        result = card_number(test_case_card_number_2_percent)
        expected_output = {'dmn': 'DMN_CARD_NUMBER', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_card_number_value_3_percent(self, test_case_card_number_3_percent):
        input_data = test_case_card_number_3_percent
        result = card_number(test_case_card_number_3_percent)
        expected_output = {'dmn': 'DMN_CARD_NUMBER', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_card_number_value_3_percent_text(self, test_case_card_number_3_percent_text):
        input_data = test_case_card_number_3_percent_text
        result = card_number(test_case_card_number_3_percent_text)
        expected_output = {'dmn': 'DMN_CARD_NUMBER', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
