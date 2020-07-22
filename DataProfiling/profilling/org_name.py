import re
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")

org_name_prefix = ['ООО', 'ЗАО', 'ОАО', 'ПАО', 'АО', 'БАНК']
org_name_pattern = '(?!.*(day|width|num|form|kind|flag|flgdat|id|vers|type|amt|amount|stat|key|sum|date|time|count|cost|period).*)' \
                      '.*(corp_nam|fssp_nam|custn|where|customer|benef|firm|legal|who|issue|org|comp|party|employ|emitent|depon|' \
                      'emp_nam|agency|creditor|institut|payer|issuer|bank|authority|investor).*'


def org_name_md_pattern(field_name):
    return True if field_name and re.findall(org_name_pattern, field_name) else False

def is_org_name_value(value):
    return True if value and [val for val in value.split() if val.upper() in org_name_prefix] else False

def percent_diff_org_name(percent, diff):
    return 100 if percent + diff > 100 else round(percent + diff, 1)

def org_name(param_dict=None):
    count_match = 0
    min_conformance_percent = 2.0
    field_name = param_dict.get('name')
    field_size = param_dict.get('size')
    field_type = param_dict.get('type')
    values_list = param_dict.get('data')
    if not values_list:
        return False
    mdata_match_percent = 0
    if org_name_md_pattern(field_name):
        mdata_match_percent = 10

    for value in values_list:
        match_values = value
        if match_values:
            if is_org_name_value(match_values):
                count_match += 1


    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_ORG_NAME', 'percent': percent_diff_org_name(percentage, mdata_match_percent)} \
           if percentage > min_conformance_percent \
           else {'dmn': 'DMN_ORG_NAME', 'percent': 0.0}
