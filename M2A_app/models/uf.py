from django.db.models import CharField, Model


class UF(Model):
    sg_uf = CharField(max_length=2)
    nome_uf = CharField(max_length=500)

    def __str__(self):
        return f'{self.sg_uf} - {self.nome_uf}'
