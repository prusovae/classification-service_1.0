import re
from profilling.dict_loader import currency_codes, acct_charts
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")

acct_number_meta = '(?!.*(accept|access|type|status|name|flg|_id|_pk|uid|mask|state|descr|amount|sum|currenc).*).*(' \
                   'cbc|acc|ksnp|avizo|pmfr|ksbr|amfr).*'


def acct_number_md_pattern(field_name):
    return True if field_name and (re.findall(acct_number_meta, field_name)) else False


def is_acct_number_value(value):
    return True if value and value.isdigit() and len(value) == 20 and value[5:8] in currency_codes \
                   and value[0:5] in acct_charts else False


## Функция токенизации
def tokenize(value=None):
    return [match_value for match_value in re.findall('\d{20}', value.lower())] if value else []


def percent_diff_acct_number(percent, diff):
    return 100 if percent + diff > 100 else round(percent + diff, 1)


def acct_number(param_dict=None):
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
    if acct_number_md_pattern(field_name):
        mdata_match_percent = 10

    for value in values_list:
        match_values_list = tokenize(value)
        if match_values_list:
            for match_values in match_values_list:
                if is_acct_number_value(match_values):
                    count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_ACCT_NUMBER', 'percent': percent_diff_acct_number(percentage, mdata_match_percent)} \
           if percentage > min_conformance_percent \
           else {'dmn': 'DMN_ACCT_NUMBER', 'percent': 0.0}

