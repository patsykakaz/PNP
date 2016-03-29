# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0013_auto_20160117_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageunivers',
            name='illustration',
            field=models.ImageField(upload_to='/home/patsykakaz/PNP/MAIN/static/media/SITES/universPNP', null=True, verbose_name='illustration', blank=True),
        ),
        migrations.AlterField(
            model_name='siteextension',
            name='img_banner',
            field=models.ImageField(help_text="banni\xe8re pour la page d'acceuil du sous-site", upload_to='/home/patsykakaz/PNP/MAIN/static/media/SITES/banner', null=True, verbose_name='banner', blank=True),
        ),
        migrations.AlterField(
            model_name='siteextension',
            name='img_logo',
            field=models.ImageField(upload_to='/home/patsykakaz/PNP/MAIN/static/media/SITES/logo', null=True, verbose_name='logo', blank=True),
        ),
    ]
