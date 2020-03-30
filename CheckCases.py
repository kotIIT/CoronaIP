import json
import requests
import zipcodes
from pprint import pprint
import ipinfo


def get_covid_info_for_county_ILLINOIS(county: str) -> dict:
    with requests.get(
            "https://dph.illinois.gov/sites/default/files/COVID19/COVID19CountyResults20200330_2.json") as response:

        # for c in data["characteristics_by_county"]:
        # pprint(response.json())
        data = response.json()['characteristics_by_county']['values']
        for item in data:
            # pprint(item)
            if item['County'].upper() == county.upper():
                # print("BUBBUBUBUBUBUBBUBUBUB")
                return (item)

                # print(f"poop fuck: {item['confirmed_cases']}")

        raise Exception('Could not find County, asshole')


# def get_covid_county_stats

def get_county_from_zip(zip: str) -> dict:
    return zipcodes.matching(zip)


def get_county_from_current_ip() -> str:
    PublicIP = requests.get("https://ipinfo.io")
    zipcode_data = (zipcodes.matching(PublicIP.json()['postal']))
    county = zipcode_data[0]['county'].upper().replace("COUNTY", '').strip()
    return county


def get_shitty_from_current_ip() -> str:
    PublicIP = requests.get("https://ipinfo.io")
    city = PublicIP.json()['city']
    return city


def get_state_from_current_ip() -> str:
    PublicIP = requests.get("https://ipinfo.io")
    state = PublicIP.json()['region']
    return state


def get_loop_dose_stats():
    possible_counties = [
        get_state_from_current_ip(),
        get_shitty_from_current_ip(),
        get_county_from_current_ip(),
       ]

    for county in possible_counties:

        response = get_covid_info_for_county_ILLINOIS(county)
        print(response)


if __name__ == '__main__':
    get_loop_dose_stats()
    pass
