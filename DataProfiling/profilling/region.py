import re
from profilling.dict_loader import regions
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")
region_pattern = '(?!.*(kind|type|code).*).*(district|province|rayon|region|raion).*'


def region_md_pattern(field_name):
    return True if field_name and re.findall(region_pattern, field_name) else False

def is_regions_value(value):
    return True if value and [region for region in regions if region in value.lower()] else False

def percent_diff_acct_number(percent, diff):
    return 100 if percent + diff > 100 else round(percent + diff, 1)

def region(param_dict=None):
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
    if region_md_pattern(field_name):
        mdata_match_percent = 10.0

    for value in values_list:
        match_value = value
        if match_value:
            if is_regions_value(match_value):
                count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_REGION', 'percent': percent_diff_acct_number(percentage, mdata_match_percent)} \
           if percentage > min_conformance_percent \
           else {'dmn': 'DMN_REGION', 'percent': 0.0}
