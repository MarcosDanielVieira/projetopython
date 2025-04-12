from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin


# Filtro: Ativo
class AtivoFilter(admin.SimpleListFilter):
    title = "Ativo"
    parameter_name = "is_active"
    template = "filter.html"

    def lookups(self, request, model_admin):
        return (("1", "Sim"), ("0", "Não"))

    def queryset(self, request, queryset):
        if self.value() == "1":
            return queryset.filter(is_active=True)
        elif self.value() == "0":
            return queryset.filter(is_active=False)
        return queryset


# Filtro: Membros da equipe (is_staff)
class MembrosEquipeFilter(admin.SimpleListFilter):
    title = "Membros da equipe"
    parameter_name = "is_staff"
    template = "filter.html"

    def lookups(self, request, model_admin):
        return (("1", "Sim"), ("0", "Não"))

    def queryset(self, request, queryset):
        if self.value() == "1":
            return queryset.filter(is_staff=True)
        elif self.value() == "0":
            return queryset.filter(is_staff=False)
        return queryset


# Filtro: Grupos
class GrupoFilter(admin.SimpleListFilter):
    title = "Grupo"
    parameter_name = "group"
    template = "filter.html"

    def lookups(self, request, model_admin):
        return [(str(group.id), group.name) for group in Group.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(groups__id=self.value())
        return queryset


# Admin customizado do User
class CustomUserAdmin(DefaultUserAdmin):
    list_filter = (
        AtivoFilter,
        MembrosEquipeFilter,
        GrupoFilter,
    )


# Re-registra o admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
