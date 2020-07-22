import re


## Функция проверки контрольного разряда
def check_okpo(okpo):
    def csum(stat_req, step=0):
        pairs = [(i, int(x)) for i, x in
                 (list(enumerate(stat_req[:10 - step], 1 + step)) + list(enumerate(stat_req[10 - step:], 1)))]
        return sum([k * v for k, v in pairs[:-1]])
    if not okpo.isdigit() or len(okpo) not in (8, 10):
        return False
    cval = csum(okpo) % 11
    cval = csum(okpo, step=2) % 11 if cval == 10 else cval
    cval = 0 if cval == 10 else cval
    return True if cval == int(okpo[-1]) else False


## Функция для получения совпадения по метаданным
def md_pattern_okpo(fld_name=None):
    ## Паттерн по метаданным
    meta_pattern = '.*(okpo).*'
    return True if fld_name and re.findall(meta_pattern, fld_name.lower()) else False


## Функция токенизации
def tokenize_okpo(value=None):
    return [match_value for match_value in re.findall('\\b([\\d]{8}|[\\d]{10})\\b', value.lower())] if value else []


def percent_diff_okpo(percent, diff):
    return 100 if percent + diff > 100 else percent + diff


## Функция проверки однотипных данных, при которых не правильно рассчитывается контрольное число ('1111111','2222222')
def bs_values_check_okpo(value):
    return True if len({char for char in value}) == 1 else False


def okpo(param_dict=None):
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
        match_values_list = tokenize_okpo(value)
        if len(match_values_list) != 0:
            for match_value in match_values_list:
                if bs_values_check_okpo(match_value) is False:
                    if check_okpo(match_value) is True:
                        count_match += 1
                        break
    percentage = round((count_match * 100) / len(values_list), 1)
    return {'dmn': 'DMN_OKPO', 'percent': percent_diff_okpo(percentage, mdata_match_percent if md_pattern_okpo(
        field_name) else 0)} if percentage > min_conformance_percent else {'dmn': 'DMN_OKPO', 'percent': 0.0}
