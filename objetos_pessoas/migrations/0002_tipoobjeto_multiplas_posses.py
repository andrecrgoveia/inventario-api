# Generated by Django 3.2.15 on 2023-05-10 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objetos_pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoobjeto',
            name='multiplas_posses',
            field=models.BooleanField(default=False, verbose_name='Pode ter múltiplas posses?'),
        ),
    ]
