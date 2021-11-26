from django.db.models import CharField, Model


class ValorArrecadacao(Model):
    ds_valor_arrecadacao = CharField(max_length=500)