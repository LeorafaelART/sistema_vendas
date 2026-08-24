#########################################################################################
# IMPORTS
#########################################################################################
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Usuario


#########################################################################################
# ADMINISTRAÇÃO DO USUÁRIO
#########################################################################################
"""
    Registra o modelo Usuario no Django Admin.
    O decorator @admin.register(Usuario) informa ao Django
    "quero administrar este modelo através desta classe"
"""
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """
    Configuração de como os usuários serão exibidos
    e administrados dentro do Django Admin.
    """
    #---------------------------------------
    # COLUNAS DA LISTAGEM
    #---------------------------------------

    # Define quais informações aparecem na tabela de usuarios
    list_display=(
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )

    #---------------------------------------
    # COLUNAS DA LISTAGEM
    #---------------------------------------
    # Permite pesquisar usuarios pelo painel administrativo.
    search_fields=(
        "username",
        "email",
        "first_name",
        "last_name",
    )

    #---------------------------------------
    # CAMPOS EXTRAS
    #---------------------------------------
    """
        UserAdmin.fieldsets ja possui os campos padrão do Django
        Adicionei uma sessão com alguns campos adicionais
        "informações adicionais"
    """
    fieldsets= UserAdmin.fieldsets + (
        (
            "Informações adicionais",
            {
                "fields":(
                    "criado_em",
                    "atualizado_em"
                )
            },
        ),
    )

    #---------------------------------------
    # CAMPOS SOMENTE PARA LEITURA
    #---------------------------------------
    readonly_fields=(
        "criado_em",
        "atualizado_em",
    )