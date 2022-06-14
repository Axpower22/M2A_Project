from django.db.models import Model, CharField

class Fundamento(Model):
    nome_fundamento = CharField(max_length=500)

    def __str__(self):
        return self.nome_fundamento