# Generated by Django 3.1 on 2020-10-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0009_auto_20201013_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Activa'), (2, 'Bloqueada')], null=True),
        ),
    ]
