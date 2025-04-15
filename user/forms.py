# user/forms.py
from django import forms
from django.contrib.auth.models import Group, Permission
from django.contrib.admin.widgets import FilteredSelectMultiple


class GroupChangeForm(forms.ModelForm):
    name = forms.CharField(label="Nome do Grupo", max_length=150)
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Permissões",
    )

    class Meta:
        model = Group
        fields = ("name", "permissions")
        widgets = {
            "permissions": FilteredSelectMultiple("Permissões", is_stacked=False),
        }

    class Media:
        css = {
            "all": ("css/group_form.css",)
        }  # <-- caminho relativo ao STATICFILES_DIRS
