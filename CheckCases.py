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

    return None


def get_county_from_zip(zip: str) -> dict:
    return zipcodes.matching(zip)


def get_county_from_current_ip() -> str:
    PublicIP = requests.get("https://ipinfo.io")

    # print(PublicIP)
    # pprint(PublicIP.json())

    zipcode_data = (zipcodes.matching(PublicIP.json()['postal']))

    # pprint(zipcode_data)

    county = zipcode_data[0]['county'].upper().replace("COUNTY", '').strip()

    return county


if __name__ == '__main__':
    # pprint(get_covid_info_for_county_ILLINOIS('lake'))

    print(get_county_from_current_ip())

    # zipcodes.matching  ()
    # from geopy.geocoders import Nominatim
