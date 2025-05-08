# config/context_processors.py

from django.templatetags.static import static
from django.conf import settings

def project_name(request):
    return {'project_name': settings.PROJECT_NAME}

def open_graph(request):
    # Dados padrão de Open Graph
    return { 
        'og_description': "Mapeamento de dados e construção de estratégias exclusivas para impulsionar venda de ingressos de shows e o sucesso de artistas",
        'og_image': static('img/hopen_favicon.ico'),
        'og_author': "Hopen Data",
    }