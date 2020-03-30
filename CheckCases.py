import json, urllib.request, pprint


with urllib.request.urlopen("https://dph.illinois.gov/sites/default/files/COVID19/COVID19CountyResults20200330_2.json") as url:
    data = json.loads(url.read())
    for c in data["characteristics_by_county"]:
        print(f'County  {c["values"]["County"]}')

        # print(f 'County:{c["values"[]]County})
        # print('Cases: ' + c['confirmed_cases'])
        # print('Deaths: ' + c['deaths'])
        # print('')

