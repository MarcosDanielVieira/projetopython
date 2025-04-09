# MVT

- Models (Arquivo responsável pelo banco de dados)
- View (Arquivo responsável pela lógica da aplicação)
- Templates (Arquivo responsável de mostrar o resultado para o usuário)

# Criar um ambiente virtual:

- python -m venv venv
- .\venv\Scripts\Activate.ps1
  - Entrar no ambiente virtual

# Instalar Django:

- pip install django

# Criar o projeto

- django-admin startproject app .
  - ou
- django-admin startproject core .

# Criar uma migration

- python manage.py makemigrations
- python manage.py migrate

# Criar um usuário para fazer login no admin

- python manage.py createsuperuser
  - nome_usuario
  - email_usuario
  - senha_usuario

# Rodar o servidor local

- python manage.py runserver

# Criar um app

- python manage.py startapp meu_app (produtos, home, perfil, etc)
- Colocar o nome do app em settings.py no array INSTALLED_APPS
- Criar uma rota em urls.py no array urlpatterns
- Criar uma pasta templates e cria os html

# Local dos arquivos ( img, js, css )

- Em settings.py no array STATICFILES_DIRS coloca o nome dos arquivos

# Configurando o admin

- No app que criou (produtos, home, perfil, etc), deve-se registrar
  - @admin.register(Brand)
    - class BrandAdmin(admin.ModelAdmin):
      - list_display = ("name", "is_active", "description", "created_at", "updated_at")
      - search_fields = ("name",)
      - list_filter = ("is_active",)

# Comandos opcionais

- django-admin --version
