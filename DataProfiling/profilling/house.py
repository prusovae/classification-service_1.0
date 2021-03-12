import re

def md_pattern_house(fld_name=None):
    meta_pattern = "(?!.*(count|blocked|id|officer|reason|type|date|size|time).*).*" \
                   "(bld|home|house|build|flat|apartm|korp|room|block|office|residence|kvartira).*"
    return True if fld_name and re.findall(meta_pattern, fld_name.lower()) \
        else False

def percent_diff_house(percent, diff):
    return 100 if percent + diff > 100 else percent + diff


def house(param_dict=None):
    mdata_match_percent = 100.0
    percentage = 0.0
    field_name = param_dict.get('name')
    field_size = param_dict.get('size')
    field_type = param_dict.get('type')
    values_list = param_dict.get('data')
    return {'dmn': 'DMN_HOUSE', 'percent':
        percent_diff_house(percentage, mdata_match_percent)} \
        if md_pattern_house(field_name) \
        else {'dmn': 'DMN_HOUSE', 'percent': 0.0}
