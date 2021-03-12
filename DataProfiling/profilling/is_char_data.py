import logging
logger = logging.getLogger(__name__)

def is_char_data(param_dict=None):
    logger.info("модуль запустился")
    from profilling.email_rule import email
    from profilling.url import url
    from profilling.password import password
    from profilling.first_name import first_name
    from profilling.middle_name import middle_name
    from profilling.last_name import last_name
    from profilling.first_name_eng import first_name_eng
    from profilling.middle_name_eng import middle_name_eng
    from profilling.last_name_eng import last_name_eng
    from profilling.country import country
    from profilling.region import region
    from profilling.city import city
    from profilling.street import street

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
    dmn_dict[first_name(param_dict)['dmn']] = float(first_name(param_dict)['percent'])
    dmn_dict[middle_name(param_dict)['dmn']] = float(middle_name(param_dict)['percent'])
    dmn_dict[last_name(param_dict)['dmn']] = float(last_name(param_dict)['percent'])
    dmn_dict[url(param_dict)['dmn']] = float(url(param_dict)['percent'])
    dmn_dict[password(param_dict)['dmn']] = float(password(param_dict)['percent'])
    dmn_dict[email(param_dict)['dmn']] = float(email(param_dict)['percent'])
    dmn_dict[country(param_dict)['dmn']] = float(country(param_dict)['percent'])
    dmn_dict[region(param_dict)['dmn']] = float(region(param_dict)['percent'])
    dmn_dict[city(param_dict)['dmn']] = float(city(param_dict)['percent'])
    dmn_dict[street(param_dict)['dmn']] = float(street(param_dict)['percent'])
    ## Получение списка ключей доменов с максимальным процентом совпадения.
    ## Если таких ключей больше одного (процент совпадения одинаков )
    # , то берётся тот, у которого больше ключ
    dmn_out = [key for key, value in dmn_dict.items() if value == max(dmn_dict.values())]
    print(dmn_dict)
    if dmn_dict[max(dmn_out)] != 0.0:
        return {'dmn': max(dmn_out), 'percent': dmn_dict[max(dmn_out)]}
    else:
        return {'dmn': 'NO_PND', 'percent': 0.0}
