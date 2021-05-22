import requests
from decouple import config


def find_company(cnpj):
    url_base = 'https://api.cnpja.com.br/companies/{CNPJ}'.format(CNPJ=cnpj)
    headers = {'authorization': '{KEY}'.format(KEY=config('KEY_CNPJA'))}

    response = requests.request("GET", url_base, headers=headers)

    return response.json()
