# Hopen Data

Este sistema utiliza partes do template AdminLTE (https://adminlte.io), licenciado sob a Licença MIT.
Copyright (c) 2014-2024 Colorlib


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

# Para tradução de mensagens
- Rode o comando para criar os arquivos .po (se ainda não tiver):
- limitar o comando makemessages para buscar apenas nas pastas da aplicação
  - django-admin makemessages -l pt_BR -i venv/

- No arquivo locale/pt_BR/LC_MESSAGES/django.po, adicione a tradução
  - msgid "Choose permissions by selecting them and then select the \"Choose\" arrow button."
  - msgstr "Escolha as permissões selecionando-as e depois clique no botão de seta \"Escolher\"."

- Compile o arquivo
  - django-admin compilemessages


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
- python --version
- python manage.py collectstatic (Rode collectstatic no ambiente de produção (caso for subir))
- python manage.py popular_dados (Roda os dados faker de popular_dados.py)´

- pip freeze > requirements.txt (guarda os pacotes instalados do venv)
- pip install -r .\requirements.txt (instala tudo que foi guardado)
- python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  - geração de SECRET_KEY, não colocar "aspas duplas"

# Template de referencia
- https://adminlte.io/themes/v3/index.html
