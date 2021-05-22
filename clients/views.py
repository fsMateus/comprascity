from django.shortcuts import render
from django.views import generic
from .models import Company


class IndexView(generic.ListView):
    template_name = 'clients/index.html'
    context_object_name = 'empresas'

    def get_queryset(self):
        user = self.request.user
        empresas = user.empresa.all()

        return empresas


class DetailView(generic.DetailView):
    model = Company
    template_name = 'clients/detail.html'
