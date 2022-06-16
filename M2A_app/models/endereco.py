from django.db.models import CharField
from localflavor.br.models import BRPostalCodeField

class Endereco(Model):
    cep = BRPostalCodeField()
    logradouro = CharField(max_length=500)
    bairro = CharField(max_length=500)
    cidade = CharField(max_length=500)
    complemento = CharField(blank=True, max_length=500)