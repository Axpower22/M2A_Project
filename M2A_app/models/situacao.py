from django.db.models import CharField, Model


class Situacao(Model):
    nome_situacao = CharField(max_length=500)

    def __str__(self):
        return self.nome_situacao
