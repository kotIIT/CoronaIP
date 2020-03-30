import json
import requests
import zipcodes
from pprint import pprint
import ipinfo

with requests.get("https://dph.illinois.gov/sites/default/files/COVID19/COVID19CountyResults20200330_2.json") as response:

    # for c in data["characteristics_by_county"]:
    print(response.json())
    data = response.json()['characteristics_by_county']['values']
    for item in data:
        # pprint(item)
        if item['County'] == 'Illinois':
            print("BUBBUBUBUBUBUBBUBUBUB")
            pprint(item)

            print(item['confirmed_cases'])

    # pprint(data)

# PublicIP = requests.get("https://ipinfo.io")
#
# print(PublicIP)
# print(PublicIP.json())

#zipcodes.matching  ()
#from geopy.geocoders import Nominatim