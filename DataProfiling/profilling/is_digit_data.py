import logging
logger = logging.getLogger(__name__)

def is_digit_data(param_dict=None):
    logger.info("модуль запустился")
    from profilling.ogrn import ogrn
    from profilling.okpo import okpo
    from profilling.org_inn import org_inn
    from profilling.person_inn import person_inn
    from profilling.kpp import kpp
    from profilling.postal_code import postal_code
    from profilling.snils import snils
    from profilling.rus_passport import rus_passport
    from profilling.account_number import acct_number
    from profilling.card_number import card_number
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
    dmn_dict[snils(param_dict)['dmn']] = float(snils(param_dict)['percent'])
    dmn_dict[ogrn(param_dict)['dmn']] = float(ogrn(param_dict)['percent'])
    dmn_dict[okpo(param_dict)['dmn']] = float(okpo(param_dict)['percent'])
    dmn_dict[org_inn(param_dict)['dmn']] = float(org_inn(param_dict)['percent'])
    dmn_dict[person_inn(param_dict)['dmn']] = float(person_inn(param_dict)['percent'])
    dmn_dict[kpp(param_dict)['dmn']] = float(kpp(param_dict)['percent'])
    dmn_dict[postal_code(param_dict)['dmn']] = float(postal_code(param_dict)['percent'])
    dmn_dict[rus_passport(param_dict)['dmn']] = float(rus_passport(param_dict)['percent'])
    dmn_dict[acct_number(param_dict)['dmn']] = float(acct_number(param_dict)['percent'])
    dmn_dict[card_number(param_dict)['dmn']] = float(card_number(param_dict)['percent'])
    dmn_dict[ip_address(param_dict)['dmn']] = float(ip_address(param_dict)['percent'])


    ## Получение списка ключей доменов с максимальным процентом совпадения.
    ## Если таких ключей больше одного (процент совпадения одинаков ), то берётся тот, у которого больше ключ
    dmn_out = [key for key, value in dmn_dict.items() if value == max(dmn_dict.values())]
    if dmn_dict[max(dmn_out)] != 0.0:
        logger.info({'dmn': max(dmn_out), 'percent': dmn_dict[max(dmn_out)]})
        return {'dmn': max(dmn_out), 'percent': dmn_dict[max(dmn_out)]}
    else:
        return {'dmn': 'DMN_NO_PND', 'percent': 0.0}
