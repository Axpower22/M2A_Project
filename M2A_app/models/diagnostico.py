from django.conf import settings
from django.db.models import SET_NULL, ForeignKey, Model, DateField, CASCADE, CharField

from .empresa import Empresa
from .fase_projeto import FaseProjeto
from .tipo_diagnostico import TipoDiagnostico
# from .usuario_info import UsuarioInfo
# from .questionario import Questionario, Pergunta, Resposta


class Diagnostico(Model):
    data = DateField(auto_now_add=True)
    fase = CharField(max_length=500)

    tipo = ForeignKey(TipoDiagnostico, on_delete=SET_NULL, null=True)
    empresa = ForeignKey(Empresa, on_delete=SET_NULL, null=True)
    # O que o questionário tem a ver com o diagnóstico?
    # questionario = ForeignKey(Questionario, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f"{self.empresa.fantasia} - {self.fase} - {self.data.strftime('%d/%m/%Y')}"

    # @property
    # def risco(self):
    #     risco = 0
    #     for resposta_questionario in self.respostas.objects.all():
    #         risco += resposta_questionario.resposta.valor
    #     print(risco)
    #     return risco


'''class RespostaQuestionario(Model):
    diagnostico = ForeignKey(Diagnostico, on_delete=CASCADE, related_name='respostas')
    pergunta = ForeignKey(Pergunta, on_delete=CASCADE)
    resposta = ForeignKey(Resposta, on_delete=CASCADE)'''
