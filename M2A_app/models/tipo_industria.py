from django.db.models import CharField, Model


class TipoIndustria(Model):
    ds_tipo_industria = CharField(max_length=500)