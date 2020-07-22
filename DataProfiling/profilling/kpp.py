import re


## Функция для получения совпадения по метаданным
def md_pattern_kpp(fld_name=None):
    ## Паттерн по метаданным
    meta_pattern = '.*(cpp|kpp).*'
    return True if fld_name and re.findall(meta_pattern, fld_name.lower()) else False


## Функция токенизации
def tokenize_kpp(value=None):
    return [match_value for match_value in re.findall('\\b(\\d{4}01001|\\d{4}43002)\\b', value.lower())] if value else []


def percent_diff_kpp(percent, diff):
    return 100 if percent + diff > 100 else percent + diff


def kpp(param_dict=None):
    ## Минимальный процент совпадения по контрольному числу
    min_conformance_percent = 2.0
    ## Базовая процентная оценка по  метаданным
    mdata_match_percent = 50.0
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
        match_values_list = tokenize_kpp(value)
        if len(match_values_list) != 0:
            count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_KPP', 'percent': percent_diff_kpp(percentage, mdata_match_percent if md_pattern_kpp(
        field_name) else 0)} if percentage > min_conformance_percent else {'dmn': 'DMN_KPP', 'percent': 0.0}
