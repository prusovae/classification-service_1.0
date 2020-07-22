import re
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")
rus_passport_pattern = '.*(passport|serial).*'


def rus_passport_md_pattern(field_name):
    return True if field_name and re.findall(rus_passport_pattern, field_name) else False

def is_rus_passport_value(value):
    pattern = '([0-9]{2}\s{1}[0-9]{2}\s{1}[0-9]{6})|([0-9]{4}\s{1}[0-9]{6})'
    return True if value and [val for val in value if re.findall(pattern, value)] else False

def percent_diff_rus_passport(percent, diff):
    return 100 if percent + diff > 100 else round(percent + diff, 1)

def rus_passport(param_dict=None):
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
    if rus_passport_md_pattern(field_name):
        mdata_match_percent = 10.0
    for value in values_list:
        match_value = value
        if match_value:
            if is_rus_passport_value(match_value):
                count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_RUS_PASSPORT', 'percent': percent_diff_rus_passport(percentage, mdata_match_percent)} \
           if percentage > min_conformance_percent \
           else {'dmn': 'DMN_RUS_PASSPORT', 'percent': 0.0}

