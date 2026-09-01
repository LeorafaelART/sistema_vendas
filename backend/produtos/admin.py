#########################################################
# IMPORTS
#########################################################
from django.contrib import admin

# Importa os models app produto
from .models import(
    Autor,
    Categoria,
    Editora,
    Livro,
    Produto,
)

#########################################################
# ADMIN
#########################################################

#===============
# CATEGORIA
#===============
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    Configuração de como as categorias serão exibidas
    no Django Admin
    """
    # Colunas exibistas na listagem
    list_display=(
        "id",
        "nome",
    )

    # Campos que poderão ser pesquisados
    search_fields=(
        "nome",
    )

#===============
# PRODUTO
#===============
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Colunas exibidas na listagem
    list_display=(
        "id",
        "nome",
        "tipo_produto",
        "categoria",
        "preco",
        "ativo",
    )

    # Campos para pesquisa
    search_fields=(
        "nome",
        "codigo_barras",
    )

    # Filtros exibidos na lateral do admin
    list_filter=(
        "tipo_produto",
        "categoria",
        "ativo",
    )

#===============
# AUTOR
#===============
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "nome",
    )

    search_fields=(
        "nome",
    )

#===============
# EDITORA
#===============
@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "nome",
    )

    search_fields=(
        "nome",
    )

#===============
# LIVRO
#===============
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    """
    Configuração dos dados especificos de livros
    para o Django Admin.
    """
    list_display=(
        "id",
        "produto",
        "isbn",
        "editora",
        "ano_publicacao",
        "idioma",
    )

    search_fields=(
        "produto__nome",
        "isbn",
        "editora__nome",
    )

    list_filter=(
        "editora",
        "idioma",
        "ano_publicacao",
    )