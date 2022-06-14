from django.db.models import Model, CharField, ForeignKey, CASCADE, IntegerField, ManyToManyField, OneToOneField

from .empresa import Empresa


class Questionario(Model):
    empresa_master = OneToOneField(Empresa, on_delete=CASCADE, related_name='questionario')

    def __str__(self):
        return f"Questionario - {self.empresa_master.fantasia}"

