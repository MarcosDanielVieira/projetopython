# user/forms.py
from django import forms
from django.contrib.auth.models import Group, Permission,User
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django.contrib.auth.models import User

class GroupChangeForm(forms.ModelForm):
    name = forms.CharField(
        label="Nome do grupo",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o nome do grupo','class': 'form-control'})
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
    
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label='Primeiro nome',
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o primeiro nome',
            'class': 'form-control',
            'autocomplete': 'username'
        })
    )

    last_name = forms.CharField(
        label='Último nome',
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o sobrenome',
            'class': 'form-control'
        })
    )

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'placeholder': 'exemplo@email.com',
            'class': 'form-control',
            'autocomplete': 'username'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customiza os campos herdados do UserCreationForm
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nome de usuário',
            'class': 'form-control',
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Senha',
            'class': 'form-control'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirme a senha',
            'class': 'form-control'
        })


class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(
        label='Primeiro nome',
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o primeiro nome',
            'class': 'form-control',
            'autocomplete': 'username'        
        })
    )

    last_name = forms.CharField(
        label='Último nome',
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o sobrenome',
            'class': 'form-control'
        })
    )

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'placeholder': 'exemplo@email.com',
            'class': 'form-control',
            'autocomplete': 'username'
        })
    )
    
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Permissões"
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Nome de usuário',
            'class': 'form-control',
        })
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(username=self.instance.username).exists():
            raise forms.ValidationError("Este e-mail já está sendo utilizado por outro usuário.")
        return email

class CustomPasswordResetForm(PasswordResetForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail',
        })
        
    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Busca usuários ativos com este e-mail
        users = User.objects.filter(email=email, is_active=True)

        if not users.exists():
            raise forms.ValidationError("Este e-mail não está associado a um usuário ativo.")

        return email

    