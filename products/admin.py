# Importa o módulo admin do Django para customizar a interface administrativa
from django.contrib import admin
from django.http import HttpResponse

# Importa os modelos que serão registrados no Django Admin
from .models import Brand, Category, Product, ProductImage
import csv


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


# Registra o modelo Brand no Django Admin usando um decorator
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    # Define quais campos serão exibidos na lista do admin
    list_display = ("name", "is_active", "description", "created_at", "updated_at")
    # Habilita o campo "name" como campo de busca
    search_fields = ("name",)
    # Adiciona filtros laterais baseados no campo "is_active"
    list_filter = ("is_active",)


# Registra o modelo Category no Django Admin com suas configurações específicas
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "description", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("is_active",)


# Registra o modelo Product no Django Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = (
        "title",  # Título do produto
        "brand",  # Marca relacionada
        "category",  # Categoria relacionada
        "price",  # Preço do produto
        "is_active",  # Se está ativo ou não
        "created_at",  # Data de criação
        "updated_at",  # Data de atualização
    )
    # Define os campos de busca (atenção: "brand__name" e "category__name" precisam existir ou devem ser corrigidos)
    search_fields = ("title", "brand__name", "category__name")
    # Adiciona filtros laterais com base nesses campos
    list_filter = ("is_active", "brand", "category")
    autocomplete_fields = ["brand", "category"]

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="products.csv"'
        writer = csv.writer(response)
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
                    product.brand.name,
                    product.category.name,
                    product.price,
                    product.is_active,
                    product.description,
                    product.created_at,
                    product.updated_at,
                ]
            )

        return response

    export_to_csv.short_description = "Exportar para CSV"
    actions = [export_to_csv]
