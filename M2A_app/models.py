from django.db.models import Model, CharField, IntegerField, BooleanField, ForeignKey, SET_NULL, DateField, EmailField
from localflavor.br.models import BRCNPJField, BRPostalCodeField


class UF(Model):
    sg_uf = CharField()
    nome_uf = CharField()


class Setor(Model):
    ds_setor = CharField()


class Segmento(Model):
    ds_segmento = CharField()


class ValorArrecadacao(Model):
    ds_valor_arrecadacao = CharField()


class TipoIndustria(Model):
    ds_tipo_industria = CharField()


class Telefone(Model):
    ddd = IntegerField()
    telefone = IntegerField()

    TIPO_TELEFONE_CHOICES = [
        ('CEL', 'Celular'),
        ('FIX', 'Fixo'),
        ('FAX', 'Fax'),
    ]

    tipo_telefone = CharField(choices=TIPO_TELEFONE_CHOICES)


class Perfil(Model):
    nm_perfil = CharField()
    bool_admin = BooleanField()
    bool_excluido = BooleanField()


class Situacao(Model):
    nome_situacao = CharField()


class Usuario(Model):
    nome = CharField()
    email = EmailField()
    uf = ForeignKey(UF, on_delete=SET_NULL)
    telefone = ForeignKey(Telefone, on_delete=SET_NULL)
    situacao = ForeignKey(Situacao, on_delete=SET_NULL)


class Grupo(Model):
    nome_grupo = CharField()


class Empresa(Model):
    cnpj = BRCNPJField()
    razao_social = CharField()
    fantasia = CharField()
    bool_master = BooleanField()
    inscricao_estadual = IntegerField()
    num_empregados = IntegerField()

    email = EmailField()

    dt_ano_inicio = DateField()

    projeto = CharField()
    nome_gestor = CharField()

    grupo = ForeignKey(Grupo, on_delete=SET_NULL, null=True)

    # INFORMAÇÕES COMPLEMENTARES
    ds_negocio = CharField()
    bool_missao = BooleanField()
    missao = CharField(blank=True)
    bool_visao = BooleanField()
    visao = CharField(blank=True)
    bool_valores = BooleanField()
    valores = CharField(blank=True)

    # FOREIGN KEYS
    fk_tipo_master = ForeignKey("self", on_delete=SET_NULL)
    fk_segmento = ForeignKey(Segmento, on_delete=SET_NULL)
    fk_setor = ForeignKey(Setor, on_delete=SET_NULL)
    fk_valor_arrecadacao = ForeignKey(ValorArrecadacao, on_delete=SET_NULL)
    fk_tipo_industria = ForeignKey(TipoIndustria, on_delete=SET_NULL)

    # ENDEREÇO
    cep = BRPostalCodeField()
    logradouro = CharField()
    endereco = CharField()


class TipoDiagnostico(Model):
    nome_tipo_diagnostico = CharField()


class FaseProjeto(Model):
    nome_fase = CharField()


class Diagnostico(Model):
    dt_ano = DateField()
    tipo = ForeignKey(TipoDiagnostico, on_delete=SET_NULL)
    fk_empresa = ForeignKey(Empresa, on_delete=SET_NULL)
    fase = ForeignKey(FaseProjeto, on_delete=SET_NULL)
