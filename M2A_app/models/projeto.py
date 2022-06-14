from django.db.models import SET_NULL, CharField, ForeignKey, Model


# from .empresa import Empresa

class Projeto(Model):
    nome_projeto = CharField(max_length=500)
    # cliente_master = ForeignKey(Empresa, on_delete=SET_NULL, null=True)
