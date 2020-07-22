import re
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")
card_number_pattern = '(?!.*(rowspan|colspan|index|limit|sum|flg|flag|company|type|cardinal|participan|holder' \
                      '|count|panel|status|issue|name|level|date|kind|score|length|expire).*).*(card|pan).*'


def card_number_md_pattern(field_name):
    return True if field_name and re.findall(card_number_pattern, field_name) else False


def tokenize(value=None):
    return [match_value for match_value in re.findall('\d{16}', value.lower())] if value else []


def is_card_number_value(value):
    lunh_odd_lookup = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    if value:
        card = value.replace('-', '')
        if not card or not card.isdigit() or (card.isdigit() and not len(card) in (16, 18)):
            return False
        else:
            evens = sum(int(p) for p in card[-1::-2])
            odds = sum(lunh_odd_lookup[int(p)] for p in card[-2::-2])
            return True if (evens + odds) % 10 == 0 and bs_values_check(card) else False
    return False

def percent_diff_acct_number(percent, diff):
    return 100 if percent + diff > 100 else round(percent + diff, 1)


def bs_values_check(value):
    return False if len(set([char for char in value])) == 1 else True


def card_number(param_dict=None):
    """
    Тут будет docstring
    """
    count_match = 0
    min_conformance_percent = 2.0
    # Проверка на входные значения функции
    field_name = param_dict.get('name')
    field_size = param_dict.get('size')
    field_type = param_dict.get('type')
    values_list = param_dict.get('data')
    if not values_list:
        return False
    mdata_match_percent = 0
    if card_number_md_pattern(field_name):
        mdata_match_percent = 10.0

    for value in values_list:
        match_values_list = tokenize(value)
        if match_values_list:
            for match_values in match_values_list:
                if is_card_number_value(match_values):
                    count_match += 1
    percentage = round((count_match * 100) / len(values_list), 1)

    return {'dmn': 'DMN_CARD_NUMBER', 'percent': percent_diff_acct_number(percentage, mdata_match_percent)} \
        if percentage > min_conformance_percent \
        else {'dmn': 'DMN_CARD_NUMBER', 'percent': 0.0}


