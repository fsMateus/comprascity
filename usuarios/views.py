from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from django.contrib.auth.models import User


def index(request):
    context = dict()
    try:
        usuarios = User.objects.filter(is_active=True)
        context['lista_grid'] = usuarios
    except Exception as e:
        print(e)
        pass

    return render(request, 'usuarios/1_index/0_index.html', context)


def novo_usuario(request):
    form = UsuarioForm(request.POST or None)
    context = dict(form=form)

    if form.is_valid():
        form.save()

        return redirect("usuarios:index")

    return render(
        request, "usuarios/registra_usuario.html", context
    )


def alterar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    form = UsuarioForm(request.POST or None, instance=usuario)
    context = dict(form=form)

    if form.is_valid():
        form.save()

        return redirect("usuarios:index")

    return render(
        request, "usuarios/registra_usuario.html", context
    )
