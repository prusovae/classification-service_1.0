from profilling.dict_loader import postal_codes
import re
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")
postal_code_pattern = '.*(postal|zip|indeks|index|post_?code).*'


def postal_code_md_pattern(field_name):
    return True if field_name and re.findall(postal_code_pattern, field_name.lower()) else False

def is_postal_code_value(value):
    return True if value and [val for val in value.split() if val in postal_codes] else False

def percent_diff_postal_code(percent, diff):
    return 100 if percent + diff > 100 else round(percent + diff, 1)

def postal_code(param_dict=None):
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
    if postal_code_md_pattern(field_name):
        mdata_match_percent = 10

    for value in values_list:
        match_values = value
        if match_values:
            if is_postal_code_value(match_values):
                count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_POSTAL_CODE', 'percent': percent_diff_postal_code(percentage, mdata_match_percent)} \
           if percentage > min_conformance_percent \
           else {'dmn': 'DMN_POSTAL_CODE', 'percent': 0.0}
