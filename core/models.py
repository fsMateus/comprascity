from django.db import models


class CONST(object):
    class MODALIDADE(object):
        CONCORRENCIA = 0
        CONVITE = 1
        TOMADA_PRECO = 2
        LEILAO = 3
        CONCURSO = 4
        PREGAO = 5

        choices = (
            (CONCORRENCIA, u'Concorrência'),
            (CONVITE, u'Convite / Carta-convite'),
            (TOMADA_PRECO, u'Tomada de Preços'),
            (LEILAO, u'Leilão'),
            (CONCURSO, u'Concurso'),
            (PREGAO, u'Pregão'),
        )

        as_dict = dict(choices)


class Licitacoes(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    dou = models.CharField(max_length=50, verbose_name='DOU - Identificação', unique=True)
    data_lancamento = models.DateTimeField(auto_now_add=True)
    data_abertura = models.DateTimeField(verbose_name='Data de abertura', null=True)
    orgao = models.CharField(max_length=100, verbose_name='Orgão', null=True)
    resumo = models.TextField()
    modalidade = models.IntegerField(choices=CONST.MODALIDADE.choices, verbose_name='Modalidade')
    edital = models.FileField(upload_to='media/documents')

    def __str__(self):
        return '{}#{}'.format(self.titulo, self.dou)

    class Meta:
        verbose_name = 'Licitações'
