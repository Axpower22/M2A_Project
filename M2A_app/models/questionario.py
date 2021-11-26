from django.db.models import Model, CharField, ForeignKey, CASCADE, IntegerField

from .empresa import Empresa


class Questionario(Model):
    empresa_master = ForeignKey(Empresa, on_delete=CASCADE)

    def __str__(self):
        return f"Questionario - {self.empresa_master.fantasia}"


class Fundamento(Model):
    nome_fundamento = CharField(max_length=500)

    def __str__(self):
        return self.nome_fundamento


class Pergunta(Model):
    texto_pergunta = CharField(max_length=500)
    fundamento = ForeignKey(Fundamento, on_delete=CASCADE)
    questionario = ForeignKey(Questionario, on_delete=CASCADE)

    def __str__(self):
        return self.texto_pergunta


class Resposta(Model):
    pergunta = ForeignKey(Pergunta, on_delete=CASCADE)
    texto_resposta = CharField(max_length=500)
    valor = IntegerField()

    def __str__(self):
        return self.texto_resposta
