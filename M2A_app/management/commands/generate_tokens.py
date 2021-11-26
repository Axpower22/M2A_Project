from django.contrib.auth.models import User
from django.core.management import BaseCommand
from rest_framework.authtoken.models import Token


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
