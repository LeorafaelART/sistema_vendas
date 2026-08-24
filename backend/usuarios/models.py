#=================================
# IMPORTS
#=================================
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    """
        Modelo de usuário personalizado para o sistema.

        Aproveitando o que Django ja fornece
        AbstractUser Herda todos esses campos abaixo

        - username
        - senha
        - nome
        - sobrenome
        - permissões
        - grupos
        - usuário ativo/inativo
        - acesso ao admin

        E adicionamos campos específicos do nosso projeto.
    """

    # Email do usuário
    # unique= True permite que 2 usuarios usem o mesmo email
    email= models.EmailField(
        unique= True,
        verbose_name="E-mail"
    )

    # Data e hora em que o usuário foi criado
    # auto_now_add= True preenche automático apenas na criação
    criado_em= models.DateTimeField(
        auto_now_add= True
    )

    atualizado_em= models.DateTimeField(
        auto_now= True
    )

    