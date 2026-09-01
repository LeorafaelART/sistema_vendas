#########################################################################################
# IMPORTS
#########################################################################################

# import padrão admin django
from django.contrib import admin

# include que permite carregar as URLs de outros apps
# Path 
from django.urls import include, path

#########################################################################################
# ROTAS PRINCIPAIS DO PROJETO
#########################################################################################

urlpatterns= [
    # Painel administrativo
    path("admin/", admin.site.urls),

    # Inclui as rotas do app usuarios.
    # Deixando o prefixo vazio ""
    # vai puxar por padrão a rota defina em usuarios/urls.py
    # "/login"
    # http://127.0.0.1:8000/login/

    path("", include("usuarios.urls")),

]