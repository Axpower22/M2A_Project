from django.db.models import CharField, Model


class FaseProjeto(Model):
    nome_fase = CharField(max_length=500)