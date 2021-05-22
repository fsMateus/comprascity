import requests
from decouple import config
from json import loads, dumps


def find_company(cnpj):
    url_base = 'https://api.cnpja.com.br/companies/{CNPJ}'.format(CNPJ=cnpj)
    headers = {'authorization': '{KEY}'.format(KEY=config('KEY_CNPJA'))}

    response = requests.request("GET", url_base, headers=headers)
    print(type(response), response)
    print(type(response.json()), response.json())
    return response.json()


def save_data(company):
    from ..models import DataCompany, SecondaryActivities
    data = find_company(company.cnpj)
    print(type(data), data)

    data_company = DataCompany()
    data_company.cnpj = company
    data_company.name = data['name']
    data_company.alias = data['alias']
    data_company.type = data['type']
    data_company.phone = data['phone']
    data_company.registration_status = data['registration']['status']
    data_company.registration_date = data['registration']['status_date']
    data_company.state = data['address']['state']
    data_company.city = data['address']['city']
    data_company.street = data['address']['street']
    data_company.number = data['address']['number']
    data_company.zip = data['address']['zip']
    data_company.legal_nature_code = data['legal_nature']['code']
    data_company.legal_nature_description = data['legal_nature']['description']
    data_company.primary_activity_code = data['primary_activity']['code']
    data_company.primary_activity_description = data['primary_activity']['description']

    data_company.save()

    for item in data['secondary_activities']:
        secondary_activities = SecondaryActivities()
        secondary_activities.data_company_id = data_company
        secondary_activities.code = item['code']
        secondary_activities.description = item['description']

        secondary_activities.save()

    print(data_company)
    return data_company
