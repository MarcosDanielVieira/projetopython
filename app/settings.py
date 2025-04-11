"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 5.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+#hs9rrdp2*qepgaw!!rb$o1____h8)lcd_yy5&a#%fd+y%@&_"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "ckeditor",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "base",
    "products",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "pt-BR"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

JAZZMIN_SETTINGS = {
    # título da janela (será padrão para current_admin_site.site_title se ausente ou None)
    "site_title": "SGP",
    # Título na tela de login (máx. 19 caracteres) (padrão para current_admin_site.site_header se ausente ou None)
    "site_header": "SGP",
    # Título na marca (máx. 19 caracteres) (padrão para current_admin_site.site_header se ausente ou None)
    "site_brand": "SGP",
    # Logo a ser usado para o seu site, deve estar presente nos arquivos estáticos, usado para a marca no canto superior esquerdo
    # "site_logo": "books/img/logo.png",
    # Logo a ser usado para o seu site, deve estar presente nos arquivos estáticos, usado para o logo do formulário de login (padrão para site_logo)
    "login_logo": None,
    # Logo a ser usado para o formulário de login em temas escuros (padrão para login_logo)
    "login_logo_dark": None,
    # Classes CSS que são aplicadas ao logo acima
    "site_logo_classes": "img-circle",
    # Caminho relativo para um favicon do seu site, será padrão para site_logo se ausente (idealmente 32x32 px)
    "site_icon": None,
    # Texto de boas-vindas na tela de login
    "welcome_sign": "Bem-vindo(a) ao SGP",
    # Copyright no rodapé
    "copyright": "Marcos Daniel",
    # Lista de model admins para pesquisar na barra de pesquisa, barra de pesquisa omitida se excluída
    # Se você quiser usar um único campo de pesquisa, não precisa usar uma lista, pode usar uma string simples
    "search_model": ["auth.User", "products.Product"],
    # Nome do campo no modelo de usuário que contém ImageField/URLField/Charfield do avatar ou um callable que recebe o usuário
    "user_avatar": None,
    ############
    # Menu Superior #
    ############
    # Links para colocar ao longo do menu superior
    "topmenu_links": [
        # URL que é revertida (Permissões podem ser adicionadas)
        {"name": "Início", "url": "admin:index", "permissions": ["auth.view_user"]},
        # URL externa que abre em uma nova janela (Permissões podem ser adicionadas)
        # {
        #     "name": "Suporte",
        #     "url": "https://github.com/farridav/django-jazzmin/issues",
        #     "new_window": True,
        # },
        # model admin para linkar (Permissões verificadas no modelo)
        # {"model": "auth.User"},
        # App com menu dropdown para todas as suas páginas de modelos (Permissões verificadas nos modelos)
        {"app": "books"},
    ],
    #############
    # Menu do Usuário #
    #############
    # Links adicionais para incluir no menu do usuário no canto superior direito (tipo de URL "app" não é permitido)
    # "usermenu_links": [
    #     {
    #         "name": "Suporte",
    #         "url": "https://github.com/farridav/django-jazzmin/issues",
    #         "new_window": True,
    #     },
    #     {"model": "auth.user"},
    # ],
    #############
    # Menu Lateral #
    #############
    # Se deve exibir o menu lateral
    "show_sidebar": True,
    # Se deve expandir automaticamente o menu
    "navigation_expanded": True,
    # Ocultar esses aplicativos ao gerar o menu lateral (ex: auth)
    "hide_apps": [],
    # Ocultar esses modelos ao gerar o menu lateral (ex: auth.user)
    "hide_models": [],
    # Lista de aplicativos (e/ou modelos) para basear a ordenação do menu lateral (não precisa conter todos os aplicativos/modelos)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    # Links personalizados para anexar a grupos de aplicativos, com chave no nome do aplicativo
    "custom_links": {
        "books": [
            {
                "name": "Criar Mensagens",
                "url": "make_messages",
                "icon": "fas fa-comments",
                "permissions": ["books.view_book"],
            }
        ]
    },
    # Ícones personalizados para aplicativos/modelos do menu lateral (https://fontawesome.com/search?o=r&ic=free&s=solid)
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "products.Brand": "fas fa-copyright",
        "products.Category": "fa fa-object-group",
        "products.Product": "fas fa-box",
    },
    # Ícones que são usados quando um não é especificado manualmente
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Modal Relacionado #
    #################
    # Usar modais em vez de popups
    "related_modal_active": False,
    #############
    # Ajustes de UI #
    #############
    # Caminhos relativos para scripts CSS/JS personalizados (devem estar presentes nos arquivos estáticos)
    "custom_css": None,
    "custom_js": None,
    # Se deve linkar a fonte de fonts.googleapis.com (use custom_css para fornecer a fonte caso contrário)
    "use_google_fonts_cdn": True,
    # Se deve mostrar o personalizador de UI na barra lateral
    "show_ui_builder": False,
    ###############
    # View de Alteração #
    ###############
    # Renderizar a view de alteração como um único formulário ou em abas, as opções atuais são
    # - single
    # - horizontal_tabs (padrão)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # substituir formulários de alteração por modeladmin
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # Adicionar um dropdown de idioma no admin
    # "language_chooser": True,
    # "show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-info",
    "accent": "accent-info",
    "navbar": "navbar-cyan navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
    "actions_sticky_top": True,
}

CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Custom",
        "toolbar_Custom": [
            ["Bold", "Italic", "Underline", "Strike"],
            ["NumberedList", "BulletedList"],
            ["Link", "Unlink"],
            ["RemoveFormat", "Source"],
        ],
        "removePlugins": "image,uploadimage",
        "height": 300,
        "width": "100%",
        "extraPlugins": "placeholder",
        "title": "Digite aqui o conteúdo...",
    }
}
