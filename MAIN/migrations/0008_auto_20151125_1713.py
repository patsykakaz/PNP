# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0007_auto_20151125_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteextension',
            name='illustration',
        ),
        migrations.AddField(
            model_name='siteextension',
            name='img_banner',
            field=models.ImageField(null=True, upload_to='/Users/patsykakaz_LSC/Documents/PRO/PNP/MAIN/static/media/SITES/banner', blank=True),
        ),
        migrations.AddField(
            model_name='siteextension',
            name='img_logo',
            field=models.ImageField(null=True, upload_to='/Users/patsykakaz_LSC/Documents/PRO/PNP/MAIN/static/media/SITES/logo', blank=True),
        ),
    ]
