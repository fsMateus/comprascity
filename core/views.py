from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Licitacoes, CONST
from .servicos import find_editais_for_activities, find_editais_for_words_key


@login_required
def index(request):
    companys = request.user.empresa.all()
    if not companys:
        return redirect('clients:index')

    aux_sugestoes = []
    for company in companys:
        dados = find_editais_for_activities(company)
        aux_sugestoes += dados

    context = dict()

    licitacoes = Licitacoes.objects.all()
    context['sugestoes'] = licitacoes.filter(pk__in=aux_sugestoes)

    filtro_modalidade = request.POST.get('filtro_modalidade', None)
    filtro_palavras = request.POST.get('filtro_palavras', None)

    if filtro_modalidade and filtro_modalidade.isdigit():
        licitacoes = licitacoes.filter(modalidade=int(filtro_modalidade))

    if filtro_palavras:
        palavras = filtro_palavras.split(',')
        itens = find_editais_for_words_key(palavras)
        licitacoes = licitacoes.filter(pk__in=itens)

    context['licitacoes'] = licitacoes
    context['MODALIDADE'] = CONST.MODALIDADE

    return render(request, 'core/index.html', context)
