from django.db import models


# Importa a classe base 'models' do Django, usada para definir modelos que serão traduzidos para tabelas no banco de dados.
class Brand(models.Model):
    # Campo de texto com no máximo 100 caracteres, obrigatório por padrão. Representa o nome da marca.
    name = models.CharField(max_length=100, verbose_name="Nome")

    # Campo booleano que indica se a marca está ativa. Padrão é True.
    is_active = models.BooleanField(default=True, verbose_name="Ativo")

    # Campo de texto mais longo (sem limite definido). Pode ser nulo (null=True) e opcional no formulário (blank=True).
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")

    # Armazena a data/hora de criação do registro. É preenchido automaticamente no momento da criação.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    # Armazena a data/hora da última atualização do registro. É atualizado automaticamente a cada modificação.
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    # Classe interna usada para definir configurações adicionais do modelo
    class Meta:
        # Define a ordenação padrão dos objetos retornados pelo nome (ordem alfabética crescente)
        ordering = ["name"]

        # Define um nome legível (singular) para o modelo na interface administrativa do Django
        verbose_name = "Marca"
        verbose_name_plural = "Marca"

    # Método especial que define como a instância do modelo será representada como string (por exemplo, no admin)
    def __str__(self):
        return self.name


class Category(models.Model):
    # Campo de texto com no máximo 100 caracteres, obrigatório por padrão. Representa o nome da categoria.
    name = models.CharField(max_length=100, verbose_name="Nome")

    # Campo booleano que indica se a categoria está ativa. Padrão é True.
    is_active = models.BooleanField(default=True, verbose_name="Ativo")

    # Campo de texto mais longo (sem limite definido). Pode ser nulo (null=True) e opcional no formulário (blank=True).
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")

    # Armazena a data/hora de criação do registro. É preenchido automaticamente no momento da criação.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    # Armazena a data/hora da última atualização do registro. É atualizado automaticamente a cada modificação.
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    # Classe interna usada para definir configurações adicionais do modelo
    class Meta:
        # Define a ordenação padrão dos objetos retornados pelo nome (ordem alfabética crescente)
        ordering = ["name"]

        # Define um nome legível (singular) para o modelo na interface administrativa do Django
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    # Método especial que define como a instância do modelo será representada como string (por exemplo, no admin)
    def __str__(self):
        return self.name


class Product(models.Model):
    # Campo de texto com no máximo 100 caracteres, obrigatório por padrão. Representa o nome do produto.
    title = models.CharField(max_length=100, verbose_name="Título")

    # Chave estrangeira para o modelo Brand, criando um relacionamento muitos-para-um
    brand = models.ForeignKey(
        Brand,  # Modelo de destino (uma marca)
        on_delete=models.PROTECT,  # Impede a exclusão de uma marca se houver produtos associados
        related_name="products",  # Permite acessar os produtos a partir da marca (ex: brand.products.all())
        verbose_name="Marca",  # Nome legível para exibição em formulários e no admin
    )

    # Chave estrangeira para o modelo Brand, criando um relacionamento muitos-para-um
    category = models.ForeignKey(
        Category,  # Modelo de destino (uma categoria)
        on_delete=models.PROTECT,  # Impede a exclusão de uma categoria se houver produtos associados
        related_name="products",  # Permite acessar os produtos a partir da categoria (ex: brand.products.all())
        verbose_name="Categoria",  # Nome legível para exibição em formulários e no admin
    )

    # Campo para armazenar o preço do produto com duas casas decimais
    price = models.DecimalField(
        max_digits=10,  # Número total de dígitos (ex: 99999999.99 = 10 dígitos)
        decimal_places=2,  # Número de casas decimais (2 casas para valores monetários)
        verbose_name="Preço",  # Nome exibido no admin e em formulários
    )

    # Campo booleano que indica se a categoria está ativa. Padrão é True.
    is_active = models.BooleanField(default=True, verbose_name="Ativo")

    # Campo de texto mais longo (sem limite definido). Pode ser nulo (null=True) e opcional no formulário (blank=True).
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")

    # Armazena a data/hora de criação do registro. É preenchido automaticamente no momento da criação.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")

    # Armazena a data/hora da última atualização do registro. É atualizado automaticamente a cada modificação.
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    # Classe interna usada para definir configurações adicionais do modelo
    class Meta:
        # Define a ordenação padrão dos objetos retornados pelo nome (ordem alfabética crescente)
        ordering = ["title"]

        # Define um nome legível (singular) para o modelo na interface administrativa do Django
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    # Método especial que define como a instância do modelo será representada como string (por exemplo, no admin)
    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField("Images", upload_to="images")
    product = models.ForeignKey(
        Product, related_name="product_images", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.product.title)

    class Meta:
        verbose_name = "Imagens do produto"
