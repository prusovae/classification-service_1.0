import re

## Функция для получения совпадения по метаданным
def md_pattern_ip_address(fld_name=None):
    ## Паттерн по метаданным
    meta_pattern = '(?!.*(multip|key|flag|flg|requisite|monet|cost|price|descript|cipa|cipi|type|date|time|' \
                   'tip|script|state|status|guid|pk|zip|ship|vip|count).*).*(remote_addr|ip|url|net|mac|tcp|' \
                   'host|node|connect|server|site|web|www|link|ftp).*'
    return True if fld_name and re.findall(meta_pattern, fld_name.lower()) \
        else False


## Функция токенизации
def tokenize_ip_address(value=None):
    return [match_value for match_value in re.findall(
        '(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.'
        '(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.'
        '(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.'
        '(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])'
        , value.lower())] if value else []

def percent_diff_ip_address(percent, diff):
    return 100 if percent + diff > 100 else percent + diff


def ip_address(param_dict=None):
    ## Минимальный процент совпадения по контрольному числу
    min_conformance_percent = 2.0
    ## Базовая процентная оценка по  метаданным
    mdata_match_percent = 25.0
    ## Количество совпадений по данным
    count_match = 0

    ## Проверка на входные значения функции
    field_name = param_dict.get('name')
    field_size = param_dict.get('size')
    field_type = param_dict.get('type')
    values_list = param_dict.get('data')
    for value in values_list:
        ## Токенизируем входящее значение и заменяем все пробельные символы
        match_values_list = tokenize_ip_address(value)
        if len(match_values_list) != 0:
            count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_IP_ADDRESS', 'percent':
        percent_diff_ip_address(percentage, mdata_match_percent
        if md_pattern_ip_address(
        field_name) else 0)} \
        if percentage > min_conformance_percent \
        else {'dmn': 'DMN_IP_ADDRESS', 'percent': 0.0}
