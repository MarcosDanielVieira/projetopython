# user/forms.py
from django import forms
from django.contrib.auth.models import Group, Permission,User
from django.contrib.admin.widgets import FilteredSelectMultiple


class GroupChangeForm(forms.ModelForm):
    name = forms.CharField(
        label="Nome do Grupo",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o nome do grupo'})
    )
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Permissões",
    )

    class Meta:
        model = Group
        # Campos que irão aparecer no formulário
        fields = ("name", "permissions")
        widgets = {  # mudando o tipo do input
            "permissions": FilteredSelectMultiple("Permissões", is_stacked=False),
        }

    class Media:
        css = {
            "all": ("css/group_form.css",)
        }  # <-- caminho relativo ao STATICFILES_DIRS

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome de usuário'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sobrenome'
            }),
        }