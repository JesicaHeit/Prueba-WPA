# Generated by Django 3.0.8 on 2020-09-25 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200919_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
