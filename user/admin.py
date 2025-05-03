from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.admin import GroupAdmin
from .forms import GroupChangeForm, CustomUserChangeForm, CustomUserCreationForm


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

# Filtro: Super usuário

class SuperUserFilter(admin.SimpleListFilter):
    title = "Superusuário"
    parameter_name = "is_superuser"
    template = "filter.html"  # mesmo template customizado

    def lookups(self, request, model_admin):
        return [
            ("1", "Sim"),
            ("0", "Não"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "1":
            return queryset.filter(is_superuser=True)
        elif self.value() == "0":
            return queryset.filter(is_superuser=False)
        return queryset
    
class IsActiveFilter(admin.SimpleListFilter):
    title = "Ativo"
    parameter_name = "is_active"
    template = "filter.html"  # mesmo template customizado

    def lookups(self, request, model_admin):
        return [
            ("1", "Sim"),
            ("0", "Não"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "1":
            return queryset.filter(is_active=True)
        elif self.value() == "0":
            return queryset.filter(is_active=False)
        return queryset
    
class GroupFilter(admin.SimpleListFilter):
    title = "Grupo"
    parameter_name = "group"
    template = "filter.html"  # usa o template customizado

    def lookups(self, request, model_admin):
        groups = Group.objects.all()
        return [(str(group.id), group.name) for group in groups]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(groups__id=self.value())
        return queryset
    
class IsStaffFilter(admin.SimpleListFilter):
    title = "Membro da equipe"
    parameter_name = "is_staff"
    template = "filter.html"  # mesmo template usado para Brand

    def lookups(self, request, model_admin):
        return [
            ("1", "Sim"),
            ("0", "Não"),
        ]

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
    form = CustomUserChangeForm
    fieldsets = (
        (("Informações de login"), {'fields': ('username', 'password','email')}),
        (("Informações pessoais"), {'fields': ('first_name', 'last_name', )}),
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
    
class CustomUserAdmin(DefaultUserAdmin):
    add_form = CustomUserCreationForm
    list_filter =(IsStaffFilter,SuperUserFilter,IsActiveFilter, GroupFilter)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    
     # Sobrescreve a view de listagem para adicionar o placeholder dinâmico
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        # Mapeia campos de busca para nomes mais amigáveis
        field_map = {
            "username": "Usuário",
            "first_name": "primeiro nome", 
            "email":"e-mail"
        }

        # Cria uma lista de nomes legíveis com base em search_fields
        search_labels = [
            field_map.get(field, field.replace("__", " de "))
            for field in self.search_fields
            if field != 'last_name' 
        ]

        # Monta a string final do placeholder
        placeholder = f"{', '.join(search_labels)}"

        # Envia o placeholder para o template
        extra_context["custom_search_placeholder"] = placeholder

        # Chama a view padrão com o contexto extra
        return super().changelist_view(request, extra_context=extra_context)


# Desregistra o admin padrão e registra o personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)
 
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
