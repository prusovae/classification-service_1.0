import re


## Функция для получения совпадения по метаданным
def md_pattern_url(fld_name=None):
    ## Паттерн по метаданным
    meta_pattern = '(?!.*(multip|key|flag|flg|requisite|monet|cost|price|descript|cipa|cipi|type|date|time|' \
                   'tip|script|state|status|guid|pk|zip|ship|vip|count).*).*(remote_addr|ip|url|net|mac|tcp|' \
                   'host|node|connect|server|site|web|www|link|ftp).*'
    return True if fld_name and re.findall(meta_pattern, fld_name.lower()) else False


## Функция токенизации
def tokenize_url(value=None):
    return [match_value for match_value in re.findall('(https\:|http\:|ftp\:)\S*(.ru|.com)|\S*(.ru|.com)', value.lower())] if value\
        and not re.findall('@', value.lower()) else []


def percent_diff_url(percent, diff):
    return 100 if percent + diff > 100 else percent + diff


## Функция проверки однотипных данных, при которых не правильно рассчитывается контрольное число ('1111111','2222222')
def bs_values_check_url(value):
    return True if len({char for char in value}) == 1 else False


def url(param_dict=None):
    ## Минимальный процент совпадения по контрольному числу
    min_conformance_percent = 2.0
    ## Базовая процентная оценка по  метаданным
    mdata_match_percent = 15.0
    ## Количество совпадений по данным
    count_match = 0

    field_name = param_dict.get('name')
    field_size = param_dict.get('size')
    field_type = param_dict.get('type')
    values_list = param_dict.get('data')
    ## Проверка на входные значения и не пустоту values_list производится в главной функции.
    for value in values_list:
        ## Токенизируем входящее значение и заменяем все пробельные символы
        match_values_list = tokenize_url(value)
        if len(match_values_list) != 0:
            count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_URL', 'percent': percent_diff_url(percentage, mdata_match_percent if md_pattern_url(
        field_name) else 0)} if percentage > min_conformance_percent else {'dmn': 'DMN_URL', 'percent': 0.0}

