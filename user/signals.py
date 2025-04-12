from django.db.models.signals import post_migrate
from django.contrib.auth.models import Permission
from django.dispatch import receiver


@receiver(post_migrate)
def traduzir_permissoes(sender, **kwargs):
    traducoes = {
        # Usuário
        "Can add User": "Pode adicionar usuário",
        "Can change User": "Pode alterar usuário",
        "Can delete User": "Pode excluir usuário",
        "Can view User": "Pode visualizar usuário",
        # Grupo
        "Can add Group": "Pode adicionar grupo",
        "Can change Group": "Pode alterar grupo",
        "Can delete Group": "Pode excluir grupo",
        "Can view Group": "Pode visualizar grupo",
        # Produtos > Categoria
        "Can add Categoria": "Pode adicionar categoria",
        "Can change Categoria": "Pode alterar categoria",
        "Can delete Categoria": "Pode excluir categoria",
        "Can view Categoria": "Pode visualizar categoria",
        # Permissão
        "Can add permission": "Pode adicionar permissão",
        "Can change permission": "Pode alterar permissão",
        "Can delete permission": "Pode excluir permissão",
        "Can view permission": "Pode visualizar permissão",
        # Produtos
        "Can add produtos": "Pode adicionar produto",
        "Can change produtos": "Pode alterar produto",
        "Can delete produtos": "Pode excluir produto",
        "Can view produtos": "Pode visualizar produto",
        # Produtos > Marca
        "Can add Marca": "Pode adicionar marca",
        "Can change Marca": "Pode alterar marca",
        "Can delete Marca": "Pode excluir marca",
        "Can view Marca": "Pode visualizar marca",
        # Log (LogEntry do admin)
        "Can add log entry": "Pode adicionar entrada de log",
        "Can change log entry": "Pode alterar entrada de log",
        "Can delete log entry": "Pode excluir entrada de log",
        "Can view log entry": "Pode visualizar entrada de log",
    }

    for codename, traducao in traducoes.items():
        perm = Permission.objects.filter(name=codename).first()
        if perm:
            perm.name = traducao
            perm.save()
