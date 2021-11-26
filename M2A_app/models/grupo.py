from django.db.models import CharField, Model


class Grupo(Model):
    nome_grupo = CharField(max_length=500)