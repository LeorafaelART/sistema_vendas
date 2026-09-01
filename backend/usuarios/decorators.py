#########################################################################################
# IMPORTS
#########################################################################################

# wraps mantem informações da função original
# quando ela é envolvida pelo decorator.
from functools import wraps

from django.shortcuts import redirect

#==============================
# DECORATOR DE GRUPOS
#==============================

def grupo_requerido(*grupos_permitidos):
    """
    Decorator responsavel por permitir apenas para usuarios
    que pertencem a determinado grupo.
    """

    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # superusuários sempre terão acessos
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            # verifica se o usuário pertence a algum dos grupos
            possui_acesso= request.user.groups.filter(
                name__in= grupos_permitidos 
            ).exists()

            # caso não pertence a nenhum grupo volta para a home
            if not possui_acesso:
                return redirect("home")

            # se tiver acesso executa a view
            return view_func(request, *args, **kwargs)

        return wrapper
    return decorator