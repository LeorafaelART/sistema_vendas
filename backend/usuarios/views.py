#########################################################################################
# IMPORTS
#########################################################################################

# authenticate vierifica se o usuario realmente existe
# login cria a sessão do usuário autenticado
from django.contrib.auth import authenticate, login, logout

# login_required impede que usuarios não logados acessem determinadas paginas
from django.contrib.auth.decorators import login_required
from .decorators import grupo_requerido

# render permite retornar um arquivo HTML
# redirect permite redirecionar o usuario para outra URL
from django.shortcuts import render, redirect

#=====================
# LOGIN
#=====================

def login_view(request):
    """
    Responsável por:
    1. Exibir a págia de login.
    2. Receber usuário e senha.
    3. Validar as credenciais do usuário.
    4. Criar a sessão do usuário assim que ele logar.
    """
    # Verifica se o formulário foi enviado
    # GET -> apenas abre a página do usuário
    # POST -> usuário enviou o formulário

    if request.method == "POST":
        # Pega os valores enviados pelo formulario HTML
        username= request.POST.get("username")
        password= request.POST.get("password")

        # Tenta autenticar o usuário.
        #
        # Caso o login for valido retorna o objeto usuário
        # Se for inválido retorna None
        usuario= authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            # Cria a sessão de autenticação 
            #
            # Depois o django reconhece o request.user
            login(request, usuario)

            # Quando tiver a pagina inicial
            # Por enquanto isso redireciona para o nome da rota
            return redirect("home")

        # Caso autenticação falha retorna mensagem para o HTML
        contexto={
            "erro": "Usuário ou senha inválidos."
        }

        return render(request, "usuarios/login.html", contexto)

    # Se for GET, apenas exibe a pagina de login.
    return render(request, "usuarios/login.html")

#--------------
# LOGOUT
#--------------
@login_required
def logout_view(request):
    """
        Responsvavel por encerrar a sessão do usuário.
    """
    # Remove a sessão atual do usuário
    logout(request)

    # Depois de sair redireciona para o pagina de login
    return redirect("login")

#=====================
# HOME
#=====================

@login_required
def home_view(request):
    """
        Responsável por exibir a pagina inicial do sistema.

        @login_required verifica se o usuario esta logado
    """
    # Busca todos os grupos aos quais o usupario pertence
    #
    # values_list("name", flat=True) retorna apenas os nomes dos grupos
    grupos= request.user.groups.values_list("name", flat=True)

    # Dados enviados para o template
    contexto={
        "grupos": grupos
    }

    # Renderiza o HTML da pagina inicial
    return render(request, "usuarios/home.html", contexto)

#=====================
# GERENCIA
#=====================
@login_required
@grupo_requerido("Gerente", "Administrador")
def gerencia_view(request):
    """
        Página temporaria para testar controle de acesso
        através dos grupos do Django
    """
    return render(request, "usuarios/gerencia.html")

