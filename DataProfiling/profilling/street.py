import re
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")
street_pattern = '(?!.*(type|kind|id|code).*).*(street).*'


def street_md_pattern(field_name):
    return True if field_name and re.findall(street_pattern, field_name) else False

def is_street_value(value):
    if not value:
        return False
    clean_value = value.replace('.', ' ')
    clean_value = clean_value.replace(',', ' ')
    clean_value = clean_value.lower().replace('улица ', 'ул ')
    return True if 'ул ' in clean_value else False

def percent_diff_street(percent, diff):
    return 100 if percent + diff > 100 else round(percent + diff, 1)


def street(param_dict=None):
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
    if street_md_pattern(field_name):
        mdata_match_percent = 10.0

    for value in values_list:
        match_values = value
        if match_values:
            if is_street_value(match_values):
                count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_STREET', 'percent': percent_diff_street(percentage, mdata_match_percent)} if percentage > min_conformance_percent else {'dmn': 'DMN_STREET', 'percent': 0.0}
