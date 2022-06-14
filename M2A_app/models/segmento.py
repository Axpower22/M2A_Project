from django.db.models import Model, CharField


class Segmento(Model):
    ds_segmento = CharField(max_length=500)

    def __str__(self):
        return self.ds_segmento