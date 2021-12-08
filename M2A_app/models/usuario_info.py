from django.contrib.auth.models import User
from django.db.models import CharField, ForeignKey, SET_NULL, OneToOneField, CASCADE, Model

from .empresa import Empresa
from .perfil import Perfil
from .situacao import Situacao
from .uf import UF


class UsuarioInfo(Model):
    user = OneToOneField(User, on_delete=CASCADE, default=1, related_name='info')

    nome = CharField(max_length=500)
    uf = ForeignKey(UF, on_delete=SET_NULL, null=True)
    telefone = CharField(blank=True, max_length=500)
    situacao = ForeignKey(Situacao, on_delete=SET_NULL, null=True)
    perfil = ForeignKey(Perfil, on_delete=SET_NULL, null=True)

    empresa = ForeignKey(Empresa, on_delete=SET_NULL, null=True, blank=True)

    FORMACAO_CHOICES = [
        ('Analfabeto', 'Analfabeto'),
        ('Primeiro grau', 'Primeiro grau'),
        ('Segundo grau', 'Segundo grau'),
        ('Superior', 'Superior'),
        ('Pós-Graduação', 'Pós-Graduação'),
        ('Mestrado e Doutorado', 'Mestrado e Doutorado')
    ]
    formacao = CharField(choices=FORMACAO_CHOICES, max_length=500)

    def __str__(self):
        return self.nome
