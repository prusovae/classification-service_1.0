import re
from profilling.dict_loader import middle_names_eng
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")
middle_names_eng_pattern = '(?!.*(exposure|insurance|uid|token|pk|full|date|time|logical|vers|state|status|collection|tpl_n|ts|process|amount|period|summ|count|run|dll_n|tooln|measur|start|end).*).*(m_name|mname|middle|mid).*'


def middle_name_eng_md_pattern(field_name):
    return True if field_name and re.findall(middle_names_eng_pattern, field_name) else False

def is_middle_name_eng_value(value):
    if not value:
        return False
    value = value.replace(',', '')
    value = value.replace('.', '')
    value = value.lower().split()
    return True if value and [value for value in value if value in middle_names_eng] else False


def percent_diff_first_name(percent, diff):
    return 100 if percent + diff > 100 else round(percent + diff, 1)

def middle_name_eng(param_dict=None):
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
    if middle_name_eng_md_pattern(field_name):
        mdata_match_percent = 10.0

    for match_values_list in values_list:
        if match_values_list:
            if is_middle_name_eng_value(match_values_list):
                count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_PATRONYMIC', 'percent': percent_diff_first_name(percentage, mdata_match_percent)} \
        if percentage > min_conformance_percent else {'dmn': 'DMN_PATRONYMIC', 'percent': 0.0}
