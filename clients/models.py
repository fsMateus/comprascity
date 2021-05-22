from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    user = models.ForeignKey(User, related_name='empresa', on_delete=models.PROTECT)
    cnpj = models.CharField(max_length=18, verbose_name='CNPJ')

    def __str__(self):
        return self.cnpj

    class Meta:
        verbose_name = 'Empresa'


class DataCompany(models.Model):
    cnpj = models.ForeignKey(Company, related_name='empresa_cnpj', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, verbose_name='Razão Social')
    alias = models.CharField(max_length=255, verbose_name='Nome Fantasia', blank=True, null=True)
    type = models.CharField(max_length=50, verbose_name='Tipo', blank=True, null=True)
    phone = models.CharField(max_length=50, verbose_name='Telefone', blank=True, null=True)
    registration_status = models.CharField(max_length=50, verbose_name='Situação Cadastral')
    registration_date = models.DateField(verbose_name='Data do Registro')
    state = models.CharField(max_length=50, verbose_name='Estado')
    city = models.CharField(max_length=100, verbose_name='Municipio')
    street = models.CharField(max_length=255, verbose_name='Logradouro')
    number = models.CharField(max_length=20, verbose_name='Número')
    zip = models.CharField(max_length=10, verbose_name='CEP')
    legal_nature_code = models.CharField(max_length=10, verbose_name='Natureza Legal - ID')
    legal_nature_description = models.CharField(max_length=100, verbose_name='Natureza Legal - Descrição')
    primary_activity_code = models.CharField(max_length=10, verbose_name='Atividade Primária - CNAE')
    primary_activity_description = models.CharField(max_length=100, verbose_name='Atividade Primária - Descrição')

    def __str__(self):
        return '{} # {}'.format(self.cnpj, self.name)

    class Meta:
        verbose_name = 'Dados da Empresa'


class SecondaryActivities(models.Model):
    data_company_id = models.ForeignKey(DataCompany, related_name='secondary_activities', on_delete=models.CASCADE)
    code = models.CharField(max_length=10, verbose_name='CNAE')
    description = models.CharField(max_length=100, verbose_name='Descrição')

    def __str__(self):
        return '{} # {}'.format(self.description, self.code)

    class Meta:
        verbose_name = 'Atividades Secundárias'