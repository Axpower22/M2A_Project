from django.contrib.auth.models import User
from django.db.models import ForeignKey, CharField, EmailField, IntegerField, BooleanField, DateField, Model, SET_NULL, OneToOneField
from localflavor.br.models import BRPostalCodeField

from .grupo import Grupo
from .projeto import Projeto
from .segmento import Segmento
from .setor import Setor
from .tipo_industria import TipoIndustria
from .uf import UF
from .valor_arredacao import ValorArrecadacao
from .endereco import Endereco


class Empresa(Model):
    usuario = ForeignKey(User, on_delete=SET_NULL, null=True)

    cnpj = CharField(max_length=500, unique=True)
    razao_social = CharField(max_length=500, unique=True)
    fantasia = CharField(max_length=500, unique=True)
    bool_master = BooleanField()
    inscricao_estadual = CharField(blank=True, max_length=500, unique=True)
    num_empregados = IntegerField()

    # email = EmailField(unique=True)

    dt_ano_inicio = DateField()

    projeto = ForeignKey(Projeto, on_delete=SET_NULL, null=True)

    telefone = CharField(max_length=500)
    fax = CharField(blank=True, max_length=500)
    celular = CharField(max_length=500)

    # INFORMAÇÕES COMPLEMENTARES
    ds_negocio = CharField(max_length=500)
    missao = CharField(blank=True, max_length=500)
    visao = CharField(blank=True, max_length=500)
    valores = CharField(blank=True, max_length=500)

    # FOREIGN KEYS
    fk_grupo = ForeignKey(Grupo, on_delete=SET_NULL, null=True)
    fk_master = ForeignKey("self", on_delete=SET_NULL, null=True, blank=True)
    fk_segmento = ForeignKey(Segmento, on_delete=SET_NULL, null=True)
    fk_setor = ForeignKey(Setor, on_delete=SET_NULL, null=True)
    fk_valor_arrecadacao = ForeignKey(ValorArrecadacao, on_delete=SET_NULL, null=True)
    fk_tipo_industria = ForeignKey(TipoIndustria, on_delete=SET_NULL, null=True)
    fk_uf = ForeignKey(UF, on_delete=SET_NULL, null=True)
    fk_endereco = ForeignKey(Endereco, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.fantasia
