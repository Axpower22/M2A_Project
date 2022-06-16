from django.db.models import Model, CharField, ForeignKey, ManyToManyField

class Pergunta(Model):
    texto_pergunta = CharField(max_length=500)
    fundamento = ForeignKey(Fundamento, on_delete=CASCADE)
    questionario = ManyToManyField(Questionario, related_name='perguntas', blank=True, null=True)

    def __str__(self):
        return self.texto_pergunta