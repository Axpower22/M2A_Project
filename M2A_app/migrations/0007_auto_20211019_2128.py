# Generated by Django 3.2.8 on 2021-10-20 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('M2A_app', '0006_auto_20211019_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='bool_missao',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='bool_valores',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='bool_visao',
        ),
    ]
