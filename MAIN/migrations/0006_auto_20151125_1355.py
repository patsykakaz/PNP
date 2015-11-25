# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0005_auto_20151125_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteextension',
            name='illustration',
            field=models.ImageField(null=True, upload_to='/Users/patsykakaz_LSC/Documents/PRO/PNP/MAIN/static/media/SITES', blank=True),
        ),
    ]
