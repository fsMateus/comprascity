from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import FormCompany


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


@login_required
def incluir(request):
    from .json.get_data_company import save_data
    form = FormCompany(request.POST or None)
    context = dict(form=form, VERBOSE_NAME='Empresa')

    try:
        if form.is_valid():
            modelo = form.save(commit=False)
            modelo.user = request.user
            modelo.save()

            save_data(modelo)

            return redirect('clients:detail', pk=modelo.pk)

    except Exception as e:
        print(e)

    return render(request, 'clients/incluir.html', context)
