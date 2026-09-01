#####################################
# IMPORTS
#####################################

from django.urls import path # função utlizada para criar as rotas
from . import views # importa as views do app usuario

#####################################
# ROTAS DO APP USUARIO
#####################################

urlpatterns=[
    
    # Quando o usuário acessar /login/
    # o Django executará a função login_view
    # que esta no views.py
    path("login/", views.login_view, name="login"),

    # Página inicial
    # Como o caminho está vazio "",
    # A rota sera: http://127.0.0.1:8000/
    path("", views.home_view, name="home"),

    # Rota para encerrar a sessão do usuário
    path("logout/", views.logout_view, name="logout"),

    # Página temporária para testar acesso
    # de Gerente e Administrador.
    path("gerencia/", views.gerencia_view, name="gerencia"),
]