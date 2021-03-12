import logging
logger = logging.getLogger(__name__)

import re
from profilling.is_digit_data import is_digit_data
from profilling.is_char_digit_data import is_char_digit_data
from profilling.is_date_data import is_date_data
from profilling.is_char_data import is_char_data
from profilling.is_text_data import is_text_data
from profilling.dict_loader import data_types_map


def master_route_func(param_dict=None):
    logger.info("модуль запустился")
    field_name = param_dict.get("name")
    field_size = param_dict.get("size")
    field_type = param_dict.get("type")
    values_list = param_dict.get("data")
    logger.debug("falsk send this request --> %s", param_dict)
    if not field_name:
        return False


    def is_digit(values_list):
        digit_counter = 0
        counter = 0
        for value in values_list:
            counter += 1
            for junk_char in "#%$@ *.!&/": value = value.replace(junk_char, '')
            if value.isdigit():
                digit_counter += 1
        result = round(digit_counter / counter * 100)
        logger.debug('is_digit result = %s', result)
        if result > 90:
            return True
        return False

    def is_date(values_list):
        pattern_date = '(^\d{1,2}[-./]\d{1,2}[-./]\d{2,4}$)|' \
                       '(^\d{2,4}[-./]\d{1,2}[-./]\d{1,2}$)|' \
                       '(^\d{1,2}[/]\d{2}$)|(^\d{1,2}[/]\d{4}$)'
        date_counter = 0
        value_counter = 0
        for value in values_list:
            value_counter += 1
            if bool(re.findall(pattern_date, value.lower().strip()))  == True:
                date_counter += 1
        result = round(date_counter / value_counter * 100)
        logger.debug('is_date result = %s', result)
        if result > 50:
            return True
        return False

    def is_text(values_list):
        for value in values_list:
            if len(value.split()) > 1:
                return True
        logger.debug('is_text result = text detected')
        return False

    def is_char(values_list):
        counter = 0
        char_counter = 0
        for value in values_list:
            counter = counter + 1 if value else counter
            for junk_char in "#%$@- *.!&/": value = value.replace(junk_char, '')
            if value.isalpha():
                char_counter += 1
        result = round((char_counter / counter) * 100)
        logger.debug('is_char result = %s', result)
        if result > 90:
            return True

    field_type = (lambda data_type: data_types_map.get(data_type.upper(), 'UNKNOWN'))(field_type)
    if field_type == 'UNKNOWN':
        result = {'dmn': 'NO_PND', 'percent': 0.0}
    if field_type == 'BINARY':
        result = {'dmn': 'DMN_BINARY', 'percent': 100.0}
    if field_type == 'DATE':
        result = is_date_data(param_dict)
    if field_type == 'STRING' or 'NUMBER':
        if is_date(values_list):
            result = (is_date_data(param_dict))
        else:
            if is_digit(values_list):
                result = (is_digit_data(param_dict))
            else:
                if is_text(values_list):
                    result = (is_text_data(param_dict))
                else:
                    if is_char(values_list):
                        result = (is_char_data(param_dict))
                    else:
                        result = (is_char_digit_data(param_dict))
    logger.info("result = %s", result)
    return result
