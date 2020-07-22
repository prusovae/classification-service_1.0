import re


## Функция для получения совпадения по метаданным
def md_pattern_password(fld_name=None):
    ## Паттерн по метаданным
    meta_pattern = "(?!.*(categori|passage|passed|passport|count|state|status|type|invalid|match|flg|flag).*).*" \
                   "(pwd|pass|secret|security|code_?word).*"
    return True if fld_name and re.findall(meta_pattern, fld_name.lower()) else False


def percent_diff_password(percent, diff):
    return 100 if percent + diff > 100 else percent + diff


def password(param_dict=None):
    ## Базовая процентная оценка по  метаданным
    mdata_match_percent = 100.0
    ## Процент совпадения по данным
    percentage = 0.0

    field_name = param_dict.get('name')
    field_size = param_dict.get('size')
    field_type = param_dict.get('type')
    values_list = param_dict.get('data')
    
    return {'dmn': 'DMN_PASSWORD', 'percent': percent_diff_password(percentage, mdata_match_percent)} if md_pattern_password(
        field_name) else {'dmn': 'DMN_PASSWORD', 'percent': 0.0}
