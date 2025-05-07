# user\signals.py

from django.db.models.signals import post_migrate
from django.contrib.auth.models import Permission
from django.dispatch import receiver
from django.db import transaction


@receiver(post_migrate)
def traduzir_permissoes(sender, **kwargs):
    def traduzir():
        traducoes = {
            # Usuário
            "Can add user": "Pode adicionar usuário",
            "Can change user": "Pode alterar usuário",
            "Can delete user": "Pode excluir usuário",
            "Can view user": "Pode visualizar usuário",
        
            # Grupo
            "Can add group": "Pode adicionar grupo",
            "Can change group": "Pode alterar grupo",
            "Can delete group": "Pode excluir grupo",
            "Can view group": "Pode visualizar grupo",
          
            # Permissão
            "Can add permission": "Pode adicionar permissão",
            "Can change permission": "Pode alterar permissão",
            "Can delete permission": "Pode excluir permissão",
            "Can view permission": "Pode visualizar permissão",
          
            # Log
            "Can add log entry": "Pode adicionar entrada de log",
            "Can change log entry": "Pode alterar entrada de log",
            "Can delete log entry": "Pode excluir entrada de log",
            "Can view log entry": "Pode visualizar entrada de log",

            # Sessões
            "Can add session": "Pode adicionar sessão",
            "Can change session": "Pode alterar sessão",
            "Can delete session": "Pode excluir sessão",
            "Can view session": "Pode visualizar sessão",
            
            # Tipos de Conteúdo (ContentType)
            "Can add content type": "Pode adicionar tipo de conteúdo",
            "Can change content type": "Pode alterar tipo de conteúdo",
            "Can delete content type": "Pode excluir tipo de conteúdo",
            "Can view content type": "Pode visualizar tipo de conteúdo",
        }

        permissions = Permission.objects.filter(name__in=traducoes.keys())
        for perm in permissions:
            if perm.name in traducoes:
                perm.name = traducoes[perm.name]
                perm.save()

    # Garante que a tradução aconteça após o commit da migração
    transaction.on_commit(traduzir)

@receiver(post_migrate)
def remove_social_permissions(sender, **kwargs):
    from django.contrib.contenttypes.models import ContentType
    content_types = ContentType.objects.filter(app_label='social_django')
    Permission.objects.filter(content_type__in=content_types).delete()