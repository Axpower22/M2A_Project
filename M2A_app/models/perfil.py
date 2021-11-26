from django.db.models import BooleanField, CharField, Model


class Perfil(Model):
    nm_perfil = CharField(max_length=500)
    bool_admin = BooleanField()
    bool_excluido = BooleanField()

    def __str__(self):
        return self.nm_perfil

    class Meta:
        verbose_name_plural = 'Perfis'
