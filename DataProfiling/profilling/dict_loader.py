import os
import logging
logger = logging.getLogger(__name__)
logger.info("модуль запустился")
dict_path = os.path.join('data', 'dict')

data_types_path = os.path.join(dict_path, 'data_type.csv')

acct_chart_path = os.path.join(dict_path, 'acct_chart.csv')
currency_code_path = os.path.join(dict_path, 'currency_code.csv')
postal_code_path = os.path.join(dict_path, 'postal_code.csv')

country_path = os.path.join(dict_path, 'country.csv')
region_path = os.path.join(dict_path, 'regions.csv')
city_path = os.path.join(dict_path, 'city.csv')
street_path = os.path.join(dict_path, 'streets.csv')

men_first_names_path = os.path.join(dict_path, 'men_first_names.csv')
women_first_names_path = os.path.join(dict_path, 'women_first_names.csv')
men_middle_names_path = os.path.join(dict_path, 'men_middle_names.csv')
women_middle_names_path = os.path.join(dict_path, 'women_middle_names.csv')
men_last_names_path = os.path.join(dict_path, 'men_last_names.csv')
women_last_names_path = os.path.join(dict_path, 'women_last_names.csv')
unisex_last_names_path = os.path.join(dict_path, 'unisex_last_names.csv')
men_first_names_eng_path = os.path.join(dict_path, 'men_first_names_eng.csv')
women_first_names_eng_path = os.path.join(dict_path, 'women_first_names_eng.csv')
men_middle_names_eng_path = os.path.join(dict_path, 'men_middle_names_eng.csv')
women_middle_names_eng_path = os.path.join(dict_path, 'women_middle_names_eng.csv')
men_last_names_eng_path = os.path.join(dict_path, 'men_last_names_eng.csv')
women_last_names_eng_path = os.path.join(dict_path, 'women_last_names_eng.csv')
unisex_last_names_eng_path = os.path.join(dict_path, 'unisex_last_names_eng.csv')

phone_numbers_path = os.path.join(dict_path, 'phone_numbers.csv')
postal_codes_path = os.path.join(dict_path, 'postal_code.csv')

data_types_map = dict()

postal_codes = set()
acct_charts = set()
currency_codes = set()
phone_numbers = set()

countries = set()
regions = set()
cities = set()
streets = set()

first_names = set()
first_names_eng = set()
men_first_names = set()
men_first_names_eng = set()
women_first_names = set()
women_first_names_eng = set()
middle_names = set()
middle_names_eng = set()
men_middle_names = set()
men_middle_names_eng = set()
women_middle_names = set()
women_middle_names_eng = set()
last_names = set()
last_names_eng = set()
men_last_names = set()
men_last_names_eng = set()
women_last_names = set()
women_last_names_eng = set()
unisex_last_names = set()
unisex_last_names_eng = set()


def load_data_types(file_path):
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            data_types_map[line.split(":")[1].strip()] = line.split(":")[0].strip()


def load_acct_chart(file_path):
    with open(file_path, encoding='utf-8') as file:
        for acct_chart in file:
            if acct_chart not in acct_charts:
                acct_charts.add(acct_chart.rstrip('\n'))


def load_phone_number(file_path):
    with open(file_path, encoding='utf-8') as file:
        for phone_number in file:
            if phone_number not in phone_numbers:
                phone_numbers.add(phone_number.rstrip('\n'))


def load_currency_code(file_path):
    with open(file_path, encoding='utf-8') as file:
        for currency_code in file:
            if currency_code not in currency_codes:
                currency_codes.add(currency_code.rstrip('\n'))


def load_postal_code(file_path):
    with open(file_path, encoding='utf-8') as file:
        for postal_code in file:
            if postal_code not in postal_codes:
                postal_codes.add(postal_code.rstrip('\n'))


def load_first_names():
    with open(men_first_names_path, encoding='utf-8') as f:
        for first_name in f:
            men_first_names.add(first_name.rstrip('\n'))
            first_names.add(first_name.rstrip('\n'))
    with open(women_first_names_path, encoding='utf-8') as f:
        for first_name in f:
            women_first_names.add(first_name.rstrip('\n'))
            first_names.add(first_name.rstrip('\n'))


def load_first_names_eng():
    with open(men_first_names_eng_path, encoding='utf-8') as f:
        for first_name_eng in f:
            men_first_names_eng.add(first_name_eng.rstrip('\n'))
            first_names_eng.add(first_name_eng.rstrip('\n'))
    with open(women_first_names_eng_path, encoding='utf-8') as f:
        for first_name_eng in f:
            women_first_names_eng.add(first_name_eng.rstrip('\n'))
            first_names_eng.add(first_name_eng.rstrip('\n'))


def load_last_names():
    with open(unisex_last_names_path, encoding='utf-8') as f:
        for last_name in f:
            unisex_last_names.add(last_name.rstrip('\n'))
            last_names.add(last_name.rstrip('\n'))
    with open(men_last_names_path, encoding='utf-8') as f:
        for last_name in f:
            men_last_names.add(last_name.rstrip('\n'))
            last_names.add(last_name.rstrip('\n'))
    with open(women_last_names_path, encoding='utf-8') as f:
        for last_name in f:
            women_last_names.add(last_name.rstrip('\n'))
            last_names.add(last_name.rstrip('\n'))


def load_last_names_eng():
    with open(unisex_last_names_eng_path, encoding='utf-8') as f:
        for last_name in f:
            unisex_last_names_eng.add(last_name.rstrip('\n'))
            last_names_eng.add(last_name.rstrip('\n'))
    with open(men_last_names_eng_path, encoding='utf-8') as f:
        for last_name in f:
            men_last_names_eng.add(last_name.rstrip('\n'))
            last_names_eng.add(last_name.rstrip('\n'))
    with open(women_last_names_eng_path, encoding='utf-8') as f:
        for last_name in f:
            women_last_names_eng.add(last_name.rstrip('\n'))
            last_names_eng.add(last_name.rstrip('\n'))


def load_middle_names():
    with open(men_middle_names_path, encoding='utf-8') as f:
        for middle_name in f:
            men_middle_names.add(middle_name.rstrip('\n'))
            middle_names.add(middle_name.rstrip('\n'))
    with open(women_middle_names_path, encoding='utf-8') as f:
        for middle_name in f:
            women_middle_names.add(middle_name.rstrip('\n'))
            middle_names.add(middle_name.rstrip('\n'))


def load_middle_names_eng():
    with open(men_middle_names_eng_path, encoding='utf-8') as f:
        for middle_name_eng in f:
            men_middle_names_eng.add(middle_name_eng.rstrip('\n'))
            middle_names_eng.add(middle_name_eng.rstrip('\n'))
    with open(women_middle_names_eng_path, encoding='utf-8') as f:
        for middle_name_eng in f:
            women_middle_names_eng.add(middle_name_eng.rstrip('\n'))
            middle_names_eng.add(middle_name_eng.rstrip('\n'))


def load_country():
    with open(country_path, encoding='utf-8') as file:
        for country in file:
            if country not in countries:
                countries.add(country.lower().rstrip('\n'))


def load_region():
    with open(region_path, encoding='utf-8') as file:
        for region in file:
            if region not in regions:
                regions.add(region.rstrip('\n'))


def load_streets():
    with open(street_path, encoding='utf-8') as file:
        for street in file:
            if street not in streets:
                streets.add(street.rstrip('\n'))


def load_city():
    with open(city_path, encoding='utf-8') as file:
        for city in file:
            if city not in cities:
                cities.add(city.rstrip('\n'))


def load_datamasking_dicts():
    load_data_types(data_types_path)
    load_first_names()
    load_first_names_eng()
    load_last_names()
    load_last_names_eng()
    load_middle_names()
    load_middle_names_eng()

    load_acct_chart(acct_chart_path)
    load_currency_code(currency_code_path)
    load_phone_number(phone_numbers_path)
    load_postal_code(postal_codes_path)
    load_streets()
    load_country()
    load_region()
    load_city()


load_datamasking_dicts()
