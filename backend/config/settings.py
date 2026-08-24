#########################################################################################
# IMPORTS
#########################################################################################

import os
from pathlib import Path

from dotenv import load_dotenv

"""
Configurações principais do projeto Sistema de Vendas.

Neste arquivo ficam configurações como:

- Banco de dados
- Aplicações instaladas
- Segurança
- Idioma
- Fuso horário
- Templates
- Arquivos estáticos
- Usuário personalizado
"""

#########################################################################################
# CAMINHOS DO PROJETO
#########################################################################################
"""
Define a pasta base do projeto Django
o arquivo settings.py está em:
    sistema_vendas/backend/config/settings.py

porém a base do projeto sera:
    sistema_vendas/.env
"""
BASE_DIR= Path(__file__).resolve().parent.parent

#########################################################################################
# VARIAVEIS DE AMBIENTE
#########################################################################################
"""
Nosso arquivo .env está em:
sistema_vendas/.env

Como BASE_DIR representa "backend",
uso BASE_DIR.parent para voltar uma pasta.
"""

load_dotenv(BASE_DIR.parent / ".env")

#########################################################################################
# CONFIGURAÇÕES DE SEGURANÇA
#########################################################################################
"""
Chave secreta utilizada internamente pelo Django.
"""
SECRET_KEY = os.getenv("SECRET_KEY")

#########################################################################################
# ALTERAR MODO
#########################################################################################
"""
DEBUG=True mostra informações detalhadas sobre erros.
Em produção alterar para False.
"""
DEBUG = os.getenv("DEBUG", "False") == "True"

#########################################################################################
# HOSTS PERMITIDOS
#########################################################################################

"""
Define quais endereços podem acessar a aplicação.
Durante o desenvolvimento podemos deixar vazio.
"""
ALLOWED_HOSTS = []

#########################################################################################
# APLICAÇÕES INSTALADAS
#########################################################################################

INSTALLED_APPS = [

    # --------------------------------------------------------
    # Aplicações internas do próprio Django
    # --------------------------------------------------------

    # Painel administrativo do Django.
    "django.contrib.admin",

    # Sistema de autenticação: usuários, grupos e permissões.
    "django.contrib.auth",

    # Permite que o Django trabalhe com diferentes tipos
    # de modelos cadastrados no projeto.
    "django.contrib.contenttypes",

    # Sistema de sessões.
    # Permite, por exemplo, manter um usuário logado.
    "django.contrib.sessions",

    # Sistema de mensagens temporárias.
    # Exemplo: "Produto cadastrado com sucesso".
    "django.contrib.messages",

    # Gerenciamento de arquivos estáticos:
    # CSS, JavaScript, imagens etc.
    "django.contrib.staticfiles",


    # --------------------------------------------------------
    # Bibliotecas externas
    # --------------------------------------------------------

    # Django REST Framework.
    # Será utilizado futuramente para construirmos nossa API.
    "rest_framework",


    # --------------------------------------------------------
    # Aplicações criadas no projeto
    # --------------------------------------------------------

    # App responsável pelos usuários do Sistema de Vendas.
    "usuarios",
]

#########################################################################################
# MIDDLEWARES
#########################################################################################

# Middlewares são componentes executados durante o processamento

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

#########################################################################################
# CONFIGURAÇÃO PRINCIPAL DE HTMLS
#########################################################################################

# Informa ao Django onde está o arquivo principal de rotas.
ROOT_URLCONF = "config.urls"

#########################################################################################
# TEMPLATES HTML
#########################################################################################

# Configura como o Django localizará e renderizará os arquivos HTML.

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # Criar uma pasta global para os templates
        "DIRS": [],

        # Permite que o Django procure templates dentro dos apps.
        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


#########################################################################################
# CONFIGURAÇÃO WSGI
#########################################################################################

# Utilizada para executar a aplicação Django em servidores web.
# Não precisamos alterar isso durante o desenvolvimento inicial.
WSGI_APPLICATION = "config.wsgi.application"

#########################################################################################
# BANCO DE DADOS
#########################################################################################

# Configuração da conexão entre Django e PostgreSQL.
# Os dados sensíveis ficam armazenados no arquivo .env.

DATABASES = {
    "default": {

        # Define que utilizaremos PostgreSQL.
        "ENGINE": "django.db.backends.postgresql",

        # Nome do banco.
        "NAME": os.getenv("DB_NAME"),

        # Usuário do PostgreSQL.
        "USER": os.getenv("DB_USER"),

        # Senha do PostgreSQL.
        "PASSWORD": os.getenv("DB_PASSWORD"),

        # Endereço onde o PostgreSQL está rodando.
        "HOST": os.getenv("DB_HOST"),

        # Porta utilizada pelo PostgreSQL.
        "PORT": os.getenv("DB_PORT"),
    }
}

#########################################################################################
# VALIDAÇÃO DE SENHAS
#########################################################################################

# Regras utilizadas pelo Django para evitar senhas SIMPLES ou INSEGURAS

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

#########################################################################################
# IDIOMA E FUSO LOCAL
#########################################################################################

# Define português do Brasil como idioma do projeto.
LANGUAGE_CODE = "pt-br"

# Define o horário utilizado pela aplicação.
TIME_ZONE = "America/Sao_Paulo"

# Ativa o sistema de internacionalização do Django.
USE_I18N = True

# Mantém suporte a fusos horários.
USE_TZ = True

#########################################################################################
# ARQUIVOS ESTÁTICOS
#########################################################################################

# URL utilizada para arquivos como CSS, JavaScript e imagens.
STATIC_URL = "static/"

#########################################################################################
# USUÁRIO PERSONALIZADO
#########################################################################################

# Informa ao Django que não utilizaremos diretamente
# o modelo de usuário padrão.
#
# Nosso usuário está definido em:
# usuarios/models.py
#
# Formato:
# "nome_do_app.NomeDaClasse"
AUTH_USER_MODEL = "usuarios.Usuario"