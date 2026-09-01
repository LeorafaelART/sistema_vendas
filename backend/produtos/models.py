#########################################################
# IMPORTS
#########################################################
from django.db import models


#########################################################
# MODELS
#########################################################

#=========================
# CATEGORIAS GERAIS
#=========================
class Categoria(models.Model):
    """
    Representa uma categoria do produto.
    Exemplos:
        -livros:
            - Romance
            - Ficção
            - História
            - Cinema
            - Musica
        
        - DVD's:
            - Terror
            - Suspense
            - Aventura
        
        Cd's Lp's:
            - Rock
            - MPB
            - Classica
    """

    # nome da categoria.
    nome= models.CharField(max_length= 100, unique= True)
    def __str__(self):
        """
        Define como a categoria sera exibida
        no Django Admin e em outras partes do sistema
        """
        return self.nome

#==================================
# PRODUTO
#==================================

class Produto(models.Model):
    """
    Representa  qualquer produto comercializado pelo sistema.
    Exemplo:
    - Livro
    - LP
    - CD
    - DVD
    """
    # Tipo de produtos permitidos inicialmente.
    #
    # O primeiro valor é o que salvo no banco.
    # O segundo é o que sera exibido no programa.

    TIPOS_PRODUTO=[
        ("LIVRO", "Livro"),
        ("LP", "LP"),
        ("CD", "CD"),
        ("DVD", "DVD"),
    ]

    # Nome comercial do produto.
    nome= models.CharField(
        max_length= 200
    )

    # Código de barras
    # blank=True: permite deixar o campo vazio em formulário
    # null=True: permite armazenar NULL no banco.
    codigo_barras= models.CharField(
        max_length=50,
        unique= True,
        blank= True,
        null= True
    )

    # Define o tipo de produto que esta sendo cadastrado.
    tipo_produto= models.CharField(
        max_length= 20,
        choices= TIPOS_PRODUTO

    )

    # Define a categoria relacionada ao produto
    # ForeignKey deixa que varios produtos pertecence a mesma categoria
    categoria= models.ForeignKey(
        Categoria,
        on_delete= models.PROTECT,
        related_name="produtos"
    )

    # Preço atual de venda
    # DecimalField é mais adequado pra dinheiro
    preco= models.DecimalField(
        max_digits= 10,
        decimal_places= 2
    )

    # Permite desativar o produto sem  apagar do banco
    ativo= models.BooleanField(
        default= True
    )

    # Data de criação do produto
    criado_em= models.DateTimeField(
        auto_now_add= True
    )

    # Data ultima alteração
    atualizado_em= models.DateTimeField(
        auto_now= True
    )

    def __str__(self):
        return self.nome

#==================================
#  CATEGORIAS: LIVRO
#==================================

#--------------------
# AUTOR
#--------------------
class Autor(models.Model):
    """
    Representa um autor de livros.
    Ex:
        - Machado de Assis
        - Geroge Orwell
        - Clarice Lispector
    """
    # Nome completo do autor
    nome= models.CharField(
        max_length= 200
    )

    def __str__(self):
        return self.nome

#--------------------
# EDITORA
#--------------------
class Editora(models.Model):
    """
    Representa a editora responsável pela publicação.
    Ex:
        - Companhia das Letras
        - Record
        - Intrínseca
    """
    # nome da editora.
    # unique= True impede nomes repetidos
    nome= models.CharField(
        max_length= 200,
        unique= True
    )

    def __str__(self):
        return self.nome

#--------------------
# LIVRO
#--------------------
class Livro(models.Model):
    """
    Armazena informações escíficas dos produtos que são livros
    dados gerais como Nome, Preço, Categoria, Codigo de barras
    fica no model Produto.
    """
    # Relaciona este liroa um único produto
    # OneToOneField: 
    # Um produto possui no máximo um registro Livro
    # e um Livro pertence a exatamente um Produto.
    produto= models.OneToOneField(
        Produto,
        on_delete= models.CASCADE,
        related_name= "livro"
    )

    # ISBN 
    # unique= True impede cadastrar ISBN 2x
    isbn= models.CharField(
        max_length= 20,
        unique= True
    )

    # Um livro pode ter varios autores.
    # E um autor pode participar de vários livros
    autores= models.ManyToManyField(
        Autor,
        related_name= "livros"
    )

    # Vários livros podem pertencer a mesma editora.
    editora= models.ForeignKey(
        Editora,
        on_delete= models.PROTECT,
        related_name= "livros"
    )

    # Número de pagina do livro
    numero_paginas= models.PositiveIntegerField(
        blank= True,
        null= True
    )

    # Ano de publicação
    ano_publicacao= models.PositiveIntegerField(
        blank= True,
        null= True
    )

    # Edição do livro
    edicao= models.CharField(
        max_length=  50,
        blank= True,
        null= True
    )

    # Idioma do livro
    idioma= models.CharField(
        max_length= 50,
        blank= True,
        null= True
    )

    # Peso em gramas
    peso_gramas= models.PositiveIntegerField(
        blank= True,
        null= True
    )

    # Volume da obra ou coleção
    volume= models.CharField(
        max_length= 50,
        blank= True,
        null= True
    )

    # Altura do livro em centímetros.
    altura_cm = models.DecimalField(
        max_digits= 5,
        decimal_places= 2,
        blank= True,
        null= True
    )

    # Largura do livro em centímetros.
    largura_cm = models.DecimalField(
        max_digits= 5,
        decimal_places= 2,
        blank= True,
        null= True
    )

    # Espessura do livro em centímetros.
    espessura_cm = models.DecimalField(
        max_digits= 5,
        decimal_places= 2,
        blank= True,
        null= True
    )

    def __str__(self):
        return self.produto.nome