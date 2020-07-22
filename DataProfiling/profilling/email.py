import re
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")
email_value_pattern = '\A[a-z0-9!#$%&*+/=?^_‘{|}~-]+(?:\.[a-z0-9!#$%&*+/=?^_‘{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?'
email_pattern = '.*(email).*'


def email_md_pattern(field_name):
    return True if field_name and re.findall(email_pattern, field_name) else False

def is_email_value(value):
    return True if value and [value for value in value.split(' ') if re.findall(email_value_pattern, value)] else False

def percent_diff_email(percent, diff):
    return 100 if percent + diff > 100 else round(percent + diff, 1)

def email(param_dict=None):
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
    if email_md_pattern(field_name):
        mdata_match_percent = 10.0

    for match_values_list in values_list:
            if match_values_list:
                if is_email_value(match_values_list):
                    count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_EMAIL', 'percent': percent_diff_email(percentage, mdata_match_percent)} if percentage > min_conformance_percent else {'dmn': 'DMN_EMAIL', 'percent': 0.0}
