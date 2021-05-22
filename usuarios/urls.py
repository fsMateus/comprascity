from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, novo_usuario, alterar_usuario

app_name = 'usuarios'
urlpatterns = [
    path('', index, name="index"),
    path('entrar/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html',
        extra_context={'titulo': 'Autenticação'}
    ), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name="logout"),
    path('novo_usuario/', novo_usuario, name="novo_usuario"),
    path('alterar_usuario/<int:pk>', alterar_usuario, name="alterar_usuario"),
]
