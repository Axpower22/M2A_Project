from django.db.models import Model, CharField, ForeignKey, IntegerField

class Resposta(Model):
    pergunta = ForeignKey(Pergunta, on_delete=CASCADE, related_name='respostas')
    texto_resposta = CharField(max_length=500)
    valor = IntegerField()

    def __str__(self):
        return self.texto_resposta