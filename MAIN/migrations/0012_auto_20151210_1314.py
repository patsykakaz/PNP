# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0011_pageunivers_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageunivers',
            name='illustration',
            field=models.ImageField(upload_to='/Users/patsykakaz_LSC/Documents/PRO/PNP/MAIN/static/media/SITES/universPNP', null=True, verbose_name='illustration', blank=True),
        ),
        migrations.AlterField(
            model_name='publicite',
            name='media',
            field=models.ImageField(null=True, upload_to='/Users/patsykakaz_LSC/Documents/PRO/PNP/MAIN/static/media/publicite'),
        ),
        migrations.AlterField(
            model_name='siteextension',
            name='img_banner',
            field=models.ImageField(help_text="banni\xe8re pour la page d'acceuil du sous-site", upload_to='/Users/patsykakaz_LSC/Documents/PRO/PNP/MAIN/static/media/SITES/banner', null=True, verbose_name='banner', blank=True),
        ),
        migrations.AlterField(
            model_name='siteextension',
            name='img_logo',
            field=models.ImageField(upload_to='/Users/patsykakaz_LSC/Documents/PRO/PNP/MAIN/static/media/SITES/logo', null=True, verbose_name='logo', blank=True),
        ),
    ]
