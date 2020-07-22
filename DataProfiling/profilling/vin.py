import re


## Функция проверки контрольного разряда
def check_vin(vin):
    positional_weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    illegal_all = ['I', 'O', 'Q']
    letter_key = dict(
        A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8,
        J=1, K=2, L=3, M=4, N=5, P=7, R=9,
        S=2, T=3, U=4, V=5, W=6, X=7, Y=8, Z=9)
    if [char for char in illegal_all if char in vin]:
        return False
    check_digit = vin[8]
    pos = sum = 0
    for char in vin:
        value = int(letter_key[char]) if char in letter_key else int(char)
        weight = positional_weights[pos]
        sum += (value * weight)
        pos += 1
    calc_check_digit = int(sum) % 11
    calc_check_digit = 'X' if calc_check_digit == 10 else calc_check_digit
    return True if str(check_digit) == str(calc_check_digit) else False


## Функция для получения совпадения по метаданным
def md_pattern_vin(fld_name=None):
    ## Паттерн по метаданным
    meta_pattern = '.*(vin).*'
    return True if fld_name and re.findall(meta_pattern, fld_name.lower()) else False


## Функция токенизации
def tokenize_vin(value=None):
    return [re.sub('\\s|-', '', match_value) for match_value in re.findall(
        '\\b([A-HJ-NPR-Z\d]{13}\d{4})\\b', value.upper())] if value else []


def percent_diff_vin(percent, diff):
    return 100 if percent + diff > 100 else percent + diff


## Функция проверки однотипных данных, при которых не правильно рассчитывается контрольное число ('1111111','2222222')
def bs_values_check_vin(value):
    return True if len({char for char in value}) == 1 else False


def vin(param_dict=None):
    ## Минимальный процент совпадения по контрольному числу
    min_conformance_percent = 2.0
    ## Базовая процентная оценка по  метаданным
    mdata_match_percent = 10.0
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
        match_values_list = tokenize_vin(value)
        if len(match_values_list) != 0:
            for match_value in match_values_list:
                if bs_values_check_vin(match_value) is False:
                    if check_vin(match_value) is True:
                        count_match += 1
                        break
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_VIN', 'percent': percent_diff_vin(percentage, mdata_match_percent if md_pattern_vin(
        field_name) else 0)} if percentage > min_conformance_percent else {'dmn': 'DMN_VIN', 'percent': 0.0}
