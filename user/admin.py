# user\admin.py
from social_django.models import Association, Nonce, UserSocialAuth, Code
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin, GroupAdmin

# ========================
# FORMULÁRIOS PERSONALIZADOS
# ========================

from .forms import GroupChangeForm, CustomUserChangeForm, CustomUserCreationForm

# ========================
# FILTROS PERSONALIZADOS
# ========================

from .filters import IsActiveFilter, IsStaffFilter, SuperUserFilter, GroupFilter

# ========================
# ADMIN PERSONALIZADO
# ========================

class CustomUserAdmin(DefaultUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = (
        (("Informações de login"), {'fields': ('username', 'password', 'email')}),
        (("Informações pessoais"), {'fields': ('first_name', 'last_name')}),
        (("Permissões"), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (("Datas importantes"), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = (IsStaffFilter, SuperUserFilter, IsActiveFilter, GroupFilter)
    list_per_page = 20
    list_max_show_all = 100
    search_fields = ('username', 'first_name', 'email')
    ordering = ('username',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        field_map = {
            "username": "Usuário",
            "first_name": "primeiro nome",
            "email": "e-mail"
        }
        search_labels = [
            field_map.get(field, field.replace("__", " de "))
            for field in self.search_fields
            if field != 'last_name'
        ]
        extra_context["custom_search_placeholder"] = ", ".join(search_labels)
        return super().changelist_view(request, extra_context=extra_context)

# Admin customizado para Group
class CustomGroupAdmin(GroupAdmin):
    form = GroupChangeForm
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
    
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["custom_search_placeholder"] = "Nome do grupo"
        return super().changelist_view(request, extra_context=extra_context)

# ========================
# REGISTRO FINAL
# ========================

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)


# Ocultar os modelos do admin
for model in [Association, Nonce, UserSocialAuth, Code]:
    try:
        admin.site.unregister(model)
    except admin.sites.NotRegistered:
        pass