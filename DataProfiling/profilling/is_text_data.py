import logging
logger = logging.getLogger(__name__)

def is_text_data(param_dict=None):
    logger.info("модуль запустился")
    import statistics
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
    from profilling.card_number import card_number
    from profilling.account_number import acct_number
    from profilling.birth_date import birth_date
    from profilling.car_num import car_num
    from profilling.card_expire_date import expire_date
    from profilling.house import house
    from profilling.ip_address import ip_address
    from profilling.kpp import kpp
    from profilling.ogrn import ogrn
    from profilling.okpo import okpo
    from profilling.org_inn import org_inn
    from profilling.org_name import org_name
    from profilling.person_inn import person_inn
    from profilling.postal_code import postal_code
    from profilling.rus_passport import rus_passport
    from profilling.snils import snils
    from profilling.vin import vin

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
    dmn_dict[url(param_dict)['dmn']] = float(url(param_dict)['percent'])
    dmn_dict[password(param_dict)['dmn']] = float(password(param_dict)['percent'])
    dmn_dict[email(param_dict)['dmn']] = float(email(param_dict)['percent'])
    dmn_dict[first_name(param_dict)['dmn']] = float(first_name(param_dict)['percent'])
    dmn_dict[middle_name(param_dict)['dmn']] = float(middle_name(param_dict)['percent'])
    dmn_dict[last_name(param_dict)['dmn']] = float(last_name(param_dict)['percent'])
    dmn_dict[first_name_eng(param_dict)['dmn']] = float(first_name_eng(param_dict)['percent'])
    dmn_dict[middle_name_eng(param_dict)['dmn']] = float(middle_name_eng(param_dict)['percent'])
    dmn_dict[last_name_eng(param_dict)['dmn']] = float(last_name_eng(param_dict)['percent'])
    dmn_dict[country(param_dict)['dmn']] = float(country(param_dict)['percent'])
    dmn_dict[region(param_dict)['dmn']] = float(region(param_dict)['percent'])
    dmn_dict[city(param_dict)['dmn']] = float(city(param_dict)['percent'])
    dmn_dict[street(param_dict)['dmn']] = float(street(param_dict)['percent'])
    dmn_dict[acct_number(param_dict)['dmn']] = float(acct_number(param_dict)['percent'])
    dmn_dict[card_number(param_dict)['dmn']] = float(card_number(param_dict)['percent'])
    dmn_dict[birth_date(param_dict)['dmn']] = float(birth_date(param_dict)['percent'])
    dmn_dict[car_num(param_dict)['dmn']] = float(car_num(param_dict)['percent'])
    dmn_dict[expire_date(param_dict)['dmn']] = float(expire_date(param_dict)['percent'])
    dmn_dict[house(param_dict)['dmn']] = float(house(param_dict)['percent'])
    dmn_dict[ip_address(param_dict)['dmn']] = float(ip_address(param_dict)['percent'])
    dmn_dict[kpp(param_dict)['dmn']] = float(kpp(param_dict)['percent'])
    dmn_dict[ogrn(param_dict)['dmn']] = float(ogrn(param_dict)['percent'])
    dmn_dict[okpo(param_dict)['dmn']] = float(okpo(param_dict)['percent'])
    dmn_dict[org_name(param_dict)['dmn']] = float(org_name(param_dict)['percent'])
    dmn_dict[org_inn(param_dict)['dmn']] = float(org_inn(param_dict)['percent'])
    dmn_dict[person_inn(param_dict)['dmn']] = float(person_inn(param_dict)['percent'])
    dmn_dict[postal_code(param_dict)['dmn']] = float(postal_code(param_dict)['percent'])
    dmn_dict[rus_passport(param_dict)['dmn']] = float(rus_passport(param_dict)['percent'])
    dmn_dict[snils(param_dict)['dmn']] = float(snils(param_dict)['percent'])
    dmn_dict[vin(param_dict)['dmn']] = float(vin(param_dict)['percent'])
    logger.debug(dmn_dict)

    # Допустимое среднеквадратическое отклоение (стандартное отклонение)
    allowable_deviation = 10

    # Функции для группировки супер-атрибутов
    def group_fio_fio_param():
        group_percent_list = (dmn_dict.get('DMN_FIRST_NAME'),
                              dmn_dict.get('DMN_PATRONYMIC'),
                              dmn_dict.get('DMN_SURNAME'))
        group_max_percent = max(group_percent_list)
        deviation = statistics.pstdev([value for value in group_percent_list if value is not None])
        return {'group_max_percent': group_max_percent, 'deviation': deviation, 'dmn_name': group_percent_list}

    def group_fio_first_last_param():
        group_percent_list = (dmn_dict.get('DMN_FIRST_NAME'),
                              dmn_dict.get('DMN_SURNAME'))
        group_max_percent = max(group_percent_list)
        deviation = statistics.pstdev([value for value in group_percent_list if value is not None])
        return {'group_max_percent': group_max_percent, 'deviation': deviation, 'dmn_name': group_percent_list}

    def group_address_street_city_param():
        group_percent_list = (dmn_dict.get('DMN_CITY'),
                              dmn_dict.get('DMN_STREET'))
        group_max_percent = max(group_percent_list)
        deviation = statistics.pstdev([value for value in group_percent_list if value is not None])
        return {'group_max_percent': group_max_percent, 'deviation': deviation, 'dmn_name': group_percent_list}

    def group_address_street_city_region_param():
        group_percent_list = (dmn_dict.get('DMN_CITY'),
                              dmn_dict.get('DMN_STREET'),
                              dmn_dict.get('DMN_REGION'))
        group_max_percent = max(group_percent_list)
        deviation = statistics.pstdev([value for value in group_percent_list if value is not None])
        return {'group_max_percent': group_max_percent, 'deviation': deviation, 'dmn_name': group_percent_list}

    def group_address_street_city_country_param():
        group_percent_list = (dmn_dict.get('DMN_CITY'),
                              dmn_dict.get('DMN_STREET'),
                              dmn_dict.get('DMN_COUNTRY'))
        group_max_percent = max(group_percent_list)
        deviation = statistics.pstdev([value for value in group_percent_list if value is not None])
        return {'group_max_percent': group_max_percent, 'deviation': deviation, 'dmn_name': group_percent_list}

    def group_address_full_param():
        group_percent_list = {'DMN_CITY': dmn_dict.get('DMN_CITY'),
                              'DMN_STREET': dmn_dict.get('DMN_STREET'),
                              'DMN_REGION': dmn_dict.get('DMN_REGION'),
                              'DMN_COUNTRY': dmn_dict.get('DMN_COUNTRY')}
        group_max_percent = max(group_percent_list.values())
        deviation = statistics.pstdev([value for value in group_percent_list.values() if value is not None])
        return {'group_max_percent': group_max_percent, 'deviation': deviation, 'dmn_name': group_percent_list}
    # Создаем список процентов совпадений, не равных 0.0
    percent_list = [value for key, value in dmn_dict.items() if value != 0.0]
    if len(percent_list) != 0:
        max_percent = max(percent_list)
        # Если в списке один домен
        if len(percent_list) == 1:
            return {'dmn': max([key for key, value in dmn_dict.items() if value == max_percent]), 'percent': max_percent}
        # Если в списке больше 2 доменов
        if len(percent_list) >= 2:
            # Если среднеквадратическое отклоение больше или равно  допустимому отклонению, то проверяем
            #  отклонения в группах супер-атрибутов. Если групповое отклонение меньше допустимого и
            #  максимальный процент совпадения находится в этой группе,то выбираем этот супер-атрибут.
            if statistics.pstdev(percent_list) >= allowable_deviation:
                if (group_fio_fio_param()['deviation'] <= allowable_deviation) and group_fio_fio_param()['group_max_percent'] == max_percent:
                    return {'dmn': 'DMN_FIO', 'percent': max_percent}
                if (group_fio_first_last_param()['deviation'] <= allowable_deviation) and group_fio_first_last_param()['group_max_percent'] == max_percent:
                    return {'dmn': 'DMN_FIO', 'percent': max_percent}
                if (group_address_full_param()['deviation'] <= allowable_deviation) and group_address_full_param()['group_max_percent'] == max_percent:
                    return {'dmn': 'DMN_ADDRESS', 'percent': max_percent}
                if (group_address_street_city_country_param()['deviation'] <= allowable_deviation) and group_address_street_city_country_param()['group_max_percent'] == max_percent:
                    return {'dmn': 'DMN_ADDRESS', 'percent': max_percent}
                if (group_address_street_city_region_param()['deviation'] <= allowable_deviation) and group_address_street_city_region_param()['group_max_percent'] == max_percent:
                    return {'dmn': 'DMN_ADDRESS', 'percent': max_percent}
                if (group_address_street_city_param()['deviation'] <= allowable_deviation) and group_address_street_city_param()['group_max_percent'] == max_percent:
                    return {'dmn': 'DMN_ADDRESS', 'percent': max_percent}
                # Если предыдущие условия не выполняются, то выбирается домен с максимальным %  совпадения
                return {'dmn': max([key for key, value in dmn_dict.items() if value == max_percent]), 'percent': max_percent}
            else:
                # Если среднеквадратическое отклоение меньше  допустимого отклонения, то проверяем нет ли супер-атрибута
                if (group_fio_fio_param()['deviation'] <= allowable_deviation) and group_fio_fio_param()['group_max_percent'] == max_percent:
                    if len(group_fio_fio_param()['dmn_name']) == len(percent_list):
                        return {'dmn': 'DMN_FIO', 'percent': max_percent}
                if (group_fio_first_last_param()['deviation'] <= allowable_deviation) and group_fio_first_last_param()['group_max_percent'] == max_percent:
                    if len(group_fio_first_last_param()['dmn_name']) == len(percent_list):
                        return {'dmn': 'DMN_FIO', 'percent': max_percent}
                if (group_address_full_param()['deviation'] <= allowable_deviation) and group_address_full_param()['group_max_percent'] == max_percent:
                    if len(group_address_full_param()['dmn_name']) == len(percent_list):
                        return {'dmn': 'DMN_ADDRESS', 'percent': max_percent}
                if (group_address_street_city_country_param()['deviation'] <= allowable_deviation) and group_address_street_city_country_param()['group_max_percent'] == max_percent:
                    if len(group_address_street_city_country_param()['dmn_name']) == len(percent_list):
                        return {'dmn': 'DMN_ADDRESS', 'percent': max_percent}
                if (group_address_street_city_region_param()['deviation'] <= allowable_deviation) and group_address_street_city_region_param()['group_max_percent'] == max_percent:
                    if len(group_address_street_city_region_param()['dmn_name']) == len(percent_list):
                        return {'dmn': 'DMN_ADDRESS', 'percent': max_percent}
                if (group_address_street_city_param()['deviation'] <= allowable_deviation) and group_address_street_city_param()['group_max_percent'] == max_percent:
                    if len(group_address_street_city_param()['dmn_name']) == len(percent_list):
                        return {'dmn': 'DMN_ADDRESS', 'percent': max_percent}
                # Если не нашли супер атрибут, то DMN_COMMENT
                return {'dmn': 'DMN_COMPLEX', 'percent': max(percent_list)}
    else:
        return {'dmn': 'NO_PND', 'percent': 0.0}
#todo Если нет совпадений, сейчас возвращается None, исправить на DMN_NO_PND
#todo Заменить 100500 return'ов на (result =) в конце один return result