# MVT

- Models (Arquivo responsável pelo banco de dados)
- View (Arquivo responsável pela lógica da aplicação)
- Templates (Arquivo responsável de mostrar o resultado para o usuário)

# Criar um ambiente virtual (recomendado):

- python -m venv venv
- .\venv\Scripts\Activate.ps1 (Entrar no ambiente virtual)

# Instalar Django:

- pip install django

# Criar o projeto

- django-admin startproject nome_projeto .

# Rodar o servidor local

- python manage.py runserver

# Criar um app

- python manage.py startapp meu_app (produtos, home, perfil, etc)
- Colocar o nome do app em settings.py no array INSTALLED_APPS
- Criar uma rota em urls.py no array urlpatterns
- Criar uma pasta templates e cria os html

# Criar uma migration

- python manage.py makemigrations
- python manage.py migrate

# Criar um usuário para fazer login no admin

- python manage.py createsuperuser
  - nome_usuario
  - email_usuario
  - senha_usuario

# Local dos arquivos ( img, js, css )

- Em settings.py no array STATICFILES_DIRS coloca o nome dos arquivos

# Comandos opcionais

- django-admin --version
