# Importa o módulo admin do Django para customizar a interface administrativa
from django.contrib import admin
from django.http import HttpResponse

# Importa os modelos e formulários usados no admin
from .models import Brand, Category, Product, ProductImage
from .forms import ProductForm
import csv


# Configuração para adicionar imagens do produto diretamente no admin
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0  # Não exibe linhas extras vazias por padrão


# Filtro personalizado para o campo is_active (Sim/Não)
class ActiveFilter(admin.SimpleListFilter):
    title = "Ativo"
    parameter_name = "is_active"
    template = "filter.html"  # Template customizado de filtro

    def lookups(self, request, model_admin):
        # Define as opções do filtro: Sim (1) ou Não (0)
        return (("1", "Sim"), ("0", "Não"))

    def queryset(self, request, queryset):
        # Filtra de acordo com a seleção do usuário
        if self.value() == "1":
            return queryset.filter(is_active=True)
        elif self.value() == "0":
            return queryset.filter(is_active=False)
        return queryset


# Filtro lateral para filtrar por marca (brand)
class BrandFilter(admin.SimpleListFilter):
    title = "Marca"
    parameter_name = "brand"
    template = "filter.html"  # Usa o mesmo template customizado

    def lookups(self, request, model_admin):
        # Retorna uma lista de marcas como (id, nome)
        brands = Brand.objects.all()
        return [(str(brand.id), brand.name) for brand in brands]

    def queryset(self, request, queryset):
        # Filtra os produtos pela marca selecionada
        if self.value():
            return queryset.filter(brand__id=self.value())
        return queryset


# Admin da tabela Brand
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "description",
                    "created_at", "updated_at")
    search_fields = ("name",)  # Campo de busca
    list_filter = (ActiveFilter,)  # Filtro lateral


# Admin da tabela Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "description",
                    "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = (ActiveFilter,)


# Ação personalizada para ativar produtos em massa
@admin.action(description="Ativar produtos selecionados")
def activate_product(self, request, queryset):
    queryset.update(is_active=True)


# Ação personalizada para desativar produtos em massa
@admin.action(description="Desativar produtos selecionados")
def disable_product(self, request, queryset):
    queryset.update(is_active=False)


# Admin da tabela Product (produto)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Permite adicionar imagens no mesmo formulário
    inlines = [ProductImageInline]
    form = ProductForm  # Formulário customizado para produtos

    # Organização dos campos do formulário em seções
    fieldsets = (
        (
            "Geral",
            {
                "fields": (
                    "title",
                    "brand",
                    "category",
                    "price",
                    "is_active",
                    "description",
                )
            },
        ),
    )

    # Campos exibidos na listagem do admin
    list_display = (
        "title",
        "brand",
        "category",
        "price",
        "is_active",
        "created_at",
        "updated_at",
    )

    # Campos usados para busca (busca automática no admin)
    search_fields = ("title", "brand__name", "category__name")

    # Filtros laterais
    list_filter = (ActiveFilter, BrandFilter, "category")

    # Usa autocomplete para seleção de marca e categoria
    autocomplete_fields = ["brand", "category"]

    # Lista de ações disponíveis no admin
    actions = [activate_product, disable_product]

    # Ação personalizada para exportar os dados em CSV
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="products.csv"'
        writer = csv.writer(response, delimiter=";")

        # Cabeçalho do CSV
        writer.writerow(
            [
                "titulo",
                "marca",
                "categoria",
                "preço",
                "ativo",
                "descrição",
                "criado em",
                "atualizado em",
            ]
        )

        # Dados do CSV
        for product in queryset:
            writer.writerow(
                [
                    product.title,
                    product.brand.name if product.brand else "",
                    product.category.name if product.category else "",
                    product.price,
                    product.is_active,
                    product.description,
                    product.created_at,
                    product.updated_at,
                ]
            )

        return response

    export_to_csv.short_description = "Exportar para CSV"
    actions.append(export_to_csv)  # Adiciona a ação na lista

    # Sobrescreve a view de listagem para adicionar o placeholder dinâmico
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        # Mapeia campos de busca para nomes mais amigáveis
        field_map = {
            "title": "Título",
            "brand__name": "marca",
            "category__name": "categoria",
        }

        # Cria uma lista de nomes legíveis com base em search_fields
        search_labels = [
            field_map.get(field, field.replace("__", " de "))
            for field in self.search_fields
        ]

        # Monta a string final do placeholder
        placeholder = f"{', '.join(search_labels)}"

        # Envia o placeholder para o template
        extra_context["custom_search_placeholder"] = placeholder

        # Chama a view padrão com o contexto extra
        return super().changelist_view(request, extra_context=extra_context)
