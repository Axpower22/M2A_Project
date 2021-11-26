from django.db.models import IntegerField, DateField, ForeignKey, Model, SET_NULL

from .empresa import Empresa


class Faturamento(Model):
    fk_empresa = ForeignKey(Empresa, on_delete=SET_NULL, null=True, related_name='faturamentos')
    dt_ano = DateField()
    valor = IntegerField()
