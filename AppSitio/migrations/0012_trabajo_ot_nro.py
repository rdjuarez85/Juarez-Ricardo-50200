# Generated by Django 5.0.1 on 2024-02-28 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSitio', '0011_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='ot_nro',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
