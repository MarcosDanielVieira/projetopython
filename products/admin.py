# Importa o módulo admin do Django para customizar a interface administrativa
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html

# Importa os modelos que serão registrados no Django Admin
from .models import Brand, Category, Product, ProductImage
from .forms import ProductForm
import csv


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


# Filtro personalizado para o campo is_active
class ActiveFilter(admin.SimpleListFilter):
    title = "Ativo"
    parameter_name = "is_active"
    template = "filter.html"  # Caminho relativo a base/templates

    def lookups(self, request, model_admin):
        return (("1", "Sim"), ("0", "Não"))

    def queryset(self, request, queryset):
        if self.value() == "1":
            return queryset.filter(is_active=True)
        elif self.value() == "0":
            return queryset.filter(is_active=False)
        return queryset


class BrandFilter(admin.SimpleListFilter):
    title = "Marca"
    parameter_name = "brand"
    template = "filter.html"  # Usa o mesmo template customizado

    def lookups(self, request, model_admin):
        # Retorna uma tupla com id e nome da marca
        brands = Brand.objects.all()
        return [(str(brand.id), brand.name) for brand in brands]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(brand__id=self.value())
        return queryset


# Registra o modelo Brand no Django Admin usando um decorator
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    # Define quais campos serão exibidos na lista do admin
    list_display = ("name", "is_active", "description", "created_at", "updated_at")
    # Habilita o campo "name" como campo de busca
    search_fields = ("name",)
    # Adiciona filtros laterais baseados no campo "is_active"
    list_filter = (ActiveFilter,)


# Registra o modelo Category no Django Admin com suas configurações específicas
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "description", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = (ActiveFilter,)


@admin.action(description="Ativar produtos selecionados")
def activate_product(self, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Desativar produtos selecionados")
def disable_product(self, request, queryset):
    queryset.update(is_active=False)


# Registra o modelo Product no Django Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    form = ProductForm
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
    list_display = (
        "title",  # Título do produto
        "brand",  # Marca relacionada
        "category",  # Categoria relacionada
        "price",  # Preço do produto
        "is_active",  # Se está ativo ou não
        "created_at",  # Data de criação
        "updated_at",  # Data de atualização
    )
    # list_editable = ("title",) # (não pode ser o 1° item da listagem (por ser um link))
    # Define os campos de busca (atenção: "brand__name" e "category__name" precisam existir ou devem ser corrigidos)
    search_fields = ("title", "brand__name", "category__name")
    # Adiciona filtros laterais com base nesses campos
    list_filter = (ActiveFilter, BrandFilter, "category")
    autocomplete_fields = ["brand", "category"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="products.csv"'
        writer = csv.writer(response, delimiter=";")
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
    actions = [export_to_csv, activate_product, disable_product]
