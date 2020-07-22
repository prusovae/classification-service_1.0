import logging
logger = logging.getLogger(__name__)

import re
from profilling.is_digit_data import is_digit_data
from profilling.is_char_digit_data import is_char_digit_data
from profilling.is_date_data import is_date_data
from profilling.is_char_data import is_char_data
from profilling.is_text_data import is_text_data




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
            counter+=1
            for junk_char in "#%$@ *.!&/": value = value.replace(junk_char, '')
            if value.isdigit():
                digit_counter+=1
        result = round(digit_counter / counter * 100)
        logger.debug('is_digit result = %s', result)
        if result > 90:
            return True
        return False


    def is_date(values_list):
        pattern_date = '\\b(\d{1,2}[-./]\d{1,2}[-./]\d{2,4})|(\d{2,4}[-./]\d{1,2}[-./]\d{1,2})\\b'
        date_counter = 0
        value_counter = 0
        for value in values_list:
            value_counter+=1
            if bool(re.findall(pattern_date, value.lower()))  == True:
                date_counter+=1
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


    if field_type == 'int':
        result = {'dmn': 'DMN_NO_PND', 'percent': 0.0}
    if field_type == 'date':
        result = is_date_data(param_dict)
    if field_type == 'text':
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



dict__ ={
    "name": "ff",
    "size": "field_size",
    "type": "text",
    "data": ["127.0.0.1","127.0.0.1","10.106.11.25"]
}

print(master_route_func(dict__))