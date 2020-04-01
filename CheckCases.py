import json
import requests
import zipcodes
from pprint import pprint
from datetime import date
import ipinfo


def get_covid_info_for_county_ILLINOIS(county: str) -> dict:
    curr_date = get_current_date()
    url = "https://dph.illinois.gov/sites/default/files/COVID19/COVID19CountyResults"
    with requests.get(url + curr_date + ".json") as response:

        # for c in data["characteristics_by_county"]:
        # pprint(url + curr_date + ".json")
        # pprint(response.json())
        data = response.json()['characteristics_by_county']['values']
        for item in data:
            # pprint(item)
            if item['County'].upper() == county.upper():
                # print("BUBBUBUBUBUBUBBUBUBUB")
                return item

                # print(f"poop fuck: {item['confirmed_cases']}")

        raise Exception('Could not find County, asshole')


# def get_covid_county_stats

def get_current_date() -> str:
    today = date.today()
    curr_date = today.strftime("%Y%m%d")
    return curr_date


def get_county_from_zip(zip: str) -> dict:
    return zipcodes.matching(zip)


def get_county_from_current_ip() -> str:
    public_ip = requests.get("https://ipinfo.io")
    zipcode_data = (zipcodes.matching(public_ip.json()['postal']))
    county = zipcode_data[0]['county'].upper().replace("COUNTY", '').strip()
    return county


def get_shitty_from_current_ip() -> str:
    public_ip = requests.get("https://ipinfo.io")
    city = public_ip.json()['city']
    return city


def get_state_from_current_ip() -> str:
    public_ip = requests.get("https://ipinfo.io")
    state = public_ip.json()['region']
    return state


def get_loop_dose_stats():
    possible_counties = [
        get_county_from_current_ip(),
        get_state_from_current_ip(),
        get_shitty_from_current_ip(),

    ]

    for county in possible_counties:
        try:
            response = get_covid_info_for_county_ILLINOIS(county)
            print(response)
        except:
            pass


if __name__ == '__main__':
    get_loop_dose_stats()
    pass
