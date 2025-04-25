from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.admin import GroupAdmin
from .forms import GroupChangeForm


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
    fieldsets = (
        (("Informações básicas"), {'fields': ('username', 'password')}),
        (("Informações pessoais"), {'fields': ('first_name', 'last_name', 'email')}),
        (("Permissões"), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (("Datas importantes"), {'fields': ('last_login', 'date_joined')}),
    )
    list_filter = (
        AtivoFilter,
        MembrosEquipeFilter,
        GrupoFilter,
    )
    list_per_page = 20  # Listando 20 itens por página
    list_max_show_all = 100  # Só mostra tudo se tiver mais de 200


class CustomGroupAdmin(GroupAdmin):
    form = GroupChangeForm
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)

# Re-registra o admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
