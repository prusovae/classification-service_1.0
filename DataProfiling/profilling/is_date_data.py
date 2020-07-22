import logging
logger = logging.getLogger(__name__)

def is_date_data(param_dict=None):
    logger.info("модуль запустился")
    from profilling.birth_date import birth_date
    from profilling.card_expire_date import expire_date
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
    dmn_dict[birth_date(param_dict)['dmn']] = float(birth_date(param_dict)['percent'])
    dmn_dict[expire_date(param_dict)['dmn']] = float(expire_date(param_dict)['percent'])
    ## Получение списка ключей доменов с максимальным процентом совпадения.
    ## Если таких ключей больше одного (процент совпадения одинаков ), то берётся тот, у которого больше ключ
    dmn_out = [key for key, value in dmn_dict.items() if value == max(dmn_dict.values())]
    if dmn_dict[max(dmn_out)] != 0.0:
        logger.info({'dmn': max(dmn_out), 'percent': dmn_dict[max(dmn_out)]})
        return {'dmn': max(dmn_out), 'percent': dmn_dict[max(dmn_out)]}
    else:
        return {'dmn': 'DMN_NO_PND', 'percent': 0.0}
