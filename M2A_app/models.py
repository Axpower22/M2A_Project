from django.db.models import Model, CharField, IntegerField, BooleanField, ForeignKey, SET_NULL, DateField, EmailField
from localflavor.br.models import BRCNPJField, BRPostalCodeField


class UF(Model):
    sg_uf = CharField(max_length=2)
    nome_uf = CharField(max_length=500)


class Setor(Model):
    ds_setor = CharField(max_length=500)


class Segmento(Model):
    ds_segmento = CharField(max_length=500)


class ValorArrecadacao(Model):
    ds_valor_arrecadacao = CharField(max_length=500)


class TipoIndustria(Model):
    ds_tipo_industria = CharField(max_length=500)


class Telefone(Model):
    ddd = IntegerField()
    telefone = IntegerField()

    TIPO_TELEFONE_CHOICES = [
        ('CEL', 'Celular'),
        ('FIX', 'Fixo'),
        ('FAX', 'Fax'),
    ]

    tipo_telefone = CharField(choices=TIPO_TELEFONE_CHOICES, max_length=500)


class Perfil(Model):
    nm_perfil = CharField(max_length=500)
    bool_admin = BooleanField()
    bool_excluido = BooleanField()


class Situacao(Model):
    nome_situacao = CharField(max_length=500)


class Usuario(Model):
    nome = CharField(max_length=500)
    email = EmailField()
    uf = ForeignKey(UF, on_delete=SET_NULL, null=True)
    telefone = ForeignKey(Telefone, on_delete=SET_NULL, null=True)
    situacao = ForeignKey(Situacao, on_delete=SET_NULL, null=True)


class Grupo(Model):
    nome_grupo = CharField(max_length=500)


class Empresa(Model):
    cnpj = BRCNPJField()
    razao_social = CharField(max_length=500)
    fantasia = CharField(max_length=500)
    bool_master = BooleanField()
    inscricao_estadual = IntegerField()
    num_empregados = IntegerField()

    email = EmailField()

    dt_ano_inicio = DateField()

    projeto = CharField(max_length=500)
    nome_gestor = CharField(max_length=500)

    grupo = ForeignKey(Grupo, on_delete=SET_NULL, null=True)

    # INFORMAÇÕES COMPLEMENTARES
    ds_negocio = CharField(max_length=500)
    bool_missao = BooleanField()
    missao = CharField(blank=True, max_length=500)
    bool_visao = BooleanField()
    visao = CharField(blank=True, max_length=500)
    bool_valores = BooleanField()
    valores = CharField(blank=True, max_length=500)

    # FOREIGN KEYS
    fk_tipo_master = ForeignKey("self", on_delete=SET_NULL, null=True)
    fk_segmento = ForeignKey(Segmento, on_delete=SET_NULL, null=True)
    fk_setor = ForeignKey(Setor, on_delete=SET_NULL, null=True)
    fk_valor_arrecadacao = ForeignKey(ValorArrecadacao, on_delete=SET_NULL, null=True)
    fk_tipo_industria = ForeignKey(TipoIndustria, on_delete=SET_NULL, null=True)

    # ENDEREÇO
    cep = BRPostalCodeField()
    logradouro = CharField(max_length=500)
    endereco = CharField(max_length=500)


class TipoDiagnostico(Model):
    nome_tipo_diagnostico = CharField(max_length=500)


class FaseProjeto(Model):
    nome_fase = CharField(max_length=500)


class Diagnostico(Model):
    dt_ano = DateField()
    tipo = ForeignKey(TipoDiagnostico, on_delete=SET_NULL, null=True)
    fk_empresa = ForeignKey(Empresa, on_delete=SET_NULL, null=True)
    fase = ForeignKey(FaseProjeto, on_delete=SET_NULL, null=True)
