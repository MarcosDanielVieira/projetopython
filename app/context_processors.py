from django.conf import settings

def project_name(request):
    return {'project_name': settings.PROJECT_NAME}
