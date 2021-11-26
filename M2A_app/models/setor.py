from django.db.models import Model, CharField


class Setor(Model):
    ds_setor = CharField(max_length=500)