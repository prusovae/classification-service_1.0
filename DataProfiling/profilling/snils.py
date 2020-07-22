import re


## Функция проверки контрольного разряда
def check_snils(snils):
    def snils_csum(snils):
        k = range(9, 0, -1)
        pairs = zip(k, [int(x) for x in snils[:-2]])
        return sum([k * v for k, v in pairs])

    snils = snils.replace('-', '')
    if not snils.isdigit() or len(snils) != 11:
        return False
    csum = snils_csum(snils)
    while csum > 101:
        csum %= 101
    csum = 0 if csum in (100, 101) else csum
    return True if csum == int(snils[-2:]) else False


## Функция для получения совпадения по метаданным
def md_pattern_snils(fld_name=None):
    ## Паттерн по метаданным
    meta_pattern = '.*(strah|snils|pension|insurance).*'
    return True if fld_name and re.findall(meta_pattern, fld_name.lower()) else False


## Функция токенизации
def tokenize_snils(value=None):
    return [re.sub('\\s|-', '', match_value) for match_value in re.findall(
        '(\\b\\d\\d\\d\\s\\d\\d\\d\\s\\d\\d\\d\\s\\d\\d\\b|\\b\\d\\d\\d-\\d\\d\\d-\\d\\d\\d-\\d\\d\\b|'
        '\\b\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d\\d\\b)', value.lower())] if value else []


def percent_diff_snils(percent, diff):
    return 100 if percent + diff > 100 else percent + diff


## Функция проверки однотипных данных, при которых не правильно рассчитывается контрольное число ('1111111','2222222')
def bs_values_check_snils(value):
    return True if len({char for char in value}) == 1 else False


def snils(param_dict=None):
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
        ## Токенизируем входящее значение и заменяем все пробельные символы
        match_values_list = tokenize_snils(value)
        if len(match_values_list) != 0:
            for match_value in match_values_list:
                if bs_values_check_snils(match_value) is False:
                    if check_snils(match_value) is True:
                        count_match += 1
                        break
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_SNILS', 'percent': percent_diff_snils(percentage, mdata_match_percent if md_pattern_snils(
        field_name) else 0)} if percentage > min_conformance_percent else {'dmn': 'DMN_SNILS', 'percent': 0.0}

