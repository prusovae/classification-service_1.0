import pytest
from profilling.email import email


@pytest.fixture()
def test_case_email_all_none():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [None for i in range(100)]}


@pytest.fixture()
def test_case_email_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ''}


@pytest.fixture()
def test_case_email_all_empty():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': ['' for i in range(100)]}


@pytest.fixture()
def test_case_email_0_percent():
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': [str(i) for i in range(100)]}


@pytest.fixture()
def test_case_email_2_percent():
    data = [str(i) for i in range(98)]
    data.append('ae.prusov@gmail.com')
    data.append('prusov1987@gmail.com')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_email_3_percent():
    data = [str(i) for i in range(97)]
    data.append('ae.prusov@gmail.com')
    data.append('prusov1987@gmail.com')
    data.append('ae.prusov@yandex.ru')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


@pytest.fixture()
def test_case_email_3_percent_text():
    data = [str(i) for i in range(97)]
    data.append('email ae.prusov@gmail.com')
    data.append('моя почта ae.prusov@gmail.com')
    data.append('email клиента ae.prusov@gmail.com и бла бла бла')
    return {'name': 'rus',
            'size': 'field_size',
            'type': 'text',
            'data': data}


class TestCardNumber:

    def test_email_func_type(self):
        # Проверка типа возвращаемого функцией
        assert type(email({})) == bool, 'не верный тип'

    def test_email_value_none(self):
        input_data = {'name': 'rus',
                      'size': 'field_size',
                      'type': 'text',
                      'data': None}
        result = email(input_data)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_email_value_all_none(self, test_case_email_all_none):
        input_data = test_case_email_all_none
        result = email(test_case_email_all_none)
        expected_output = {'dmn': 'DMN_EMAIL', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_email_value_empty(self, test_case_email_empty):
        input_data = test_case_email_empty
        result = email(test_case_email_empty)
        expected_output = False
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_email_value_all_empty(self, test_case_email_all_empty):
        input_data = test_case_email_all_empty
        result = email(test_case_email_all_empty)
        expected_output = {'dmn': 'DMN_EMAIL', 'percent': 0.0}
        print(
            "\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
                input_data, result,
                expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_email_value_0_percent(self, test_case_email_0_percent):
        input_data = test_case_email_0_percent
        result = email(test_case_email_0_percent)
        expected_output = {'dmn': 'DMN_EMAIL', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_email_value_2_percent(self, test_case_email_2_percent):
        input_data = test_case_email_2_percent
        result = email(test_case_email_2_percent)
        expected_output = {'dmn': 'DMN_EMAIL', 'percent': 0.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_email_value_3_percent(self, test_case_email_3_percent):
        input_data = test_case_email_3_percent
        result = email(test_case_email_3_percent)
        expected_output = {'dmn': 'DMN_EMAIL', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'

    def test_email_value_3_percent_text(self, test_case_email_3_percent_text):
        input_data = test_case_email_3_percent_text
        result = email(test_case_email_3_percent_text)
        expected_output = {'dmn': 'DMN_EMAIL', 'percent': 3.0}
        print("\n(подали на вход) input_data: {0}, \n(реальность) output: {1}, \n(ожидание) expected: {2}".format(
            input_data,
            result,
            expected_output))
        assert result == expected_output, 'не совпадает %'
