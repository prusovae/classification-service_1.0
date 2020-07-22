import pytest
from profilling.middle_name_eng import middle_name_eng


@pytest.fixture()
def test_case_middle_name_eng_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_middle_name_eng_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_middle_name_eng_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_middle_name_eng_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_middle_name_eng_2_percent():
    data = [str(i) for i in range(98)]
    data.append('Evgenievich')
    data.append('Sergeevich')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_middle_name_eng_3_percent():
    data = [str(i) for i in range(97)]
    data.append('Evgenievich')
    data.append('Sergeevich')
    data.append('Ivanovich')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_middle_name_eng_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('middle_name_eng Evgenievich')
    data.append('Фамилия клиента Sergeevich')
    data.append('Фамилия клиента Ivanovich и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestCardNumber:

    def test_middle_name_eng_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(middle_name_eng({})) == bool, 'не верный тип'

    def test_middle_name_eng_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = middle_name_eng(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_middle_name_eng_value_all_none(self, test_case_middle_name_eng_all_none):
        input_data = test_case_middle_name_eng_all_none
        result = middle_name_eng(test_case_middle_name_eng_all_none)
        expected_output = {'dmn': 'DMN_MIDDLE_NAME_ENG', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_middle_name_eng_value_empty(self, test_case_middle_name_eng_empty):
        input_data = test_case_middle_name_eng_empty
        result = middle_name_eng(test_case_middle_name_eng_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_middle_name_eng_value_all_empty(self, test_case_middle_name_eng_all_empty):
        input_data = test_case_middle_name_eng_all_empty
        result = middle_name_eng(test_case_middle_name_eng_all_empty)
        expected_output = {'dmn': 'DMN_MIDDLE_NAME_ENG', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_middle_name_eng_value_0_percent(self, test_case_middle_name_eng_0_percent):
        input_data = test_case_middle_name_eng_0_percent
        result = middle_name_eng(test_case_middle_name_eng_0_percent)
        expected_output = {'dmn': 'DMN_MIDDLE_NAME_ENG', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_middle_name_eng_value_2_percent(self, test_case_middle_name_eng_2_percent):
        input_data = test_case_middle_name_eng_2_percent
        result = middle_name_eng(test_case_middle_name_eng_2_percent)
        expected_output = {'dmn': 'DMN_MIDDLE_NAME_ENG', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_middle_name_eng_value_3_percent(self, test_case_middle_name_eng_3_percent):
        input_data = test_case_middle_name_eng_3_percent
        result = middle_name_eng(test_case_middle_name_eng_3_percent)
        expected_output = {'dmn': 'DMN_MIDDLE_NAME_ENG', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_middle_name_eng_value_3_percent_text(self, test_case_middle_name_eng_3_percent_text):
        input_data = test_case_middle_name_eng_3_percent_text
        result = middle_name_eng(test_case_middle_name_eng_3_percent_text)
        expected_output = {'dmn': 'DMN_MIDDLE_NAME_ENG', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
