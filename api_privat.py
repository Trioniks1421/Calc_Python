import requests
import json
from pprint import pprint
PRIVAT_BANK_URL='https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

response  = requests.get(PRIVAT_BANK_URL).text
response_to_json  = json.loads(response)
print(type(response_to_json) , response_to_json)

for elem in response_to_json:
    for key in elem:
        print('{} --- {}'.format(key , elem[key]))
    print('----')
