# filters.py
from django.contrib import admin
from django.contrib.auth.models import Group

class IsActiveFilter(admin.SimpleListFilter):
    title = "Ativo"
    parameter_name = "is_active"
    template = "filter.html"

    def lookups(self, request, model_admin):
        return [("1", "Sim"), ("0", "Não")]

    def queryset(self, request, queryset):
        if self.value() == "1":
            return queryset.filter(is_active=True)
        elif self.value() == "0":
            return queryset.filter(is_active=False)
        return queryset

class IsStaffFilter(admin.SimpleListFilter):
    title = "Membro da equipe"
    parameter_name = "is_staff"
    template = "filter.html"

    def lookups(self, request, model_admin):
        return [("1", "Sim"), ("0", "Não")]

    def queryset(self, request, queryset):
        if self.value() == "1":
            return queryset.filter(is_staff=True)
        elif self.value() == "0":
            return queryset.filter(is_staff=False)
        return queryset

class SuperUserFilter(admin.SimpleListFilter):
    title = "Superusuário"
    parameter_name = "is_superuser"
    template = "filter.html"

    def lookups(self, request, model_admin):
        return [("1", "Sim"), ("0", "Não")]

    def queryset(self, request, queryset):
        if self.value() == "1":
            return queryset.filter(is_superuser=True)
        elif self.value() == "0":
            return queryset.filter(is_superuser=False)
        return queryset

class GroupFilter(admin.SimpleListFilter):
    title = "Grupo"
    parameter_name = "group"
    template = "filter.html"

    def lookups(self, request, model_admin):
        return [(str(group.id), group.name) for group in Group.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(groups__id=self.value())
        return queryset
