from django.db.models import IntegerField, DateField, Model, SET_NULL

# A empresa que tem o faturamento, e não o faturamento que tem a empresa
# from .empresa import Empresa 


class Faturamento(Model):
    # fk_empresa = ForeignKey(Empresa, on_delete=SET_NULL, null=True, related_name='faturamentos')
    dt_ano = DateField()
    valor = IntegerField()
