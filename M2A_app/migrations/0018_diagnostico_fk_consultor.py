# Generated by Django 3.2.8 on 2021-11-25 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('M2A_app', '0017_auto_20211120_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostico',
            name='fk_consultor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='M2A_app.usuarioinfo'),
        ),
    ]
