import re
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")
person_inn_pattern = '.*(inn).*'


def person_inn_md_pattern(field_name):
    return True if field_name and re.findall(person_inn_pattern, field_name.lower()) else False

def is_person_inn_value(value):
    if value and value.isdigit() and len(value) == 12:
        person_inn = list(str(value.strip(' ')))
        discharge_weighty = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
        checksum = int()
        new_string = (
        [int(x) * int(discharge_weighty) for x, discharge_weighty in zip(person_inn[:-1], discharge_weighty)])
        for i in new_string:
            checksum += i
        control_digit = checksum % 11
        check_digit = int(value[-2])
        print(control_digit)
        return control_digit % 10 == check_digit if control_digit > 9 else control_digit == check_digit
    return False

## Функция токенизации
def tokenize(value=None):
    return [match_value for match_value in re.findall('\d{12}', value.lower())] if value else []

def percent_diff_person_inn(percent, diff):
    return 100 if percent + diff > 100 else round(percent + diff, 1)

def bs_values_check_person_inn(value):
    return True if len({char for char in value}) == 1 else False

def person_inn(param_dict=None):
    """
    Тут будет docstring
    """
    count_match = 0
    min_conformance_percent = 2.0
    field_name = param_dict.get('name')
    field_size = param_dict.get('size')
    field_type = param_dict.get('type')
    values_list = param_dict.get('data')
    if not values_list:
        return False
    mdata_match_percent = 0
    if person_inn_md_pattern(field_name):
        mdata_match_percent = 10

    for value in values_list:
        match_values_list = tokenize(value)
        for match_values in match_values_list:
            if match_values_list:
                if not bs_values_check_person_inn(match_values) and is_person_inn_value(match_values):
                    count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_INN', 'percent': percent_diff_person_inn(percentage, mdata_match_percent)} \
           if percentage > min_conformance_percent \
           else {'dmn': 'DMN_INN', 'percent': 0.0}
