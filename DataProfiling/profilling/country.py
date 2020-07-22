import re
from profilling.dict_loader import countries
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")
country_pattern = '.*(country).*'


def countries_md_pattern(field_name):
    return True if field_name and re.findall(country_pattern, field_name) else False

def tokenize(value=None):
    return [value.replace(',', '') for value in value.split(' ')] if value else []

def is_countries_value(value):
    return True if value and value.lower() in countries else False

def percent_diff_country(percent, diff):
    return 100 if percent + diff > 100 else round(percent + diff, 1)

def country(param_dict=None):
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
    if countries_md_pattern(field_name):
        mdata_match_percent = 10.0

    for value in values_list:
        match_value_list = tokenize(value)
        if match_value_list:
            for match_value in match_value_list:
                if is_countries_value(match_value):
                    count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_COUNTRY', 'percent': percent_diff_country(percentage, mdata_match_percent)} if percentage > min_conformance_percent else {'dmn': 'DMN_COUNTRY', 'percent': 0.0}
