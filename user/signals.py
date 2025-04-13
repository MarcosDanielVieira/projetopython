from django.db.models.signals import post_migrate
from django.contrib.auth.models import Permission
from django.dispatch import receiver
from django.db import transaction


@receiver(post_migrate)
def traduzir_permissoes(sender, **kwargs):
    def traduzir():
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
            # Log
            "Can add log entry": "Pode adicionar entrada de log",
            "Can change log entry": "Pode alterar entrada de log",
            "Can delete log entry": "Pode excluir entrada de log",
            "Can view log entry": "Pode visualizar entrada de log",
            # Tipos de Conteúdo (ContentType)
            "Can add content type": "Pode adicionar tipo de conteúdo",
            "Can change content type": "Pode alterar tipo de conteúdo",
            "Can delete content type": "Pode excluir tipo de conteúdo",
            "Can view content type": "Pode visualizar tipo de conteúdo",
            # Produtos > Imagens
            "Can add Produto": "Pode adicionar produto",
            "Can change Produto": "Pode alterar produto",
            "Can delete Produto": "Pode excluir produto",
            "Can view Produto": "Pode visualizar produto",
            # Produtos > Imagens
            "Can add product image": "Pode adicionar imagem do produto",
            "Can change product image": "Pode alterar imagem do produto",
            "Can delete product image": "Pode excluir imagem do produto",
            "Can view product image": "Pode visualizar imagem do produto",
            # Sessões
            "Can add session": "Pode adicionar sessão",
            "Can change session": "Pode alterar sessão",
            "Can delete session": "Pode excluir sessão",
            "Can view session": "Pode visualizar sessão",
        }

        for codename, traducao in traducoes.items():
            perm = Permission.objects.filter(name=codename).first()
            if perm:
                perm.name = traducao
                perm.save()

    # Garante que a tradução aconteça após o commit da migração
    transaction.on_commit(traduzir)
