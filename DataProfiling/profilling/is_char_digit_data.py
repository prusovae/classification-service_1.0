import logging
logger = logging.getLogger(__name__)


def is_char_digit_data(param_dict=None):
    logger.info("модуль запустился")
    from profilling.car_num import car_num
    from profilling.vin import vin
    from profilling.url import url
    from profilling.password import password
    from profilling.house import house
    from profilling.email import email
    from profilling.ip_address import ip_address

    ## Проверка на входные значения функции
    field_name = param_dict.get("name")
    field_size = param_dict.get("size")
    field_type = param_dict.get("type")
    values_list = param_dict.get("data")
    if not field_name:
        return False
    ## Создание словаря для доменов
    dmn_dict = dict()
    ## Заполнение словаря результатами работы функций
    dmn_dict[car_num(param_dict)['dmn']] = float(car_num(param_dict)['percent'])
    dmn_dict[vin(param_dict)['dmn']] = float(vin(param_dict)['percent'])
    dmn_dict[url(param_dict)['dmn']] = float(url(param_dict)['percent'])
    dmn_dict[password(param_dict)['dmn']] = float(password(param_dict)['percent'])
    dmn_dict[house(param_dict)['dmn']] = float(house(param_dict)['percent'])
    dmn_dict[email(param_dict)['dmn']] = float(email(param_dict)['percent'])
    dmn_dict[ip_address(param_dict)['dmn']] = float(ip_address(param_dict)['percent'])

    ## Получение списка ключей доменов с максимальным процентом совпадения.
    ## Если таких ключей больше одного (процент совпадения одинаков ), то берётся тот, у которого больше ключ
    dmn_out = [key for key, value in dmn_dict.items() if value == max(dmn_dict.values())]
    if dmn_dict[max(dmn_out)] != 0.0:
        logger.info({'dmn %s': max(dmn_out), 'percent %s': dmn_dict[max(dmn_out)]})
        return {'dmn': max(dmn_out), 'percent': dmn_dict[max(dmn_out)]}
    else:
        return {'dmn': 'DMN_NO_PND', 'percent': 0.0}
