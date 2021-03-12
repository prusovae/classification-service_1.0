import re


## Функция для получения совпадения по метаданным
def md_pattern_birth_date(fld_name=None):
    ## Паттерн по метаданным
    meta_pattern = '((brth|birth)_?(date|dt|day))|(brth|birth)|((date|dt)_?o?f?_?(brth|birth))'
    return True if fld_name and re.findall(meta_pattern, fld_name.lower()) else False


## Функция токенизации
def tokenize_birth_date(value=None):
    return [match_value for match_value in re.findall(
        '\\b(\d{1,2}[-./]\d{1,2}[-./]\d{2,4})\\b|'
        '\\b(\d{2,4}[-./]\d{1,2}[-./]\d{1,2})\\b', value.lower())] if value else []


def percent_diff_birth_date(percent, diff):
    return 100 if percent + diff > 100 else percent + diff


def birth_date(param_dict=None):
    ## Минимальный процент совпадения по контрольному числу
    min_conformance_percent = 2.0
    ## Базовая процентная оценка по  метаданным
    mdata_match_percent = 35.0
    ## Количество совпадений по данным
    count_match = 0

    ## Проверка на входные значения функции
    field_name = param_dict.get('name')
    field_size = param_dict.get('size')
    field_type = param_dict.get('type')
    values_list = param_dict.get('data')
    ## Проверка на входные значения и не пустоту values_list производится в главной функции.
    for value in values_list:
        ## Токенизируем входящее значение и заменяем все пробельные символы
        match_values_list = tokenize_birth_date(value)
        if len(match_values_list) != 0:
            count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_BIRTH_DATE', 'percent':
        percent_diff_birth_date(percentage, mdata_match_percent)} \
        if md_pattern_birth_date(field_name) \
           and percentage > min_conformance_percent \
        else {'dmn': 'DMN_BIRTH_DATE', 'percent': 0.0}
