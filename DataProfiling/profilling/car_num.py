import re


## Функция для получения совпадения по метаданным
def md_pattern_car_num(fld_name=None):
    ## Паттерн по метаданным
    meta_pattern = '(?!card).*(car).*'
    return True if fld_name and re.findall(meta_pattern, fld_name.lower()) else False


## Функция токенизации
def tokenize_car_num(value=None):
    return [match_value for match_value in re.findall('\\b([АВЕКМНОРСТУХ]{2}\\d{3}\\d{2,3}|'
                                                      '[АВЕКМНОРСТУХ]\\d{3}[АВЕКМНОРСТУХ]{2}\\d{2,3}|'
                                                      '\\d{4}[АВЕКМНОРСТУХ]{2}\\d{2,3})\\b', value.upper())] if value else []


def percent_diff_car_num(percent, diff):
    return 100 if percent + diff > 100 else percent + diff


def car_num(param_dict=None):
    ## Минимальный процент совпадения по контрольному числу
    min_conformance_percent = 2.0
    ## Базовая процентная оценка по  метаданным
    mdata_match_percent = 15.0
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
        match_values_list = tokenize_car_num(value)
        if len(match_values_list) != 0:
            count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_CAR_NUM', 'percent': percent_diff_car_num(percentage, mdata_match_percent if md_pattern_car_num(
        field_name) else 0)} if percentage > min_conformance_percent else {'dmn': 'DMN_CAR_NUM', 'percent': 0.0}
