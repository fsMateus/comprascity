import fitz
from .models import Licitacoes
from clients.models import DataCompany


def get_activities(company):
    data_company = DataCompany.objects.get(cnpj=company)
    activities = []

    activities.append(data_company.primary_activity_description)
    words_description = data_company.primary_activity_description.split(' ')
    for word in words_description:
        if len(word) > 4:
            activities.append(word)

    for item in data_company.secondary_activities.all():
        words_description = item.description.split(' ')
        for word in words_description:
            if len(word) > 4:
                activities.append(word)
        activities.append(item.code)

    return activities


def find_editais_for_activities(company):
    activities = get_activities(company.pk)
    checks = []

    licitacoes = Licitacoes.objects.all()
    for item in licitacoes:

        for word in activities:
            if word in item.resumo or word in item.content_edital:
                checks.append(item.pk)

    return checks


def find_editais_for_words_key(words):
    checks = []

    licitacoes = Licitacoes.objects.all()
    for item in licitacoes:

        for word in words:
            if word in item.resumo or word in item.content_edital:
                checks.append(item.pk)

    return checks


def extract_text_to_pdf(licitacao):
    doc = fitz.open(licitacao.edital.path)

    content = ''
    for page in doc:
        content += page.getText('text')

    licitacao.content_edital = content
    licitacao.save()
