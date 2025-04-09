# Importa o módulo admin do Django para customizar a interface administrativa
from django.contrib import admin

# Importa os modelos que serão registrados no Django Admin
from .models import Brand, Category, Product


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
    list_display = (
        "title",  # Título do produto
        "brand",  # Marca relacionada
        "category",  # Categoria relacionada
        "price",  # Preço do produto
        "is_active",  # Se está ativo ou não
        "created_at",  # Data de criação
        "updated_at",  # Data de atualização
    )
    # Define os campos de busca (atenção: "brand_name" e "category_name" precisam existir ou devem ser corrigidos)
    search_fields = ("title", "brand_name", "category_name")
    # Adiciona filtros laterais com base nesses campos
    list_filter = ("is_active", "brand", "category")
