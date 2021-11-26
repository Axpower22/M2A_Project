from django.db.models import CharField, Model


class TipoDiagnostico(Model):
    nome_tipo_diagnostico = CharField(max_length=500)