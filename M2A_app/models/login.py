from django.db.models import CharField, Model

class Login(Model):
    username = CharField(max_length=60)
    password = CharField(max_length=60)