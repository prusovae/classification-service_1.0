import re


## Функция проверки контрольного разряда
def check_ogrn(ogrn):

    delimeter = 11 if len(ogrn) == 13 else 13
    csum = str(int(ogrn[:-1]) % delimeter % 10)
    return True if csum == ogrn[-1:] and len(ogrn) in (13, 15) else False


## Функция для получения совпадения по метаданным
def md_pattern_ogrn(fld_name):
    ## Паттерн по метаданным
    meta_pattern = '.*(ogrn).*'
    return True if fld_name and re.findall(meta_pattern, fld_name.lower()) else False


## Функция токенизации
def tokenize_ogrn(value):
    return [match_value for match_value in re.findall('\\b([\\d]{13}|[\\d]{15})\\b', value.lower())] if value else []


def percent_diff_ogrn(percent, diff):
    return 100 if percent + diff > 100 else percent + diff


## Функция проверки однотипных данных, при которых не правильно рассчитывается контрольное число ('1111111','2222222')
def bs_values_check_ogrn(value):
    return True if len({char for char in value}) == 1 else False


def ogrn(param_dict):
    ## Минимальный процент совпадения по контрольному числу
    min_conformance_percent = 2.0
    ## Базовая процентная оценка по  метаданным
    mdata_match_percent = 10.0
    ## Количество совпадений по данным
    count_match = 0

    field_name = param_dict.get('name')
    field_size = param_dict.get('size')
    field_type = param_dict.get('type')
    values_list = param_dict.get('data')
    ## Проверка на входные значения и не пустоту values_list производится в главной функции.
    for value in values_list:
        ## Токенизируем входящее значение
        match_values_list = tokenize_ogrn(value)
        if len(match_values_list) != 0:
            for match_value in match_values_list:
                if bs_values_check_ogrn(match_value) is False:
                    if check_ogrn(match_value) is True:
                        count_match += 1
                        break
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_OGRN', 'percent': percent_diff_ogrn(percentage, mdata_match_percent if md_pattern_ogrn(
        field_name) else 0)} if percentage > min_conformance_percent else {'dmn': 'DMN_OGRN', 'percent': 0.0}

