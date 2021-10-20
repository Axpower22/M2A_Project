from django.db.models import Model, CharField, IntegerField, BooleanField, ForeignKey, SET_NULL, DateField, EmailField
from localflavor.br.models import BRCNPJField, BRPostalCodeField, BRStateField, STATE_CHOICES


class UF(Model):
    sg_uf = CharField(max_length=2)
    nome_uf = CharField(max_length=500)

    def __str__(self):
        return f'{self.sg_uf} - {self.nome_uf}'


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
    telefone = CharField(blank=True, max_length=500)
    situacao = ForeignKey(Situacao, on_delete=SET_NULL, null=True)


class Grupo(Model):
    nome_grupo = CharField(max_length=500)


class Empresa(Model):
    cnpj = BRCNPJField()
    razao_social = CharField(max_length=500, unique=True)
    fantasia = CharField(max_length=500, unique=True)
    bool_master = BooleanField()
    inscricao_estadual = CharField(max_length=500, unique=True)
    num_empregados = IntegerField()

    email = EmailField(unique=True)

    dt_ano_inicio = DateField()

    projeto = CharField(max_length=500)
    nome_gestor = CharField(max_length=500)
    telefone_gestor = CharField(blank=True, max_length=500)

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

    # RESPONSAVEL
    FORMACAO_CHOICES = [
        ('Analfabeto', 'Analfabeto'),
        ('Primeiro grau', 'Primeiro grau'),
        ('Segundo grau', 'Segundo grau'),
        ('Superior', 'Superior'),
        ('Pós-Graduação', 'Pós-Graduação'),
        ('Mestrado e Doutorado', 'Mestrado e Doutorado')
    ]

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    nome_responsavel = CharField(max_length=500)
    email_responsavel = EmailField(unique=True)
    formacao_responsavel = CharField(choices=FORMACAO_CHOICES, max_length=500)
    sexo_responsavel = CharField(choices=SEXO_CHOICES, max_length=500)
    dt_nascimento_responsavel = DateField()

    # ENDEREÇO
    cep = BRPostalCodeField()
    logradouro = CharField(max_length=500)
    bairro = CharField(max_length=500)
    cidade = CharField(max_length=500)


class Faturamento(Model):
    fk_empresa = ForeignKey(Empresa, on_delete=SET_NULL, null=True, related_name='faturamentos')
    dt_ano = DateField()
    valor = IntegerField()


class TipoDiagnostico(Model):
    nome_tipo_diagnostico = CharField(max_length=500)


class FaseProjeto(Model):
    nome_fase = CharField(max_length=500)


class Diagnostico(Model):
    dt_ano = DateField()
    tipo = ForeignKey(TipoDiagnostico, on_delete=SET_NULL, null=True)
    fk_empresa = ForeignKey(Empresa, on_delete=SET_NULL, null=True)
    fase = ForeignKey(FaseProjeto, on_delete=SET_NULL, null=True)
